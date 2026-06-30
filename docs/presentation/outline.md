# Presentation Outline — 8 Minutes

**Title:** AI-Assisted Medical Imaging: A Path Toward Global Health Equity

**Central question:** Can AI-assisted medical imaging help expand access to diagnostic healthcare in underserved communities?

**Template:** Use [`sources/2026 Student Speaker Series Slide Template A.pdf`](sources/2026%20Student%20Speaker%20Series%20Slide%20Template%20A.pdf). Insert content slides 3–16 below **between** the Introduction slide and the References slide.

---

## Slide 1 — Title (Template slide 1) (~0:00–0:15)

Required fields per GHLC:

- Presentation title
- Your name
- Current school / institution
- **Date of recording** (not presentation day at conference — the date you record the video)

Optional subtitle on slide or in speech: Fracture detection as one example of AI-supported access

---

## Section 1: Self-Introduction (0:15–1:15) — ~1 min

### Slide 2 — Introduction (Template slide 2)

Required verbal content per GHLC:

- What grade you are in
- Where you are from (hometown / region)
- What school you attend
- Extracurricular activities you are involved in
- Interests and future plans (professional bio)
- Hook: fracture detection project and interest in global health equity

**Transition:** "To understand why this matters, we need to start with the problem."

---

## Section 2: Background / Introduction to Topic (1:15–3:15) — ~2 min

Clearly express **why this is a global health topic**, why it matters, and any background the audience needs.

### Slide 3 — The Global Health Challenge

- Many communities lack radiologists and imaging specialists
- Rural areas, low-resource regions, underserved populations
- Limited access to X-ray, CT, MRI infrastructure

### Slide 4 — Consequences

- Delayed diagnosis
- Worse treatment outcomes
- Higher mortality and disability
- Example: untreated fractures → chronic pain, improper healing

### Slide 5 — AI as a Bridge

- Recent advances in AI may help close some gaps
- Not by replacing doctors — by extending their reach
- Triage, prioritization, and decision support

**Transition:** "Let me explain what medical imaging is and then show you my project."

---

## Section 3: Body (3:15–6:00) — ~2–3 min

Present what you promised in the introduction. For your own work, clearly explain **what you did**, with evidence and figures.

### Part 1 — What Is Medical Imaging? (~1 min)

#### Slide 6 — Modalities

| Modality | Primary uses |
|----------|--------------|
| X-ray | Bones, chest, fast screening |
| CT | Detailed cross-sections |
| MRI | Soft tissue, brain, joints |
| Ultrasound | Real-time, pregnancy, cardiac |

#### Slide 7 — Why Imaging Matters

- Diagnosis
- Treatment planning
- Monitoring disease over time

### Part 2 — Fracture Detection Project (~1–1.5 min)

#### Slide 8 — The Problem

- Fractures need timely X-ray interpretation
- Delays common where radiologists are scarce

#### Slide 9 — My Approach

- Trained a CNN on **~8,700 X-ray images** (`data/train/`), with a **500-image held-out test set** (`data/test/`)
- During training: 80/20 train/validation split (~6,980 train / ~1,745 validation, seed=123)
- Grayscale images at 1560×1170; binary classification: fractured vs. not fractured
- Final model: data augmentation + 3 convolutional layers + L2 regularization + dropout
- Pattern recognition — learns visual features associated with fractures

#### Slide 10 — Results

- Best validation accuracy: **95.9%** during training (15 epochs)
- **Independent test set** (500 images): **84.4%** accuracy, **94.1%** sensitivity, **75.6%** specificity
- Confusion matrix: 224 fractures detected, 14 missed; 64 healthy images flagged incorrectly
- Confusion matrix: `docs/presentation/assets/confusion_matrix.png`
- Training curve: `docs/presentation/assets/training_curve.png`
- Larger dataset than the original 90-image Colab set, but provenance and clinical validation remain limited

#### Slide 11 — Limitations (Differentiator)

- Dataset may not represent all populations, body regions, or scanner types
- False positives (64 on test set) → unnecessary anxiety and referrals
- False negatives (14 on test set) → missed fractures, dangerous if trusted blindly
- Research prototype — not clinically validated; educational use only

### Part 3 — Future Applications (~0.5 min)

#### Slide 12 — Same Technology, Many Diseases

- Tuberculosis (chest X-ray)
- Pneumonia
- Breast cancer screening
- Diabetic retinopathy
- Bone fractures (your project)

**Transition:** "So what does this mean for the future of healthcare access?"

---

## Section 4: Conclusion (6:00–8:00) — ~2 min

Restate topic and purpose. Summarize key takeaways. Include concluding thoughts and a call to action or thought-provoking question.

### Slide 13 — AI Augments, Not Replaces

- AI can prioritize urgent cases
- Support — not substitute — clinical judgment
- Expand access where specialists are scarce

### Slide 14 — Responsible AI

- Who gets access to these tools?
- How do we validate across diverse populations?
- Could AI worsen disparities if only wealthy hospitals adopt it?

### Slide 15 — Deployment Extension

- Explored: mobile X-ray + edge AI, cloud triage, hub-and-spoke
- Most realistic: portable imaging + AI-assisted prioritization at district hospitals
- Reference deployment diagram from DEPLOYMENT_RESEARCH.md

### Slide 16 — Key Takeaways / Personal Reflection

- Restate central question and answer in one sentence
- Learned how computational tools assist medical decision-making
- Inspired to explore AI and medical imaging for more equitable healthcare
- **Call to action or thought-provoking question**, e.g.: "How can we ensure AI imaging tools reach the communities that need them most?"

---

## Slide 17 — References (Template slide — mandatory)

Cite all sources used, including images and figures. Pull from [`../references/bibliography.md`](../references/bibliography.md).

Minimum citations to include:

- WHO workforce / global health reports (statistics cited in background)
- Rajpurkar et al. or Litjens et al. (AI medical imaging context)
- WHO AI ethics and governance (responsible AI section)
- Fracture dataset source
- Image/figure credits for charts, maps, and icons

---

## Slide 18 — Acknowledgements (Template slide — mandatory)

Thank individuals and organizations who contributed, for example:

- Mentors, teachers, or advisors
- GHLC program and Johns Hopkins
- Dataset providers
- Peer reviewers who gave feedback on the presentation
- Thank the audience for listening

---

## Slide 19 — Thank You (Template slide — mandatory)

Use template default or minimal customization.

---

## Slide 20 — Contact (Template slide — mandatory)

- Your name
- Email (professional)
- LinkedIn (optional)
- **Do not include social media handles**

---

## Timing Cheat Sheet

| Section | Target end time |
|---------|-----------------|
| Title + intro done | 1:15 |
| Background done | 3:15 |
| Body done | ~6:00 |
| Conclusion done | 8:00 |
| References / Ack / Contact | After 8:00 (display only, or brief closing) |

## If Running Over

Cut in this order:

1. Shorten Slides 6–7 (imaging overview) by 30 sec
2. Reduce future applications to one sentence
3. Keep limitations and responsible AI — these are your differentiator

Never remove References, Acknowledgements, or Contact slides.
