# Literature Review — Operation Ghost Ledger

**Course:** Advanced Digital Forensics / ISS 7133
**Prepared by:** Kum Jude Wung

## 1. Introduction

This review surveys the standards, frameworks and prior work that inform
the methodology used to investigate *Operation Ghost Ledger* — a case
that requires the examiner to authenticate leaked digital evidence,
forensically image and analyse seized hardware, and defend the resulting
conclusions against a claim that the evidence was AI-fabricated. The
literature falls into five areas: digital evidence lifecycle and legal
foundations; forensic imaging and cryptographic integrity; multi-domain
analysis techniques; evidentiary admissibility standards; and cognitive
bias in forensic examination.

## 2. Digital evidence lifecycle and legal foundations

Digital evidence must be handled according to a defined lifecycle —
identification, collection, preservation, examination, analysis and
presentation — to remain legally usable. The course's IPC-EAR framework
(Identify, Preserve, Collect, Examine, Analyse, Report) formalises this
sequence and is applied directly to both evidence packages in this case
(*Class 2 — Digital Evidence Types, Lifecycle & Legal Foundations*,
~pp. 74–100).

A key distinction in the literature — and in this case — is between
**found evidence** and **seized evidence**. Found evidence (Package A, the
public leak) carries no chain of custody and must be independently
authenticated before it can be relied upon. Seized evidence (Package B,
obtained under warrant) requires an unbroken chain of custody from the
point of seizure onward, and the legal authority for its collection must
be scoped correctly under statutes such as the Computer Fraud and Abuse
Act (CFAA) and the Electronic Communications Privacy Act (ECPA) — the
distinction between a warrant and a subpoena determines what can lawfully
be collected and analysed (*Class 2*, Capstone Integration section,
~pp. 230–257).

## 3. Forensic imaging and cryptographic hashing

Forensically sound acquisition depends on two principles established in
the literature: **non-alteration** of the source (via write-blocking
hardware/software) and **verifiable integrity** (via cryptographic
hashing). SHA-256 hashing of both the source media and the resulting
image allows any subsequent alteration to be detected, and is the
standard applied to Okafor's laptop image in this case. The NSRL
(National Software Reference Library) known-file filtering technique is
used to exclude standard operating-system and application files from
analysis, focusing examiner attention on user-created and anomalous files
(*Class 3 — Forensic Imaging and Cryptographic Hashing*, throughout;
Capstone Integration quiz, ~pp. 250–255).

Industry guidance — NIST SP 800-86 (*Guide to Integrating Forensic
Techniques into Incident Response*) and NIST SP 800-101 (*Guidelines on
Mobile Device Forensics*) — anchors these acquisition procedures, and is
cited directly as the methodological basis for this capstone's imaging
and mobile-analysis work.

## 4. Multi-domain forensic analysis

Because the evidence spans a laptop image, a memory capture, a network
packet capture, mobile backups and cloud logs, the investigation draws on
literature and tooling from several forensic sub-disciplines:

- **Filesystem forensics** — $MFT parsing, registry analysis and
  timeline reconstruction (tooling: Autopsy / The Sleuth Kit) to recover
  deleted files, user activity and Shellbag evidence of file access.
- **Memory forensics** — process, network-connection and hidden-artifact
  analysis using the Volatility framework, used here to look for
  execution evidence of AI-manipulation tooling.
- **Network forensics** — reconstruction of sessions from a packet
  capture (tooling: Wireshark), correlated against host-based artifacts
  to establish external communications.
- **Mobile and cloud forensics** — SQLite backup analysis (messaging,
  GPS/location, call logs) and JSON access-log correlation for
  cloud-portal activity.
- **Anti-forensics detection** — identification of wiping, steganography
  and other concealment techniques, using pattern-based detection tools
  such as YARA.

A recurring theme across this literature is that no single domain is
sufficient on its own: findings must be **correlated** across domains and
independent timestamp sources to be reliable (*Class 1*, Phase 3–4
walkthrough, pp. 22–27).

## 5. Detecting AI-manipulated evidence

The defence's central claim — that the audio, PDF and spreadsheet are
AI-generated or altered — places this case within an emerging area of
forensic literature: authentication of media in the presence of
generative AI. Relevant techniques include:

- **Audio forensics** — spectrogram and structural analysis to detect
  splicing points, unnatural spectral artifacts consistent with voice
  synthesis, or edit discontinuities at a specific timestamp.
- **Document forensics** — inspection of PDF object structure, embedded
  JavaScript, and metadata (creation/modification dates, authoring tool
  signatures) for inconsistencies indicating backdating or tampering.
- **File and metadata forensics** — EXIF/XMP extraction and cross-version
  comparison to establish whether a file's creation history is consistent
  with its claimed provenance.

This is an actively developing field precisely because generative AI
tools are becoming more capable and more accessible, which is why the
methodology in this capstone treats "AI manipulation" as a testable
hypothesis rather than an assumption in either direction.

## 6. Evidentiary admissibility standards

For forensic conclusions to be usable in court, the underlying methods
must satisfy recognised admissibility standards. The literature commonly
cites the **Daubert standard**, which evaluates expert evidence against
five factors: testability, peer review, known error rate, existence of
standards, and general acceptance in the relevant scientific community.
Alongside Daubert, the **SWGDE** (Scientific Working Group on Digital
Evidence) publishes best-practice guides that this capstone's tooling and
procedure selections are anchored to, ensuring the methodology — not just
the conclusion — can withstand scrutiny.

## 7. Cognitive bias in forensic examination

A significant body of forensic-science literature addresses the risk that
an examiner's conclusions are shaped by extraneous, non-evidentiary
information — a problem well documented in fields such as fingerprint and
DNA analysis, and directly applicable here given the high-profile,
politically charged nature of the case. Four risks are consistently
identified and countered in this capstone's methodology:

| Risk | Countermeasure (from the literature) |
|---|---|
| Confirmation bias | Blind or independent analysis; actively testing contradictory explanations |
| Context/expectation bias | Separating case context from technical examination |
| Anchoring | Avoiding construction of the timeline around a single initial timestamp |
| Overconfidence | Explicitly stating uncertainty, limitations and confidence levels |

## 8. Gaps this capstone addresses

Existing course material provides the individual techniques (imaging,
hashing, memory/network/mobile analysis, legal frameworks) but does not,
on its own, walk through a case where the central dispute is over whether
the evidence itself is authentic versus AI-fabricated. This capstone
integrates those individual techniques into a single hypothesis-driven
investigation — treating authenticity itself as the object of forensic
analysis, not just a precondition for it.

## 9. References / course source

- Digital Forensics Fundamentals — ISS 7133 course PDF (capstone
  walkthrough, pp. 16–27, 236–238)
- Digital Evidence Types, Lifecycle & Legal Foundations — ISS 7133 course
  PDF (IPC-EAR framework, ~pp. 74–100; Capstone Integration, ~pp. 230–257)
- Forensic Imaging and Cryptographic Hashing — ISS 7133 course PDF
  (Capstone Integration, ~pp. 250–255)
- NIST SP 800-86, *Guide to Integrating Forensic Techniques into Incident
  Response*
- NIST SP 800-101, *Guidelines on Mobile Device Forensics*
- SWGDE digital evidence best-practice documents
- Tools referenced throughout: Autopsy, The Sleuth Kit, Volatility,
  Wireshark, FTK Imager, ExifTool, YARA
