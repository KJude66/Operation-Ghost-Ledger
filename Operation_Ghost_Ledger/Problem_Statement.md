# Problem Statement — Operation Ghost Ledger

**Course:** Advanced Digital Forensics / ISS 7133
**Prepared by:** Kum Jude Wung

## 1. Background

Senator Kwame Nkosi (Chair, Senate Committee on Public Works) and
Director-General Amara Okafor (National Water & Power Authority) are
accused of soliciting a 15% kickback on a $500M public infrastructure
contract — the Bahari River Dam. Evidence supporting the allegation
(`audio.wav`, a signed contract, a bribe-calculation spreadsheet,
screenshots and an archived webpage) surfaced on a whistleblower site and
went viral before it could be seized or authenticated by investigators.

The defence has responded not by disputing the facts, but by disputing
the *evidence itself*: it alleges the leak is an AI-driven political
framing operation — a voice-cloned recording, AI-generated financial
records, and documents planted on Okafor's laptop via a zero-day exploit.
This defence is credible enough to require rebuttal, because generative
AI tools capable of convincing voice cloning and document fabrication are
now widely accessible, and courts increasingly need forensic examiners who
can distinguish authentic digital evidence from synthetic or altered
material.

## 2. The problem

Investigators have two evidence sets of very different evidentiary
weight and risk:

- **Package A (the public leak)** — found evidence with no chain of
  custody, of unknown provenance, potentially tampered with before or
  during the leak.
- **Package B (seized hardware)** — Okafor's laptop, a memory dump, a
  72-hour network capture, mobile backups and cloud access logs, obtained
  under a formal warrant.

Neither package alone can resolve the case. Package A alone cannot be
trusted without independent verification; Package B alone cannot explain
what actually reached the public or how. The core problem this capstone
addresses is:

> **How can a forensic examiner determine, using only reproducible,
> evidence-based methods, whether the leaked material is genuine,
> AI-manipulated, or a mixture of both — and produce findings that would
> hold up to cross-examination and Daubert scrutiny in court?**

This is not simply a technical problem of running the right tools. It is
a problem of *methodological discipline*: validating evidence before
trusting it, testing a hypothesis instead of assuming guilt or innocence,
guarding against confirmation bias, and correctly attributing any
manipulation found to a specific actor rather than inferring authorship
from a single artifact.

## 3. Core hypothesis

> The leaked files are a mixture of authentic and AI-manipulated content.

**Sub-hypotheses**
1. The audio base is authentic, but the 15% kickback figure was spliced in.
2. The PDF contract has authentic structural data but doctored financial amounts.
3. The spreadsheet was created on Okafor's laptop and later modified.

**Falsification criteria** — the hypothesis is weakened or falsified if:
- no splicing is found in the audio,
- metadata does not differ between relevant file versions, and/or
- no AI-generation artifacts are detected in any exhibit.

## 4. Objectives

1. Validate Package A independently before Package B is ever examined.
2. Acquire and image Package B using forensically sound, write-blocked methods with an unbroken chain of custody.
3. Conduct multi-domain analysis (filesystem, memory, network, mobile, cloud, anti-forensics) to test each sub-hypothesis.
4. Correlate findings across both packages into a single, evidence-grounded master timeline.
5. Produce a court-ready affidavit that states forensic — not legal — conclusions, with documented limitations and confidence levels.

## 5. Scope and limitations

**In scope:** forensic validation, imaging, and multi-domain analysis of
the two evidence packages as defined by the course scenario; correlation
and timeline reconstruction; production of the four milestone
deliverables.

**Out of scope:** determining criminal guilt or innocence (a legal, not
forensic, conclusion); any evidence not included in Package A or Package
B; live incident response or ongoing evidence collection beyond the
scenario's fixed set of exhibits.

**Constraint:** no hash value, timestamp, IP address, or tool output may
be fabricated. Where the real evidence files are unavailable, deliverables
must clearly mark the field as pending rather than inventing a plausible
value.

## 6. Significance

Corruption cases involving digital evidence are increasingly contested on
the grounds that the evidence itself was synthetically generated — a
defence that will only become more common as generative AI tools improve.
This capstone is significant because it forces the examiner to build and
defend a reproducible, bias-resistant methodology capable of surviving
that specific line of attack, rather than relying on the evidence being
self-evidently genuine.

## 7. Source

Primary source: *Class 1 — ISS 7133 — Digital Forensics Fundamentals*,
capstone scenario and walkthrough, pp. 16–27 and 236–238. Supplementary
application in *Class 2 — Digital Evidence Types, Lifecycle & Legal
Foundations* and *Class 3 — Forensic Imaging and Cryptographic Hashing*.
