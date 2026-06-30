# Speaker Notes — ~960 Words Target (Spoken Sections)

Read at ~120 words/minute. Practice with a timer. References, Acknowledgements, and Contact slides are shown after the 8-minute mark (or with a brief closing line).

---

## [0:00] Title (~30 words)

"Good [morning/afternoon]. My name is [Name], and I'm a [grade] student at [School]. Today I want to explore one question: Can artificial intelligence help expand access to medical imaging for communities that don't have enough radiologists or diagnostic infrastructure? I'll use a fracture detection project I built as one example — but the bigger story is about global health equity."

---

## [0:15] Self-Introduction (~120 words)

"I'm from [hometown/region]. Outside of school, I'm involved in [extracurricular 1] and [extracurricular 2]. I'm especially interested in [biomedical engineering / computational biology / healthcare technology] and hope to [future plan — e.g., study biomedical engineering and work on tools that improve healthcare access].

Over the past months, I've been learning how machine learning can analyze medical images — specifically, X-rays of bone fractures. I became interested in this because imaging is one of the most powerful tools in modern medicine, yet millions of people worldwide cannot access it when they need it. My project is a small step toward understanding how AI might help — not as a replacement for doctors, but as a tool that extends what clinicians can do in places where specialists are scarce."

---

## [1:15] Background — The Problem (~240 words)

"Let's start with the problem. Medical imaging — X-rays, CT scans, MRIs — is essential for diagnosing fractures, infections, cancers, and countless other conditions. But imaging is only useful if someone trained can interpret it.

Around the world, there is a severe shortage of radiologists and imaging specialists. The World Health Organization has documented that this gap is especially acute in rural communities, low-income countries, and underserved urban populations. In many regions, a patient with a suspected fracture may wait days or weeks for an X-ray to be read — if they can get an X-ray at all.

The consequences are serious. Delayed diagnosis means delayed treatment. A fracture that goes unnoticed can heal improperly, causing chronic pain and disability. Chest infections go untreated. Cancers are caught too late.

This isn't just a technical problem — it's an equity problem. Where you live shouldn't determine whether you get a timely diagnosis.

Recently, advances in artificial intelligence have opened a new possibility: computer systems that can learn to recognize patterns in medical images. The question is whether this technology can help bridge the access gap — responsibly."

---

## [3:15] Body Part 1 — Medical Imaging (~120 words)

"Medical imaging uses different technologies to see inside the body. X-rays are fast and widely used for bones and chest conditions. CT scans provide detailed cross-sectional images. MRI excels at soft tissue. Ultrasound is portable and real-time.

These tools support three critical functions: diagnosis, treatment planning, and monitoring over time. Without them, clinicians are essentially working with limited information.

The same AI techniques that analyze X-rays for fractures can be applied to many other imaging tasks — which is why one project can illustrate a much broader opportunity."

---

## [4:15] Body Part 2 — My Project (~200 words)

"For my project, I trained a convolutional neural network — a type of AI model designed for image recognition — on roughly eighty-seven hundred X-ray images, with a separate five-hundred-image test set held out for final evaluation. During training, I used an eighty-twenty split for training and validation. The images are grayscale, about fifteen hundred by eleven hundred pixels. The model uses three convolutional layers with data augmentation and regularization to reduce overfitting.

During training, the best validation accuracy reached about ninety-six percent. On the independent test set — images the model had never seen — I measured eighty-four percent accuracy, with ninety-four percent sensitivity for detecting fractures. That means it caught two hundred twenty-four of two hundred thirty-eight fractured cases. Specificity was about seventy-six percent, meaning it correctly identified one hundred ninety-eight of two hundred sixty-two healthy images, but flagged sixty-four healthy images as fractured.

But I want to be honest about limitations. While this dataset is much larger than my original ninety-image prototype, we still don't know if it represents all patient populations or imaging equipment. It will make false positives and false negatives. It has not been clinically validated and cannot be used for real medical decisions. These limitations are exactly why responsible deployment matters."

---

## [5:30] Body Part 3 — Future Applications (~60 words)

"The same underlying technology applies far beyond fractures. Researchers are using AI on chest X-rays to screen for tuberculosis and pneumonia, on mammograms for breast cancer, and on retinal images for diabetic eye disease. One technical approach — pattern recognition on medical images — can support many global health priorities."

---

## [6:15] Conclusion (~240 words)

"So where does this leave us?

AI will not replace doctors. A fracture still needs a clinician to examine the patient, decide on treatment, and set a bone. What AI can do is help prioritize cases, support diagnosis, and extend specialist expertise to places that don't have enough specialists.

But we have to ask hard questions. Who gets access to AI-assisted tools — only wealthy hospitals, or also rural clinics? How do we validate that a model works across different populations and equipment? If deployment is uneven, could AI actually worsen healthcare disparities?

After building my fracture detection model, I researched how similar systems could be deployed in low-resource settings. The most realistic approaches combine portable X-ray equipment with either on-device AI or AI-assisted triage at a district hospital — a hub-and-spoke model where technology helps sort urgent cases to the front of the queue.

Through this project, I learned that computational tools can genuinely assist medical decision-making — but only when built and deployed with humility, validation, and a commitment to equity.

I'll leave you with this question: How can we ensure AI imaging tools reach the communities that need them most, instead of only the hospitals that already have the most resources?

Thank you for listening."

---

## [After 8:00] References / Acknowledgements / Contact (display slides)

These slides are mandatory in the deck. You may advance to them after finishing the spoken conclusion, or say briefly:

"You'll find my full references and acknowledgements on the next slides. I'm happy to connect via email or LinkedIn if you have questions."

Do not include social media on the contact slide.

---

## Word Count Note

- Total spoken sections: ~1,010 words — trim imaging overview or future apps slightly if pacing runs long
- Rehearse and adjust pacing; aim to finish spoken content by 7:45–8:00
- Log timing in [`rehearsal-log.md`](rehearsal-log.md)
