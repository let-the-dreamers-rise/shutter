# Forum post (copy everything below the line)

Title: `[Shutter DAO 0x36 Impact Pilot Program Round 1 - Proactive Grant] Shielded Voting Evidence Pack: ENS scope proposal, Arbitrum brief, and fee-structure inputs`

Category: SD 0x36 Proposals. Tags: proposal, feedback_requested.

---


## 1. Application

**Applicant name or organization:** Ashwin Goyal (independent contributor)

**Primary contact / forum handle:** @YOUR_FORUM_HANDLE

**Social handle (X and/or LinkedIn):** YOUR_X_OR_LINKEDIN

**GitHub profile:** https://github.com/let-the-dreamers-rise

**How did you hear about this grant program?** The Round 1 Grant Guide thread on this forum.

**Wallet address for payment (if approved):** YOUR_ETHEREUM_MAINNET_ADDRESS

**Application type:**

* ☑ Round 1 — Proactive grant for defined future work

**Round 1 objective (select one):**

☑ Objective 2 — Qualify a Private Voting Deployment

**Contribution area:**

* ☑ Research or technical work
* ☑ Ecosystem development, partnerships, or business development (supporting role: the outputs are sales and decision material for brainbot's private-voting integrations)

---

## 2. The Shutter need or opportunity

### What specific need, opportunity, or gap does this contribution address?

Two named bodies are in the middle of deciding how far to extend Shutter shielded voting, and neither they nor Shutter have the evidence the decision needs.

1. **ENS DAO.** On 27 May 2026 netto.eth opened a temp check on shielded voting for ENS Snapshot proposals. Luis (consul.eth, Shutter) replied the same day offering support. ENS then ran its Term 7 Meta-Governance steward election (26 June 2026) and its Security Council election (7 July 2026) with shielded voting. On 16 June netto.eth committed to "a separate vote later to define whether it should be: enforced for all proposals / decided by the proposer / applied only to specific categories / not adopted at all." As of 1 October 2026 that vote has not been posted and the thread's last reply is 16 June. The ENS space privacy setting is still "any" (proposer's choice).
2. **Arbitrum DAO.** Arbitrum shields Snapshot elections only. Its 2024 vote rejected shielding all votes (Against 69.2M ARB, Elections-only 59.6M, All votes 32.6M). The only analysis anyone has produced is Entropy Advisors' 2025 note: large-voter participation held (41 vs 44 wallets above 100k VP) but the share of voting power cast in the final 24 hours rose from 41.59% to 50.53%. In March 2026 Arbitrum made its Code of Conduct and procedures "living documents" and in July 2026 it ran the OAT elections shielded (2,226 votes). The open question for Entropy and the Arbitrum Foundation is whether shielding should go beyond elections, and nobody has updated the numbers since 2025.

In four years of production (Snapshot integration live since October 2022), no cross-DAO study of what shielded voting does to participation, late voting, margins, quorum attainment or retention exists. Shutter's public figures are cumulative marketing numbers: "887 spaces since 2022", "372,914 votes", "87% of DAOs still using after 1 year". The PSE and Shutter "State of Private Voting 2026" report counts deployments but measures no effects.

