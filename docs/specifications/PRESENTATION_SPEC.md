# Presentation Specification

Official GHLC source materials: [`../presentation/sources/`](../presentation/sources/)

## Title Options

1. **AI-Assisted Medical Imaging: A Path Toward Global Health Equity** (recommended)
2. Can Artificial Intelligence Expand Access to Medical Imaging Around the World?

## Program Context

| Parameter | Value |
|-----------|-------|
| Event | GHLC 2026 Student Speaker Series (SSS) |
| Duration | 8 minutes or less (spoken presentation) |
| Medium | Pre-recorded slide presentation with presenter on camera |
| Audience | GHLC — global health and science peers |
| Selection | Application video reviewed by at least two reviewers; highest-quality submissions may be published on the official GHLC YouTube channel |
| Application deadline | **July 20, 2026, 11:59 PM Eastern Time** |

## Central Thesis

Can AI-assisted medical imaging help expand access to diagnostic healthcare in underserved communities?

The fracture detection CNN is the **example**, not the entire talk. Frame it as one application of a broader technology that could support TB screening, pneumonia detection, breast cancer imaging, diabetic retinopathy, and more.

Every section must show **clear relevance to global health** — why the topic matters for populations, access, and equity.

## Mandatory Slide Template

Slides **must** use the 2026 GHLC Student Speaker Series template:

- Source PDF: [`../presentation/sources/2026 Student Speaker Series Slide Template A.pdf`](../presentation/sources/2026%20Student%20Speaker%20Series%20Slide%20Template%20A.pdf)
- Copy the template to a Google Drive or local folder **you own** before editing (shared-folder copies can fail)

### Required Slide Order

| # | Template section | GHLC requirement | This project |
|---|------------------|------------------|--------------|
| 1 | Title | Presentation title, your name, school/institution, **date of recording** | See outline Slide 1 |
| 2 | Introduction | Self-intro (~1 min): grade, where you are from, school, extracurriculars, interests/future plans | See outline Slide 2 |
| 3–N | Content | Background (~2 min), Body (~2–3 min), Conclusion (~2 min) — insert slides between intro and References | Slides 3–16 in outline |
| N+1 | References | Cite all sources, including images and figures | [`../references/bibliography.md`](../references/bibliography.md) |
| N+2 | Acknowledgements | Thank contributors (individuals and organizations) and the audience | Mentors, dataset sources, GHLC |
| N+3 | Thank You | Closing slide | Template default |
| N+4 | Contact | Name, email, LinkedIn (optional) — **no social media** | Fill before recording |

Content slides go **between** the Introduction slide and the References slide. Do not remove or reorder the mandatory bookend slides.

## Timed Structure (Spoken — 8:00 Max)

| # | Section | Time | Key Points | Visual |
|---|---------|------|------------|--------|
| 1 | Title | ~0:15 | State title and central question | Title slide (name, school, recording date) |
| 2 | Self-introduction | 1:00 | Grade; hometown/region; school; extracurriculars; interests and future plans; fracture project hook | Introduction template slide |
| 3 | Background / introduction to topic | 2:00 | Global health relevance; radiologist shortage; delayed diagnosis; why audience should care; necessary background | Access-gap infographic or world map |
| 4 | Body | 2:00–3:00 | What you did; main points with evidence; figures/images; fracture CNN project; limitations | Architecture diagram, result charts, sample X-ray |
| 5 | Conclusion | 2:00 | Restate topic and purpose; key takeaways; AI augments doctors; responsible AI; personal reflection; call to action or thought-provoking question | Closing content slides + deployment diagram |
| — | References / Acknowledgements / Contact | After speaking | Display on screen; cite during body where needed | Template end slides |

**Total spoken target: 8:00 or less**

### Body Content Breakdown (fits within 2–3 min)

| Part | Time | Content |
|------|------|---------|
| 4a | ~1:00 | What is medical imaging? X-ray, CT, MRI, ultrasound |
| 4b | ~1:00–1:30 | Fracture detection project, results, limitations |
| 4c | ~0:30 | Future applications (TB, pneumonia, breast cancer, diabetic retinopathy) |

If over time, shorten 4a first; never cut limitations or responsible AI.

## Required Differentiator Content

### Limitations (30–45 seconds)

- Dataset bias and lack of diverse training data
- False positives and false negatives
- Model not validated for clinical deployment
- Performance may not generalize to low-resource scanner settings

### Responsible AI Questions

- Who gets access to AI-assisted tools?
- How do we validate models across populations?
- Could AI worsen disparities if only wealthy hospitals adopt it?

## Accuracy and Citations

- Verify facts and statistics with multiple reputable sources before recording
- Cite any information that is not common knowledge, your own work, or your own ideas
- Include citations for **images and figures** on the References slide
- Source list: [`../references/bibliography.md`](../references/bibliography.md)

## Language Guidelines

| Use | Avoid |
|-----|-------|
| "assists screening" | "diagnoses fractures" |
| "flags images for review" | "replaces radiologists" |
| "pattern recognition" | layer-by-layer architecture details |
| "may help expand access" | "will solve healthcare inequality" |

## Recording and Submission

| Requirement | Detail |
|-------------|--------|
| Tool | Zoom recommended (free) |
| Camera / audio | **On at all times** during recording |
| Attire | Formal / professional |
| Environment | Professional background; minimal noise |
| Practice | Rehearse with feedback from peers, family, or other GHLC students |
| Drive folder name | `LastName_FirstName_TITLE_OF_PRESENTATION` |
| Drive permissions | Share link with **editor access** |
| Submission form | https://forms.gle/Wx7L1WS59DECbtAV8 |
| Recording guide | https://www.youtube.com/playlist?list=PLD4D2lXEsA-WC-xvwD8DEXiUi_k657eZz |

The submitted video is the **polished final presentation**. If selected, this recording is what uploads to the GHLC YouTube channel.

## Extension Talking Point

> "After building a fracture detection model, I explored how similar systems could be adapted for mobile X-ray units, cloud triage, or edge devices in clinics without radiologists."

Reference: [`DEPLOYMENT_RESEARCH.md`](DEPLOYMENT_RESEARCH.md)

## Visual Asset Checklist

Place in `docs/presentation/assets/`:

- [ ] Global imaging access infographic
- [ ] Medical imaging modalities diagram
- [ ] Simple CNN / pipeline diagram
- [x] Training curve
- [x] Confusion matrix
- [ ] Sample predictions (TP, FP, FN) — optional
- [ ] Deployment model comparison diagram

## Rehearsal Notes

- Target ~120 words/minute (~960 words total for spoken sections)
- If over time, shorten imaging overview (Body 4a) first
- Practice the limitations segment — it is the differentiator
- Peer review: one listener for jargon, one for global health thread
- Log runs in [`../presentation/rehearsal-log.md`](../presentation/rehearsal-log.md)

## Related Files

- [`../presentation/sources/README.md`](../presentation/sources/README.md) — official PDF sources
- [`../presentation/outline.md`](../presentation/outline.md)
- [`../presentation/speaker-notes.md`](../presentation/speaker-notes.md)
- [`../presentation/slides-guide.md`](../presentation/slides-guide.md)
