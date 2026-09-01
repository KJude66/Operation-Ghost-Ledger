# Operation Ghost Ledger – Digital Forensics Capstone

**Course:** Advanced Digital Forensics / ISS 7133
**Prepared by:** Kum Jude Wung
    

## Case summary

Senator Kwame Nkosi (Chair, Senate Committee on Public Works) and
Director-General Amara Okafor (National Water & Power Authority) are
accused of soliciting a 15% kickback on a $500M public infrastructure
contract — the Bahari River Dam. Evidence leaked to a whistleblower site
and went viral. The defence alleges the leak is an AI-driven political
framing operation (voice cloning, AI-generated financial records, planted
documents).

**The question this investigation must answer:** does the digital evidence
support genuine corruption, digital manipulation, or a mixture of authentic
and manipulated material?

## Core hypothesis

> The leaked files are a mixture of authentic and AI-manipulated content.

**Sub-hypotheses**
1. The audio base is authentic, but the 15% figure was spliced.
2. The PDF contains authentic structural data but doctored financial amounts.
3. The spreadsheet was created on Okafor's laptop and later modified.

**Falsification criteria** — the hypothesis is weakened/falsified if:
- no splicing is found in the audio,
- metadata does not differ between relevant file versions, and/or
- no AI-generation artifacts are detected in any exhibit.

See [`01_case_setup/README.md`](01_case_setup/README.md) for the full case
identification and evidence-package breakdown.

## Repository structure

| Folder | Contents |
|---|---|
| [`01_case_setup/`](01_case_setup/) | Case identification, core hypothesis, evidence inventory |
| [`02_phase1_public_validation/`](02_phase1_public_validation/) | Milestone 1 — Package A validation, hash catalogue |
| [`03_phase2_acquisition/`](03_phase2_acquisition/) | Milestone 2 — Package B imaging, chain of custody |
| [`04_phase3_analysis/`](04_phase3_analysis/) | Weekly case files — filesystem, memory, network, mobile, cloud, anti-forensics |
| [`05_phase4_correlation/`](05_phase4_correlation/) | Milestone 3 — master timeline, correlation report |
| [`06_phase5_final/`](06_phase5_final/) | Milestone 4 — affidavit and capstone presentation |
| [`scripts/`](scripts/) | Reproducible helper scripts (SHA-256 cataloguing) |
| [`METHODOLOGY.md`](METHODOLOGY.md) | Daubert factors, cognitive-bias controls, tooling plan |
| `Operation_Ghost_Ledger_Complete_Capstone.docx` | Full narrative report across all five phases |

## Roadmap

| Phase | Weeks | Deliverable |
|---|---|---|
| 1 — Public Evidence Validation | 1–3 | Milestone 1 — Validation Report |
| 2 — Hardware Acquisition & Imaging | 4–5 | Milestone 2 — Acquisition & Chain-of-Custody Log |
| 3 — Multi-Domain Analysis | 6–12 | Weekly Case File Updates |
| 4 — Correlation & Reconstruction | 13–14 | Milestone 3 — Correlation & Reconstruction Report |
| 5 — Final Affidavit & Expert Testimony | 15 | Milestone 4 — Final Affidavit & Oral Presentation |

## Evidence handling

Do **not** upload confidential/raw forensic evidence — E01 images, RAM
dumps, PCAPs, phone backups or cloud logs — to a public repository unless
the instructor explicitly authorizes it.

Upload only approved derived artifacts: sanitized logs, reports,
screenshots and scripts.

## Academic integrity

Actual hashes, timestamps, IP addresses and forensic tool outputs must be
generated from the real evidence package — they must **never** be
invented. Where this repository shows `TBD` or `[populate from analysis]`,
that field is intentionally left for the examiner to fill in from the
actual supplied evidence.

## Final submission checklist

- [ ] Milestone 1 — Public Evidence Validation Report
- [ ] Milestone 2 — Acquisition & Chain-of-Custody Log
- [ ] Weekly Case File Updates for Phase 3
- [ ] Milestone 3 — Correlation & Reconstruction Report
- [ ] Milestone 4 — Final Affidavit
- [ ] 15-minute oral presentation
- [ ] No fabricated hashes, timestamps, IPs, screenshots or conclusions
- [ ] All sensitive/original evidence excluded from this public repository
