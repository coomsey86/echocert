# EchoCert FAQ

## What is EchoCert?

EchoCert is a **local-first digital evidence integrity system** for files, photos, video and recorded AI-assisted work.

It uses SHA-256 hashing, structured receipts and human-readable reports to help users preserve an original digital record and later verify whether the checked file still matches the recorded digest.

---

## Is EchoCert only an AI / LLM audit tool?

No.

EchoCert began with prompt/output receipts and drift comparison, and that remains a supported use case. The wider product now includes a Windows desktop evidence workflow and an Android field-capture companion.

AI auditing is one EchoCert use case rather than the whole product identity.

---

## What are EchoCert Elite and EchoCert Mobile?

**EchoCert Elite** is the Windows desktop professional workflow for hashing, receipts, verification, reports, evidence packs and case/project handling.

**EchoCert Mobile** is the Android companion being developed for field capture and verification. Its core photo/video capture → receipt → re-hash workflow has been demonstrated on a physical Android device.

The public GitHub repository does not contain the complete private commercial builds.

---

## What does a matching SHA-256 hash tell me?

If the same file bytes produce the same SHA-256 digest as the digest recorded earlier, that strongly supports that the checked bytes are unchanged from the bytes represented by the recorded digest.

A hash does not, by itself, prove who created the file, why it was created, whether its contents are true, or whether the timestamp is independently trusted.

---

## Does EchoCert prove a photo or video is genuine?

Not by itself.

EchoCert can help prove integrity of the checked digital file. It does not automatically prove that the scene shown is real, that the file was not staged before capture, or who operated the device.

---

## Does EchoCert prove legal ownership or authorship?

No.

EchoCert can support an evidence record but does not decide legal authorship, ownership or intellectual-property rights by itself.

---

## Does EchoCert provide a trusted timestamp?

Not automatically.

Where only the local device/system clock is used, EchoCert should disclose that clearly. A stronger independently trusted time claim requires an appropriate external timestamp authority or other trusted provenance mechanism.

---

## Does EchoCert establish a complete chain of custody?

Not by itself.

It can form part of a chain-of-custody process by recording integrity, metadata and verification events. A complete chain of custody also depends on people, procedures, access control, storage and documentation around the evidence.

---

## Is EchoCert court-approved, regulator-approved or forensically accredited?

No such claim is currently made.

EchoCert is being developed and tested as an evidence-integrity tool. Any future accreditation, certification or regulatory status would need to be independently obtained and stated precisely.

---

## Does EchoCert inspect model internals or judge AI truth/safety?

No.

For AI workflows, EchoCert works with the prompt, output and associated records. It does not inspect private model internals, determine whether an AI answer is true, or perform alignment/safety scoring.

---

## Does EchoCert require the cloud?

The core product direction is **local-first**. Core evidence creation and verification should not depend unnecessarily on a cloud service.

Future optional hosted services may be added where they genuinely improve verification, collaboration or timestamp/provenance strength, but they should not erase the local-first principle.

---

## Is this GitHub repository the full commercial product?

No.

This public repository is a source-available demonstration and documentation layer. Private commercial builds, production workflows, mobile implementation details, client material, signing infrastructure, keys and protected implementation details are not included.

See [`PRIVATE_PUBLIC_BOUNDARY.md`](PRIVATE_PUBLIC_BOUNDARY.md).

---

## Is EchoCert open source?

The public repository is currently **source-available under the Business Source License 1.1 (BSL 1.1)**. It should not be described simply as unrestricted open source.

See [`LICENSE`](LICENSE) and [`LICENSING.md`](LICENSING.md).

---

## Can I use EchoCert commercially?

Commercial or production use of the public licensed work is governed by the current BSL terms and may require a separate commercial licence.

See [`LICENSE`](LICENSE) and [`LICENSING.md`](LICENSING.md).

---

## What should never be uploaded to the public repository?

Do not upload:

- Client or pilot evidence
- Real legal evidence without proper authority and review
- Personal, health, family or financial records
- Passwords, tokens or recovery phrases
- Private keys, certificates or signing material
- Production-only workflows
- Protected commercial implementation details

---

## Who is EchoCert for?

Early target users include:

- Inspection and field-service professionals
- Construction / QA / condition-record workflows
- Legal support and dispute preparation
- Compliance and internal audit
- Property and insurance-support documentation
- Investigators and consultants
- Researchers
- AI governance and AI-assisted workflow users

See [`WHO_BUYS_ECHOCERT.md`](WHO_BUYS_ECHOCERT.md).
