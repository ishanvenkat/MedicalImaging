# Slides Build Guide

Build slides from the official GHLC template and this project's outline. Export optional PDFs to `docs/presentation/assets/`.

## Mandatory Template

**You must use the 2026 GHLC Student Speaker Series slide template.**

| Item | Location |
|------|----------|
| Official guidelines | [`sources/GHLC_Presentation_Guidelines.pdf`](sources/GHLC_Presentation_Guidelines.pdf) |
| Slide Template A | [`sources/2026 Student Speaker Series Slide Template A.pdf`](sources/2026%20Student%20Speaker%20Series%20Slide%20Template%20A.pdf) |

**Important:** Copy the template to a Google Drive or local folder **you own** before editing. Copying inside the shared GHLC folder can fail.

Template bookend slides (do not remove or reorder):

1. Title — title, name, school, **recording date**
2. Introduction — self-intro (~1 min)
3. *(Insert all content slides here)*
4. References
5. Acknowledgements
6. Thank You
7. Contact — name, email, LinkedIn only (**no social media**)

## Slide-by-Slide Build Order

Content slides insert between Introduction and References.

| Slide # | Title | Content source | Assets needed |
|---------|-------|----------------|---------------|
| 1 | Title | `outline.md` Slide 1 | None — fill name, school, recording date |
| 2 | Introduction | `outline.md` Section 1 | Optional photo |
| 3 | Global Health Challenge | `outline.md` Slide 3 | World map / access infographic |
| 4 | Consequences | `outline.md` Slide 4 | Icon list |
| 5 | AI as a Bridge | `outline.md` Slide 5 | Simple bridge diagram |
| 6 | Imaging Modalities | `outline.md` Slide 6 | 4-modality icons |
| 7 | Why Imaging Matters | `outline.md` Slide 7 | 3-bullet list |
| 8 | Fracture Problem | `outline.md` Slide 8 | X-ray icon |
| 9 | My Approach | `outline.md` Slide 9 | Simple pipeline diagram |
| 10 | Results | `outline.md` Slide 10 | `training_curve.png`, `confusion_matrix.png` — **84.4% test acc, 94.1% sensitivity, 75.6% specificity** |
| 11 | Limitations | `outline.md` Slide 11 | Bullet list — keep visible |
| 12 | Future Applications | `outline.md` Slide 12 | Icon grid (TB, pneumonia, etc.) |
| 13 | AI Augments Doctors | `outline.md` Slide 13 | 3-bullet list |
| 14 | Responsible AI | `outline.md` Slide 14 | Question list |
| 15 | Deployment | `DEPLOYMENT_RESEARCH.md` | Mermaid diagram export |
| 16 | Key Takeaways | `outline.md` Slide 16 | Call to action / reflection |
| 17 | References | `bibliography.md` | Full citation list |
| 18 | Acknowledgements | `outline.md` Slide 18 | Names and organizations |
| 19 | Thank You | Template default | — |
| 20 | Contact | Template default | Email, LinkedIn |

## Visual Design Tips

- Maximum 5 bullet points per slide
- Use images over text where possible (especially for imaging modalities)
- Show one chart per results slide — not a data dump
- Limitations slide: use a distinct color or icon so it stands out
- Cite image and figure sources on the References slide

## Deployment Diagram

Export the mermaid diagram from `docs/specifications/DEPLOYMENT_RESEARCH.md` using:

- [Mermaid Live Editor](https://mermaid.live) → export PNG
- Or redraw simplified version in Slides

Save as `docs/presentation/assets/deployment_diagram.png`

## Recording Checklist (GHLC Submission)

- [ ] Slides built from official Template A
- [ ] Title slide includes recording date
- [ ] References slide complete (including image credits)
- [ ] Acknowledgements and Contact slides filled in
- [ ] No social media on Contact slide
- [ ] Record in Zoom with **camera and microphone on**
- [ ] Formal attire; professional, quiet background
- [ ] Full run-through with timer — target 7:45–8:00 spoken
- [ ] Upload to Google Drive: `LastName_FirstName_TITLE_OF_PRESENTATION`
- [ ] Share link with **editor access**
- [ ] Submit via [application form](https://forms.gle/Wx7L1WS59DECbtAV8) before **July 20, 2026, 11:59 PM ET**
- [ ] Recording walkthrough: [YouTube playlist](https://www.youtube.com/playlist?list=PLD4D2lXEsA-WC-xvwD8DEXiUi_k657eZz)

## Rehearsal Checklist

- [ ] Record yourself once; listen for filler words and jargon
- [ ] Peer review #1: "Did you understand the global health argument?"
- [ ] Peer review #2: "Was any ML jargon confusing?"
- [ ] Verify all statistics against reputable sources
- [ ] Practice limitations segment until it feels natural (not rushed)
- [ ] Prepare 1–2 answers for Q&A:
  - "Would you trust this model in a real hospital?" → No, needs clinical validation
  - "Why fractures?" → Accessible dataset, clear global health link, X-rays widely used

## Cut List (if over 8 minutes)

1. Combine Slides 6–7 into one (imaging overview)
2. Shorten Slide 12 to verbal mention only
3. Never cut Slides 11 or 14 (limitations and responsible AI)
4. Never cut References, Acknowledgements, or Contact slides

## Post-Recording

- Save final slides PDF to `docs/presentation/assets/slides_final.pdf` (optional)
- Update MODEL_SPEC with any Q&A insights
- Note audience questions in a brief `docs/presentation/feedback.md` (optional)
