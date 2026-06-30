# Project Specification

## Central Question

**Can AI-assisted medical imaging help expand access to diagnostic healthcare in underserved communities?**

## Project Summary

This project trains a convolutional neural network (CNN) to detect bone fractures in X-ray images. It serves as a concrete example of how AI can support earlier diagnosis and improve healthcare access, framed for a GHLC presentation on global health equity.

## Extension Research Question

> How could AI-assisted fracture detection be deployed in low-resource healthcare settings?

Investigate: mobile X-ray systems, cloud-based diagnosis, edge AI models, and hub-and-spoke radiology workflows. Document findings in [`DEPLOYMENT_RESEARCH.md`](DEPLOYMENT_RESEARCH.md).

## Goals

1. Train and evaluate a CNN fracture classifier on X-ray images.
2. Present results in accessible language tied to global health access.
3. Analyze deployment options for underserved communities.
4. Discuss limitations and responsible AI openly.

## Success Criteria

| Criterion | Target |
|-----------|--------|
| Model trained and evaluated | Metrics documented in MODEL_SPEC |
| Presentation | 8 minutes, clear global health thesis |
| Deployment analysis | 2–3 pages in DEPLOYMENT_RESEARCH |
| Repository | Self-contained: specs, code, notebook, presentation materials |

## Scope

- Binary fracture detection (fracture / no fracture) on X-ray images
- Educational demonstration and research documentation
- Deployment feasibility analysis for low-resource settings

## Non-Goals (Explicit)

- This is **not** a clinical diagnostic product.
- No FDA/regulatory clearance claims.
- No deployment to real patients without qualified clinical oversight.
- No collection of new patient data without proper ethics approval.

## Timeline (3–4 Weeks)

| Week | Milestone |
|------|-----------|
| 1 | Scaffold repo; integrate notebook; fill MODEL_SPEC and DATA_SPEC |
| 2 | Deployment research draft; presentation outline |
| 3 | Presentation visuals; optional metric polish |
| 4 | Rehearsal; finalize docs and README |

## Stakeholders

- GHLC presentation audience (global health + science)
- Future reviewers of this educational research project

## Related Documents

- [`MODEL_SPEC.md`](MODEL_SPEC.md)
- [`DATA_SPEC.md`](DATA_SPEC.md)
- [`PRESENTATION_SPEC.md`](PRESENTATION_SPEC.md)
- [`DEPLOYMENT_RESEARCH.md`](DEPLOYMENT_RESEARCH.md)
