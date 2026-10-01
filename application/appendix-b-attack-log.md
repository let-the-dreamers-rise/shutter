# Appendix B — Candidate proposals and the attack log

Method: for each objective, draft the strongest proposal this specific applicant could file, then attack it the way SEEDGov's completeness check, Axia's rubric (evidence, value, relevance, quality and leverage, cost discipline) and the voters who actually show up (brainbot's delegate, Axia, SEEDGov, Kleros, czepluch, Mikko, d0z3y) would. Keep only what survives.

Applicant constraints that shaped every attack: solo builder and analyst; verifiable public work (deployed, verified contracts; stratified data analysis); no relationships in the Shutter, ENS, Arbitrum or Gnosis ecosystems; unknown to the voters; the DAO has recently refused to pay for work that "read as substantially AI generated".

## Scoreboard

| # | Objective | Candidate | Verdict |
|---|---|---|---|
| C1 | 2 | Shielded-voting evidence pack, ENS scope proposal, Arbitrum brief, fee-structure inputs | **Survives. Filed.** |
| C2 | 3 | Concorde opportunity assessment for delegate organisations and DAO working groups (interviews plus a 2-week shadow on Shutter DAO's October votes) | Runner-up |
| C5 | 5 | Sealed-RFP kit on the Shutter API (hardened contract, operator guide, pilot package) with Shutter DAO as first user and ENS SPP committee as target | Runner-up |
| C3 | 1 | Seer/Kleros order flow on the Gnosis encrypted RPC: measured feasibility plus validator baseline and EEZ note | Killed |
| C4 | 6 | PEN proposals and voting page in pen-interface, plus capture-cost note | Killed for Round 1 |
| C6 | 4 | Sealed indication-of-interest for onchain IPO allocations (Superstate partners) or sealed launchpad commitments | Killed |
| C7 | 7 | Open-source keyper uptime monitor for the compensation programme | Killed |

## C1 — Objective 2 (filed)

**Attack: "This is a research report. Objective 2 wants a pilot proposal tied to a named body, what they would pay, and a next decision."**
Answered by restructuring: the primary deliverable is a drafted ENS scope proposal for the vote netto.eth promised on 16 June and never posted, with a costed sponsored-keyper-set option; the evidence pack substantiates it; the Arbitrum brief and fee memo are second and third. The next decisions and dates are in a table.

**Attack: "brainbot's Luis is already in the ENS thread. Duplication."**
Luis offered technical support on 27 May 2026, not evidence. brainbot has 1.25 business FTE and 3.4 developer FTE and has produced no participation study in four years. The application asks brainbot in the discussion week which numbers it needs, which converts possible friction into a public demand signal.

**Attack: "Negative result risk. Aave reportedly lost most voters; VitaDAO quietly turned it off; Arbitrum's late voting rose."**
Pre-registered, stratified analysis; publish regardless. A split result is ENS's "specific categories" option. Shutter Governance is selling to institutions who will check these numbers, so the DAO is better off commissioning them than being surprised.

**Attack: "You cannot pull this from a public API."**
Checked on 1 October: `privacy` on proposals, `created` and `vp` on votes, page size 1,000, `skip` 5,000, 100 requests per minute, API keys available. The 2026 slice took five requests. The full shielded corpus is roughly 5,500 proposals and 370,000 votes.

**Attack: "Unknown applicant; can they do statistics?"**
Public repository `brier`: stratified dispute-lift analysis over 3,464 settled markets with z-scores and an explicit warning against pooled rows. Same method.

**Attack: "Reads as AI generated."**
Milestone 1 is a pre-registered plan plus raw data and code before any result; every figure traces to a query; a working pipeline and a real 2026 pull are already in the repository on day zero.

**Attack: "Cost discipline."**
$2,000 with a $1,700 fallback, itemised by deliverable, below two of the three asks already filed.

**Attack: "ENS may never vote; Arbitrum already runs shielded elections."**
The brief is the deliverable; ENS's vote is the stated next decision. Arbitrum's March 2026 living-documents change and July 2026 shielded OAT election make it the durability case; the brief updates Entropy's 2025 numbers.

**Attack: "The 2026 usage is tiny (47 spaces). Does this embarrass Shutter?"**
It is the strongest reason to fund it. brainbot is committing to fee structures and institutional pitches on cumulative counts. A defensible retention and effect story is worth more to those pitches than an inflated one that a buyer can falsify in an afternoon.

**Attack: "No merged PR or deployed contract."**
The accepted evidence list (Rika, 1 Sep 2026) includes documentation and reproducible outcomes. The repo, dataset, and posted briefs are reproducible outcomes; the fee memo feeds a stated brainbot KPI.

## C2 — Objective 3 (runner-up)

Strengths: the only empty "new product" track; brainbot calls shared agents a revenue product; Axia, SEEDGov, Exocortex and Kleros are all reachable inside the Shutter forum; a self-hosted shadow deployment on Shutter DAO's October votes is technically within reach for this applicant.

Attacks that stuck: the Launcher is invite-only and the framework has no LICENSE file, so a shadow deployment depends on brainbot inside the window; interview notes from an unknown applicant are the softest evidence class and sit next to the objective's exclusion of "unsupported use-case ideas"; the segment's economics are contested (Tally wound down in March 2026 saying the governance ecosystem cannot sustain companies; Coordinape sunset). Fundable, but the evidence is weaker than C1's. Keep for Round 2 or a later round after brainbot's "two initial communities" test reports.

## C5 — Objective 5 (runner-up)

Strengths: plays to the applicant's contract work; Shutter's own blog says DAOs overspend on open RFPs; Shutter DAO's own RFPs have all been public; ENS moved to confidential committee-held RFP submissions in July 2026 (a trusted-party seal Shutter can replace); the Shutter API's time-based decryption is production.

Attacks that stuck: "generic demos and unmaintained tooling do not qualify" and there is no named RFP inside the window to pilot on (Shutter DAO has not run an RFP in 2026; ENS SPP4 is 2027); brainbot already has a PoC (`SealedBidRFP`, rfp.shutter.network) so the work reads as maintenance of someone else's demo; on-chain verification of correct decryption is a heavier cryptographic task than $2,000 and seven weeks allow. Strong Round 2 or hackathon candidate once an operator commits to a dated process.

## C3 — Objective 1 (killed)

The measured state of the Gnosis encrypted mempool on 1 October: about 3 shielded transactions per month, estimated inclusion time about 11 hours, 37 registered validators against marketing claims of 8,000, and GIP-153 retiring the validator opt-in model within roughly three months. Any order-flow feasibility test returns "not feasible" before it starts, and the one live question (Shutter's role in the EEZ composer) needs Gnosis Ltd, which brainbot is already talking to and this applicant cannot reach. The validator-count discrepancy is worth a delegate asking brainbot about; it is not a grant.

## C4 — Objective 6 (killed for Round 1)

Real gaps exist (no proposal or voting page in pen-interface, no health-indicator dashboard, a capture cost in the low hundreds of dollars at 100 SEATs with quorum 10 and 70%+1). But three of three filed applications are already PEN, $6,700 of the $7,000 pool is spoken for if they all pass, PEN holds 101 USDC with no vault, and the DAO's stated top priority is revenue. A fourth PEN application competes with Crezno, Alex Soto and franklincg for the same votes instead of filling an empty commercial objective.

## C6 — Objective 4 (killed)

Shutter has no relationship with any tokenized-markets operator; the documented allocation-fairness pain is on token launchpads (Plasma's $100k gas race, MetaDAO's "see 2x oversubscribed, bid 2x"), not tokenized equities; onchain IPO venues (Superstate partners) publish no book-building rules to test against. An unknown applicant cannot produce "the operator, workflow, constraints and next decision" in seven weeks without a single warm contact. Objective 4 as written wants a named operator; a speculative design memo is exactly what it excludes.

## C7 — Objective 7 (killed)

The keyper compensation programme measures 90% uptime by hand and brainbot's own issue tracker wants weekly uptime reports; an open-source monitor would be durable. But Objective 7 awards "may not use funds reserved for Objectives 1–6 unless the DAO separately approves it", which the bundled Round 1 vote will not do.

## Residual risks on the filed proposal, and what to do about them

1. **Budget crowd-out by the three PEN applications.** Mitigation: the $1,700 fallback and question 4 in the application; the diversification argument is stated once, politely.
2. **brainbot indifference or defensiveness.** Mitigation: ask Luis and Loring a concrete question in the thread in the first 48 hours; offer the dataset to the shutter-network organisation; frame the claims audit as giving them defensible phrasing.
3. **Discussion-week timing.** The guide requires at least one week of discussion before the vote and applications are due 9 October. Post by 2 October.
4. **Being read as AI output.** Publish the pre-registration and a descriptive cut before the vote, not after.
