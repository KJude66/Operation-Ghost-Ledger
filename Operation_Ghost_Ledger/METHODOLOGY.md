# Methodology — Scientific Rigor, Bias Controls & Tooling

Applies across every phase of the investigation.

## Scientific quality

The investigation should be testable, reproducible and independently
reviewable. Course-identified Daubert factors:

- Testability
- Peer review
- Error rate
- Standards
- General acceptance

## Cognitive bias controls

| Risk | Countermeasure |
|---|---|
| Confirmation bias | Blind/independent analysis and actively test contradictory explanations. |
| Context/expectation bias | Separate case context from technical examination where possible. |
| Anchoring | Do not build the timeline around a single initial timestamp. |
| Overconfidence | State uncertainty, limitations and confidence; avoid absolute claims without support. |

## Tooling plan

| Area | Tool family | Purpose |
|---|---|---|
| Hashing | SHA-256 / standard hashing utilities | Integrity verification |
| Disk imaging | FTK Imager or validated equivalent | Forensic acquisition |
| Filesystem | Autopsy / The Sleuth Kit | MFT, metadata, deleted files, timeline |
| Memory | Volatility | Processes and network artifacts |
| Network | Wireshark | PCAP/session reconstruction |
| Mobile | SQLite analysis tools / appropriate forensic suite | Backups, WhatsApp, GPS, calls |
| Metadata | ExifTool / PDF structure tools | Metadata and structural examination |
| Detection | YARA | Pattern-based artifact detection |

## Legal & procedural guardrails

- **Legal authority** — confirm the right instrument (warrant vs.
  subpoena) before every seizure or access request; stay within CFAA /
  ECPA bounds.
- **Chain of custody** — every item, especially Package B, needs unbroken
  documentation: who, what, when, why, transferred to whom.
- **Package order** — Package A must be validated before Package B is
  examined.
- **Attribution discipline** — test whether manipulation is attributable
  to Okafor, Nkosi, or a third party; never infer authorship from a single
  artifact.
- **Separation of roles** — keep observation/examination distinct from
  analysis/interpretation.
- **Professional standards** — anchor procedures to NIST SP 800-86 and
  SWGDE best practices; disclose limitations in the final report.
