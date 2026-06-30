"""CNN architecture for fracture detection."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from tensorflow import keras
from tensorflow.keras import layers, regularizers
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
from tensorflow.keras.models import Sequential

if TYPE_CHECKING:
    from src.config import Config

TRANSFER_BASE_NAME = "efficientnet_backbone"


def build_data_augmentation(config: Config) -> keras.Sequential:
    """Notebook-style augmentation (v1): flip + rotation only."""
    return keras.Sequential(
        [
            layers.RandomFlip(
                mode="horizontal",
                seed=config.random_seed,
                input_shape=(config.img_height, config.img_width, config.num_channels),
            ),
            layers.RandomRotation(factor=0.05, seed=config.random_seed),
        ],
        name="data_augmentation",
    )


def _augmentation_layers(config: Config) -> list[keras.layers.Layer]:
    return [
        layers.RandomFlip(mode="horizontal", seed=config.random_seed),
        layers.RandomRotation(factor=0.08, seed=config.random_seed),
        layers.RandomZoom(height_factor=(-0.1, 0.1), width_factor=(-0.1, 0.1), seed=config.random_seed),
        layers.RandomContrast(factor=0.1, seed=config.random_seed),
    ]


def build_v1_model(config: Config) -> keras.Model:
    """Original notebook CNN (Flatten, no GAP) — matches the v1 checkpoint."""
    data_augmentation = build_data_augmentation(config)
    l2 = regularizers.l2(config.l2_reg)

    model = Sequential(
        [
            data_augmentation,
            layers.Rescaling(1.0 / 255),
            layers.Conv2D(16, 3, padding="same", activation="relu", kernel_regularizer=l2),
            layers.MaxPooling2D(),
            layers.Conv2D(32, 3, padding="same", activation="relu", kernel_regularizer=l2),
            layers.MaxPooling2D(),
            layers.Conv2D(64, 3, padding="same", activation="relu", kernel_regularizer=l2),
            layers.MaxPooling2D(),
            layers.Dropout(config.dropout_rate),
            layers.Flatten(),
            layers.Dense(128, activation="relu"),
            layers.Dense(1, activation=None, name="outputs"),
        ],
        name="fracture_cnn",
    )
    _compile_model(model, config.learning_rate)
    return model


def build_cnn_model(config: Config) -> keras.Model:
    """Custom CNN with stronger regularization (GAP instead of Flatten)."""
    l2 = regularizers.l2(config.l2_reg)
    augmentation = keras.Sequential(
        _augmentation_layers(config)
        + [
            layers.Rescaling(1.0 / 255, input_shape=(config.img_height, config.img_width, config.num_channels)),
        ],
        name="data_augmentation",
    )

    model = Sequential(
        [
            augmentation,
            layers.Conv2D(16, 3, padding="same", activation="relu", kernel_regularizer=l2),
            layers.MaxPooling2D(),
            layers.Conv2D(32, 3, padding="same", activation="relu", kernel_regularizer=l2),
            layers.MaxPooling2D(),
            layers.Conv2D(64, 3, padding="same", activation="relu", kernel_regularizer=l2),
            layers.MaxPooling2D(),
            layers.Dropout(config.dropout_rate),
            layers.GlobalAveragePooling2D(),
            layers.Dense(128, activation="relu", kernel_regularizer=l2),
            layers.Dropout(config.dropout_rate),
            layers.Dense(1, activation=None, name="outputs"),
        ],
        name="fracture_cnn",
    )
    _compile_model(model, config.learning_rate)
    return model


def build_transfer_model(config: Config) -> keras.Model:
    """EfficientNetB0 transfer-learning model for improved generalization."""
    weights = "imagenet"
    try:
        EfficientNetB0(include_top=False, weights=weights, input_shape=(224, 224, 3))
    except Exception:
        print("Warning: could not download ImageNet weights; using random initialization.")
        weights = None

    inputs = keras.Input(
        shape=(config.img_height, config.img_width, config.num_channels),
        name="xray_input",
    )

    x = layers.Rescaling(1.0 / 255)(inputs)
    for layer in _augmentation_layers(config):
        x = layer(x)
    x = layers.Concatenate(name="grayscale_to_rgb")([x, x, x])

    base = EfficientNetB0(
        include_top=False,
        weights=weights,
        input_shape=(config.img_height, config.img_width, 3),
        name=TRANSFER_BASE_NAME,
    )
    base.trainable = False
    x = base(x, training=False)
    x = layers.GlobalAveragePooling2D()(x)
    x = layers.Dropout(config.dropout_rate)(x)
    x = layers.Dense(128, activation="relu")(x)
    x = layers.Dropout(config.dropout_rate)(x)
    outputs = layers.Dense(1, activation=None, name="outputs")(x)

    model = keras.Model(inputs, outputs, name="fracture_efficientnet")
    _compile_model(model, config.learning_rate)
    return model


def _compile_model(model: keras.Model, learning_rate: float) -> None:
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=learning_rate),
        loss=keras.losses.BinaryCrossentropy(from_logits=True),
        metrics=["accuracy"],
    )


def build_model(config: Config) -> keras.Model:
    if config.model_type == "v1":
        return build_v1_model(config)
    if config.model_type == "transfer":
        return build_transfer_model(config)
    if config.model_type == "cnn":
        return build_cnn_model(config)
    raise ValueError(f"Unknown model_type: {config.model_type!r}. Use 'v1', 'cnn', or 'transfer'.")


def fine_tune_model(model: keras.Model, config: Config) -> None:
    """Unfreeze the top layers of the transfer-learning backbone."""
    base = model.get_layer(TRANSFER_BASE_NAME)
    base.trainable = True
    for layer in base.layers[:- config.fine_tune_layers]:
        layer.trainable = False
    _compile_model(model, config.fine_tune_learning_rate)


def get_callbacks(config: Config) -> list:
    """Training callbacks — v1 uses val_accuracy checkpointing like the notebook."""
    config.ensure_dirs()
    checkpoint_path = str(config.checkpoint_path)

    if config.model_type == "v1":
        return [
            EarlyStopping(
                monitor="val_loss",
                min_delta=0,
                patience=10,
                mode="auto",
                restore_best_weights=True,
            ),
            ModelCheckpoint(
                checkpoint_path,
                monitor="val_accuracy",
                verbose=1,
                save_best_only=True,
                save_weights_only=True,
                mode="max",
            ),
            ReduceLROnPlateau(monitor="val_loss", factor=0.2, patience=5),
        ]

    return [
        EarlyStopping(
            monitor="val_loss",
            min_delta=0,
            patience=7,
            mode="min",
            restore_best_weights=True,
        ),
        ModelCheckpoint(
            checkpoint_path,
            monitor="val_loss",
            verbose=1,
            save_best_only=True,
            save_weights_only=True,
            mode="min",
        ),
        ReduceLROnPlateau(monitor="val_loss", factor=0.2, patience=3, min_lr=1e-6),
    ]


def load_model(checkpoint: Path, config: "Config | None" = None) -> keras.Model:
    """Load a full .keras checkpoint or weights into the configured architecture."""
    if not checkpoint.is_file():
        raise FileNotFoundError(f"Checkpoint not found: {checkpoint}")

    if checkpoint.suffix == ".keras":
        return keras.models.load_model(str(checkpoint))

    if config is None:
        from src.config import get_config

        config = get_config()
    model = build_model(config)
    model.load_weights(str(checkpoint))
    return model
