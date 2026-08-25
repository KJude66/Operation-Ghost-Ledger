# Case Setup — Operation Ghost Ledger

## 1. Case identification

Operation Ghost Ledger is the semester-long forensic investigation.
Senator Kwame Nkosi and Director-General Amara Okafor are accused of
soliciting a 15% kickback on a $500M Bahari River Dam public infrastructure
contract. The defence alleges the evidence is an AI-driven political
framing operation involving AI voice cloning, AI-generated financial
records and planted documents.

**Role:** Lead Forensic Examiner for the Bahari Anti-Corruption Commission
(BACC). The ultimate forensic question is whether the digital evidence
supports genuine corruption, digital manipulation, or a mixture of
authentic and manipulated material.

## 2. Evidence packages

| Package | Classification | Contents | Primary concern |
|---|---|---|---|
| A — Public Leak | Found evidence | `audio.wav`; `Execution_Certificate.pdf`; `Bribe_Calculation.xlsx`; screenshots; archived webpage (`.warc`) | No formal chain of custody; source and integrity must be validated |
| B — Seized Hardware | Seized evidence | Okafor Windows 11 E01 image; memory dump; 72-hour PCAP; mobile SQLite backups; NWPA Oracle Cloud JSON logs | Must be acquired/preserved correctly, then examined using validated methods |

Full inventory: [`evidence_inventory.csv`](evidence_inventory.csv).

**Rule:** Package A must be validated before Package B is examined — the
public leak is the first crime scene.

## 3. Core hypothesis and sub-hypotheses

**Core hypothesis:** The leaked files are a mixture of authentic and
AI-manipulated content.

- The audio base is authentic, but the 15% figure was spliced.
- The PDF contains authentic structural data but doctored financial amounts.
- The spreadsheet was created on Okafor's laptop and later modified.

**Falsification criteria:** the hypothesis is weakened/falsified if no
splicing is found, metadata does not differ between relevant versions,
and/or no AI artifacts are detected.

This hypothesis is a starting point for the investigation, not a
conclusion — every phase below must actively test it, including looking
for evidence that would disprove it.