**A first pull on 1 October 2026 shows why this matters now.** Using the public Snapshot hub API (script and data at https://github.com/let-the-dreamers-rise/shutter, re-runnable by anyone): of 4,364 closed proposals created since 1 January 2026, **146 (3.35%) across 47 spaces used shielded voting, carrying 5,969 votes**. The active base in 2026 is about 47 spaces, not 887. The two largest 2026 users are ShapeShift DAO and ODO DAO (17 proposals each); ENS and Arbitrum use it for elections only. Shutter is about to pitch institutions (City of Munich consortium, universities, associations) and to set fees for two integrations. It should do that with real retention and effect numbers in hand, before a buyer or a DAO delegate pulls them.

### Why is it relevant to Shutter now?

* brainbot's October 2026 grant lists as a priority: "Land 3 crypto or real-world integrations for the new Shutter Governance Permanent Private Voting suite", secure keypers in 2 integrations, and "implement fee structures for 2 integrations". Fee structures need a usage baseline. There is none.
* Shutter's permanent private voting pull request to Snapshot (snapshot-labs/sx-monorepo PR 2382, threshold ElGamal) is open and unmerged; brainbot's August update says it is "waiting for Snapshot's review". Evidence of sustained demand across spaces strengthens the case for Snapshot to merge and for ENS to be a first production space.
* The ENS scope vote is overdue by netto.eth's own plan, and ENS is the warmest large-DAO door Shutter has (two shielded elections, a Shutter team member already in the thread).
* Axia's June 2026 thread on advancing Shutter named "governance privacy adoption" and "integration discovery" as high-leverage contribution types. A Shutter DAO 0x36 delegate (Mikko) called shielded voting "non-negotiable" when the DAO chose its new governance platform in August 2026.

### What specific demand signal supports this work now?

* ENS temp check and the unfulfilled follow-up vote: https://discuss.ens.domains/t/temp-check-shielded-voting-for-ens-snapshot-proposals/22142
* ENS shielded elections on Snapshot: Term 7 Meta-Governance WG Election (26 June 2026, Copeland, 60 votes); [6.47] Election of the New ENS DAO Security Council (7 July 2026, Copeland, 50 votes). Both carry `privacy: shutter` on the hub API.
* Arbitrum: https://forum.arbitrum.foundation/t/should-the-dao-default-to-using-shielded-voting-for-snapshot-votes/25884 and https://forum.arbitrum.foundation/t/updating-the-code-of-conduct-daos-procedures/29594 (Entropy's late-voting figures); shielded OAT Elections 9 July 2026 on the hub API.
* brainbot October 2026 grant priorities: https://shutternetwork.discourse.group/t/provide-a-grant-to-brainbot-gmbh-october-2026/961
* brainbot August 2026 update (Snapshot PR status): https://shutternetwork.discourse.group/t/brainbot-update-for-august-2026/946
* Snapshot PR: https://github.com/snapshot-labs/sx-monorepo/pull/2382
* Axia, "Exploring What it Means to Advance Shutter": https://shutternetwork.discourse.group/t/exploring-what-it-means-to-advance-shutter/865
* Fresh usage pull: https://github.com/let-the-dreamers-rise/shutter/blob/claude/hopeful-euler-bmuy6e/data/summary_since_2026-01-01.json produced by `tools/snapshot_shielded_pull.py` in the same repository.

### Who benefits from the outcome, and how?

* **brainbot (operating owner of Shutter Governance and the Snapshot integration):** citable effect and retention numbers for integration pitches, and a cost-and-comparables basis for the two fee structures it has committed to implementing.
* **ENS Meta-Governance stewards and netto.eth:** a decision-ready scope proposal with the data behind each of the four options they named.
* **Entropy Advisors and the Arbitrum Foundation:** an update of their own 2025 analysis through 2026, with the extension options costed in participation terms.
* **Snapshot Labs:** demand evidence to weigh the open permanent-private-voting PR.
* **Shutter DAO 0x36:** an honest baseline for its product closest to revenue, in a form it can reuse in every future private-voting conversation.
* **The 47 spaces using shielded voting in 2026:** a public dataset about their own governance.

### Value pathway (required for Round 1)

* ☑ Validated path toward a pilot, integration, or repeatable workflow (primary)
* ☑ Direct or protocol-generated Shutter revenue (secondary: the fee-structure inputs feed brainbot's stated Q4 KPI)

### Who is the relevant decision-maker, operating owner, funder, partner, or beneficiary group?

| Role | Who | Status |
|---|---|---|
| Decision-maker, ENS | netto.eth (temp-check author) and the Term 7 Meta-Governance stewards | Named; public thread; the vote they promised is outstanding |
| Decision-maker, Arbitrum | Entropy Advisors (authors of the shielded-elections policy) and Arbitrum Foundation governance | Named; policy now a "living document" |
| Operating owner, Shutter | brainbot gmbh, Luis Bezzenberger (Shutter Governance, consul.eth in the ENS thread) and Loring Harkness (DAO operations) | Named; already in the ENS thread; asked in-thread to confirm usefulness during the discussion week |
| Platform | Snapshot Labs (shielded voting host; reviewer of PR 2382) | Named |
| Beneficiary group | Shutter DAO 0x36; the 47 active shielded-voting spaces | Named |

### What problem are they solving, and what evidence supports the value of addressing it?

ENS delegates want to extend shielding without depressing participation (jkm.eth raised the "lazy voter" concern on 16 June 2026). Arbitrum saw late voting rise under shielding and voted down universal shielding in 2024; whether that trade-off holds in 2026 is unknown. brainbot has to price two integrations and has no usage baseline. Each of these decisions is currently being made on one DAO's one-year sample and on cumulative marketing counts.

### What Shutter product, deployment, service, or capability would this contribution advance?

Snapshot shielded voting (production since 2022), permanent private voting on Snapshot (PR 2382), and Shutter Governance's institutional offering and fee structure.

### What decision, implementation step, or next action should this contribution enable, and by when?

| Counterpart | Decision or step | Target date |
|---|---|---|
| ENS Meta-Governance | Post the scope vote netto.eth committed to, using the drafted proposal and evidence pack | Draft delivered by 25 Nov 2026; ENS vote within Term 7 (by end of December 2026) |
| Entropy Advisors / Arbitrum Foundation | Decide whether to propose extending shielding beyond elections, with 2026 numbers | Brief delivered by 25 Nov 2026 |
| brainbot | Use the fee-structure inputs memo in its two Q4 integration negotiations | Memo delivered by 25 Nov 2026 |
| Snapshot Labs | Evidence pack linked in the PR 2382 discussion | By 30 Nov 2026 |

### What evidence will show progress beyond outreach, general interest, or a speculative concept?

Everything below is public and re-runnable; none of it is a meeting or a contact list.

1. **Pre-registered analysis plan** (metrics, strata, comparison design, exclusion rules) published before any result, so reviewers can check that findings were not chosen after the fact.
2. **Open dataset and pipeline:** every shielded proposal since October 2022 with its votes (voter, voting power, timestamp, choice after reveal), matched control proposals from the same spaces, a per-space timeline of when shielding was enabled, paused or dropped. MIT licence. Already started: see https://github.com/let-the-dreamers-rise/shutter (`tools/` and `data/`).
3. **Evidence report** with stratified results and explicit limits.
4. **Two decision briefs posted into the live threads** (ENS, Arbitrum) and delivered to the named people.
5. **Fee-structure inputs memo** for brainbot.

---

## Deliverables and acceptance criteria

| # | Deliverable | Acceptance criterion (what the DAO can check) |
|---|---|---|
| D1 | Pre-registered analysis plan | Published in the repo and on the Shutter forum by the end of week 1 with a content hash; later deviations listed in the report |
| D2 | Dataset and pipeline | Public repo; `make all` (or one documented command) rebuilds the dataset from the Snapshot hub API; CSV/Parquet files with row counts stated; per-space enable/disable timeline |
| D3 | Evidence report (10 to 20 pages) | Covers, for shielded vs public proposals within the same spaces and against matched spaces: number of voters, voting power cast, share of VP in the final 24 hours and first 72 hours, winning margin, quorum attainment, proposal outcome type; retention and churn by space (first and last shielded proposal, months active, spaces that stopped); results stratified by proposal type (elections and ranked-choice vs single-choice and basic) and by space size. Every figure traceable to a query in D2. Includes a one-page "claims audit" that states which of Shutter's published figures (887 spaces, 87% retention) the data supports and how to phrase them defensibly |
| D4 | ENS scope proposal draft and Arbitrum brief | ENS: a proposal in ENS's format for the four options netto.eth named, with the projected participation and timing effects for each, a recommended option, and a "sponsored keyper set" cost line as an optional first paid DAO reference. Posted as a reply in the ENS temp-check thread and sent to netto.eth and Luis. Arbitrum: a two-page brief updating Entropy's figures through 2026, posted in the Arbitrum forum |
| D5 | Fee-structure inputs memo for brainbot | Cost basis (keyper operation cost using the DAO's own Keyper Compensation Program figures, 50 USDC-equivalent per keyper per month, and a 3-of-5 or 4-of-7 set), comparables (POLYAS per-voter pricing in Germany; Snapshot Pro tiering), and three candidate models (free tier plus sponsored keyper set; per-election fee; platform revenue share). Delivered to brainbot and published |

### Milestone for the second 50% payment

All five deliverables public, with D4 posted in the ENS and Arbitrum threads, by **30 November 2026**. For transparency, an informational checkpoint (D1 and a first cut of D2 with descriptive statistics) is published by **4 November 2026** so the DAO can see the work is real before the final review.

### Timeline (assuming award in the week of 12 October)

| Week | Dates | Work |
|---|---|---|
| 1 | 15 to 21 Oct | Request a Snapshot API key; finalise corpus definition; publish D1 pre-registration |
| 2 | 22 to 28 Oct | Full pull of shielded proposals and votes since Oct 2022; control sampling from the same spaces; data quality checks |
| 3 | 29 Oct to 4 Nov | Checkpoint: dataset v1, pipeline, descriptive statistics, per-space timeline |
| 4 | 5 to 11 Nov | Analysis: participation, timing, margins, quorum, retention; strata; sensitivity checks |
| 5 | 12 to 18 Nov | Evidence report draft; factual review requested from brainbot and netto.eth (facts only, not approval) |
| 6 | 19 to 25 Nov | ENS proposal draft and Arbitrum brief posted; fee-structure memo delivered |
| 7 | 26 to 30 Nov | Final report, forum delivery post, hand-off of repo (offer to transfer to the shutter-network GitHub organisation) |

### Out of scope

No new cryptography, no changes to Snapshot or Shutter code, no lobbying. ENS's and Arbitrum's decisions are the stated next steps, not grant milestones; the grant is judged on the artifacts.

### Risks and honest limits

* **The data may not flatter shielded voting in every segment.** Arbitrum's late-voting shift and the participation drop reported in Aave's trial are real possibilities. I will publish whatever the data shows. A split result (elections benefit, routine votes do not) is itself the "specific categories" option ENS asked about, and it is better for Shutter to know before an institutional buyer checks.
* **Observational data.** Spaces choose to shield; the design uses within-space comparisons (especially "any" spaces like ENS and Arbitrum where shielded and public proposals coexist) and matched controls, and reports effect ranges rather than single causal claims.
* **API limits.** The public hub allows 100 requests per minute, pages of 1,000, and `skip` to 5,000; the pipeline pages by timestamp instead of `skip`. The whole shielded corpus is in the order of 5,500 proposals and 370,000 votes, which is hours of pulling, not weeks. Note that the hub API omits flagged spaces, which will be stated in D3.
* **Counterparts may not act inside the window.** The deliverables do not depend on them; the briefs stand as decision material for whenever they act.

### Why this applicant

Independent builder and analyst. Relevant public work: `brier` (a stratified analysis of dispute rates across 3,464 settled Polymarket markets, with z-scores and an explicit warning against reading pooled rows), `veridict` and `germline-avalanche` (commit-reveal workflows deployed on public testnets with explorer-linked evidence), `rein` (verified contracts on three testnets with an honest-status section). The method here is the same as `brier`: public data, pre-stated strata, reproducible numbers, limits stated up front. All repositories are at https://github.com/let-the-dreamers-rise.

---

## 3. Funding request

**Amount requested:** $2,000 (paid per the program's USDC and SHU arrangement; 50% on approval, 50% after milestone review)

**Proposed use of funds / budget rationale:**

| Item | Amount |
|---|---|
| D1 pre-registration and D2 dataset and pipeline (corpus definition, pull, cleaning, timeline construction, documentation) | $600 |
| D3 evidence report (analysis, strata, sensitivity checks, claims audit, writing) | $700 |
| D4 ENS scope proposal draft and Arbitrum brief | $400 |
| D5 fee-structure inputs memo | $200 |
| Snapshot API key, hosting of dataset and static report | $100 |
| **Total** | **$2,000** |

If the DAO prefers a smaller award, an ENS-only version (D1, D2, D3, the ENS half of D4, D5) is $1,700.

---

## 4. Prior compensation and disclosures

**Have you, your organization, or a related party received or requested compensation for this work from Shutter or another source?**

* ☑ No

**Do you have any financial, professional, or organizational conflict relevant to this application?**

* ☑ No. I hold no role with brainbot, Axia, SEEDGov, Snapshot Labs, ENS Labs or Entropy Advisors and have no SHU, ENS or ARB position relevant to this application.

Note on tooling: the application and the analysis code are prepared with AI-assisted tooling; every link and figure in this application was checked by hand against the source on 1 October 2026, and the deliverables are reproducible code and data rather than prose.

---

## 5. Public discussion

**Forum post link:** this thread.

**Questions or feedback requested from the community:**

1. brainbot (Luis, Loring): which three numbers would be most useful in your two Q4 fee-structure conversations? I will make sure D3 and D5 produce them.
2. Should the ENS scope proposal be posted by me as a reply in netto.eth's thread, or handed to netto.eth and Luis to post? I am fine either way; the deliverable is the draft and the evidence behind it.
3. Should the dataset and pipeline live under the shutter-network GitHub organisation at hand-off?
4. If budget is tight after the three PEN applications, is the $1,700 ENS-only version preferable to the DAO?

---

## 6. Applicant attestation

I confirm that the information in this application is accurate to the best of my knowledge; that I have disclosed relevant prior compensation and conflicts; and that I understand any award remains subject to the published process and DAO approval.

**Name / handle:** Ashwin Goyal / @YOUR_FORUM_HANDLE
