# Shutter DAO 0x36 Impact Pilot — Round 1 application and evidence

This repository holds a Round 1 proactive-grant application for the Shutter DAO 0x36 Impact Pilot, the evidence behind it, the log of alternatives considered and rejected, and a working data pipeline that already produces the first numbers the proposal relies on.

**The proposal (Objective 2, $2,000):** a Shielded Voting Evidence Pack. Four years of Snapshot shielded-voting data turned into an open dataset, a pre-registered analysis of what shielding does to participation, late voting, margins, quorum and retention, a drafted ENS DAO scope proposal for the vote netto.eth promised in June 2026 and never posted, a brief updating Entropy Advisors' Arbitrum numbers through 2026, and a fee-structure inputs memo for brainbot's two Q4 integration negotiations.

**First number, produced here on 1 October 2026:** of 4,364 closed Snapshot proposals created in 2026, 146 (3.35%) across 47 spaces used shielded voting. The active base is about 47 spaces, not the 887 cumulative figure used in marketing.

## Contents

| Path | What it is |
|---|---|
| `application/round1-application.md` | Posting-ready application in the program's template order. Fields marked **[FILL]** need the applicant's personal details. |
| `application/appendix-a-evidence.md` | Every factual claim with its source and whether it was checked by hand on 1 Oct 2026. |
| `application/appendix-b-attack-log.md` | Seven candidate proposals across all seven objectives, the attacks each faced, and why this one survived. |
| `application/appendix-c-72-hour-plan.md` | Posting deadline (2 October), tagging, office hours, and what to publish before the vote. |
| `tools/snapshot_shielded_pull.py` | Pulls every closed Snapshot proposal since a date from the public hub API and summarises shielded usage. No key needed. |
| `data/` | Output of the pipeline for 2026 year-to-date (CSV of proposals, JSON summary). |

## Run the pipeline

```bash
python3 tools/snapshot_shielded_pull.py 2026-01-01 data
```

Pages backwards by proposal creation time, stays under Snapshot's 100 requests per minute, and writes `data/proposals_since_<date>.csv` and `data/summary_since_<date>.json`.

## Status

Drafted 1 October 2026 for the 9 October deadline. Post by 2 October to satisfy the one-week discussion requirement.
