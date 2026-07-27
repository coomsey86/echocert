# EchoCert Public Roadmap

This roadmap reflects the current public-safe product direction without exposing private commercial implementation details.

---

## Phase 1 — Public integrity prototype

Status: **Complete / demonstrated**

- Deterministic receipt generation
- SHA-256 integrity verification
- Prompt/output record support
- Diff reports
- HTML audit reports
- Demo scripts
- Public documentation
- Public/private boundary guidance

The original AI-audit workflow remains a valid EchoCert use case and technical foundation.

---

## Phase 2 — EchoCert Elite desktop

Status: **Controlled-pilot ready**

The private Windows build, **EchoCert Elite v0.9.4**, has demonstrated:

- SHA-256 file hashing
- JSON receipts
- PDF and TXT reports
- Evidence Pack ZIP creation
- Receipt/file verification
- Case and project metadata
- Local document storage
- UTC/local timestamp recording
- Timezone / UTC-offset recording
- Clock-source and timestamp-status disclosure
- Windows installer
- Clean-machine installation and verification testing

Current focus:

- Controlled pilot feedback
- Security hardening
- UX refinement
- Failure-case testing
- Documentation and support flow

---

## Phase 3 — EchoCert Mobile companion

Status: **Physical-device core workflow demonstrated**

A private Android development build has demonstrated on a physical Samsung device:

- Photo capture
- Video capture
- Preservation of captured originals in local evidence storage
- Automatic SHA-256 receipt creation
- One-tap re-hash verification
- Clear integrity-confirmed results when the later file matches

Current focus:

- Simplify the workflow further
- Harden file handling and permissions
- Improve receipt browsing and verification UX
- Improve desktop/mobile compatibility
- Expand safe import/capture workflows only after the core path is robust

---

## Phase 4 — Pilot validation and interoperability

Status: **Next**

- Real-world pilot users
- Legal/compliance/inspection feedback
- Structured usability testing
- Security review and threat modelling
- Better handling of edge cases and corrupted/missing files
- Clearer export and transfer workflow between mobile and desktop
- Standards-first format support
- Evaluate trusted timestamp options
- Evaluate C2PA / Content Credentials interoperability where appropriate

The aim is to strengthen evidence quality without making claims that the technology cannot support.

---

## Phase 5 — Business and team workflow

Status: **Planned**

Potential directions include:

- Organisation-level templates
- Team review workflows
- Branded evidence reports
- Internal governance records
- Multi-user case handling
- Audit-ready exports
- Role-based access where required
- Hosted verification services where they add real value

These features should follow successful pilot validation rather than precede it.

---

## Phase 6 — Integration layer

Status: **Future / conditional on demand**

Potential directions include:

- API access
- Digital signature support
- Trusted timestamp integration
- Receipt chains / linked evidence records
- Compliance exports
- Integration with governance and case-management workflows
- C2PA / Content Credentials interoperability

No future item should be treated as committed until technical need, security and user demand justify it.

---

## What will stay private

The public roadmap will not expose:

- Client or pilot evidence
- Private commercial logic
- Production-only workflows
- Private signing infrastructure
- Keys, certificates, tokens or secrets
- Sensitive legal, personal, health or financial data
- Protected implementation details that are unnecessary to explain the product

See [`PRIVATE_PUBLIC_BOUNDARY.md`](PRIVATE_PUBLIC_BOUNDARY.md).

---

## Goal

Build a practical, local-first digital evidence integrity ecosystem that normal users can understand quickly while giving professional users robust verification and reporting underneath.

**Capture or select → preserve → hash → receipt → verify → report.**
