# Appendix A — Evidence base

"Checked" means I opened the source or queried the API myself on 1 October 2026. "Reported" means it came from a research pass and was not independently re-opened; treat with one notch less confidence and re-verify before quoting it in the forum.

## A1. The program and the competition

| Fact | Status | Source |
|---|---|---|
| Round 1: $7,000 pool, 2 to 4 grants of $1,000 to $3,000; applications due 9 Oct; vote week of 12 Oct; delivery week of 30 Nov; each request needs at least one week of public discussion before the vote | Checked | https://shutternetwork.discourse.group/t/shutter-dao-0x36-impact-pilot-program-round-1-grant-guide-application-template/951 and /t/940 |
| Three applications filed as of 1 Oct, all Objective 6 (PEN): Alex Soto $2,500 (passed submission check), franklincg $3,000 (check pending), Crezno $1,200 (passed, after SEEDGov cut already-done work from a $2,000 ask) | Checked (tracker bundle and the three threads) | https://shutter-impact-pilot.vercel.app ; /t/952, /t/958, /t/964 |
| SEEDGov's completeness checks ask for social handles, GitHub, and how you heard about the program; SEEDGov reclassified completed work as Round 2 | Checked | /t/958, /t/964 |
| Rika (Axia) accepted that merged PRs, verified contracts, tx hashes, documentation and reproducible outcomes count as evidence; declined a formal priority list | Checked | /t/940 replies 1 Sep 2026 |
| brainbot's July 2026 POIDH bounty paid nothing: "five of the six did not surface new insight"; "read as substantially AI generated"; future bounties will have "narrower and more concrete deliverables" | Checked | https://shutternetwork.discourse.group/t/poidh-bounty-review-complete/934 |
| Axia named "governance privacy adoption", builders of working Shutter API demos, and connectors to DAOs, wallets, L2s as desired contributions (polls had zero voters) | Checked | https://shutternetwork.discourse.group/t/exploring-what-it-means-to-advance-shutter/865 |
| brainbot Oct 2026: $107,000 (96,396 sUSDS), 6.22 FTE (1.25 business, 3.4 dev); priorities include "Land 3 crypto or real-world integrations for the new Shutter Governance Permanent Private Voting suite", keypers for 2 integrations, "implement fee structures for 2 integrations" | Checked | https://shutternetwork.discourse.group/t/provide-a-grant-to-brainbot-gmbh-october-2026/961 |
| brainbot Aug 2026: "Waiting for Snapshot's review and implementation of our PR"; Munich prototype election 14 Sep; Shutter Governance SDK nearly complete; discussions with Gnosis, Nethermind, Erigon on GIP-153 and "possible roles for Shutter in EEZ"; out-of-protocol mempool blocked by Primev resource constraints; keypers Gnosis 6 online (4/7), API 5/5 (3/5), Time Capsule 11/11 (5/11) | Checked | https://shutternetwork.discourse.group/t/brainbot-update-for-august-2026/946 |
| No new Round 1 applications and no September brainbot update posted as of 1 Oct | Checked | forum latest.json |

## A2. Private voting: the two live decisions

| Fact | Status | Source |
|---|---|---|
| ENS temp check by netto.eth 27 May 2026; consul.eth (Luis, Shutter) replied same day; 16 Jun netto.eth promised a later vote on four scope options; last reply 16 Jun 2026; no scope vote posted | Checked | https://discuss.ens.domains/t/temp-check-shielded-voting-for-ens-snapshot-proposals/22142 |
| ENS ran two shielded elections after the temp check: Term 7 Meta-Governance WG Election (created 26 Jun 2026, Copeland, 60 votes) and [6.47] Election of the New ENS DAO Security Council (7 Jul 2026, Copeland, 50 votes) | Checked (hub API, `privacy: "shutter"`) | hub.snapshot.org, space ens.eth |
| ENS and Arbitrum spaces have `voting.privacy = "any"`; Shutter DAO 0x36 has `"shutter"` | Checked | hub API |
| Arbitrum shielded Snapshot elections: AGV 2026 Council Elections (27 Nov 2025, 1,691 votes); OAT Elections (9 Jul 2026, 2,226 votes); "Updating the Code of Conduct & DAO Procedures to Become Living Documents" passed Mar 2026 (1,383 votes) | Checked (hub API) | hub.snapshot.org, space arbitrumfoundation.eth |
| Entropy's figures: large-voter participation 41 vs 44; final-24h VP share 50.53% shielded vs 41.59% public; early voting (days 1 to 3) roughly 30% to 10% in an ARDC comparison | Checked | https://forum.arbitrum.foundation/t/updating-the-code-of-conduct-daos-procedures/29594 |
| 2024 Arbitrum vote: Against 69.2M, Elections-only 59.6M, All votes 32.6M (3,603 voters) | Reported | https://forum.arbitrum.foundation/t/should-the-dao-default-to-using-shielded-voting-for-snapshot-votes/25884 |
| Snapshot PR 2382 "permanent private voting via Shutter threshold ElGamal" by blockchainluffy: open, unmerged, 19 commits, adds te-data-layer, hub/sequencer changes, UI option marked Alpha; keypers run outside Snapshot | Checked (PR page) | https://github.com/snapshot-labs/sx-monorepo/pull/2382 |
| Shutter marketing numbers: "887 spaces since 2022" (Snapshot Labs in the Shutter migration thread, Aug 2026); 881 DAOs / 372,914 votes (Shutter blog Oct 2025); "87% of DAOs still using after 1 year" (shutter.network/shielded-voting) | Reported | /t/867; https://blog.shutter.network/permanent-shielded-voting-is-coming-to-snapshot/ ; https://shutter.network/shielded-voting/ |
| PSE and Shutter "State of Private Voting 2026" ranks Shutter shielded voting "high maturity" and permanent shielded voting "low, research-stage PoC"; it reports counts, not effects | Reported | pse.dev report PDF |
| Aave trial participation drop (13.5k to 2k votes per proposal) is a claim cited by Arbitrum delegates; VitaDAO enabled Dec 2022 and silently disabled in 2024 | Reported | /t/25884 ; gov.vitadao.com/t/1744 |
| Snapshot shielded voting is free; Shutter said in 2024 it would stay free; no payment from Snapshot to Shutter is on record | Reported | https://shutternetwork.discourse.group/t/shielded-voting-by-shutter-on-gitcoin/392 ; discuss.octant.app/t/175 |
| Shutter Governance (shuttergovernance.com) is operated by brainbot GmbH; no public pricing; named pilot is the City of Munich staff council election with UniBw München and Votebase; the city's request to run a legally binding digital election was rejected in Aug 2026, so the 14 Sep run was a non-binding prototype | Reported | shuttergovernance.com ; Behörden Spiegel 26 Aug 2026 |
| Keyper Compensation Program: 50 USDC-equivalent per keyper per month in SHU; renewed Sept 2026 to Feb 2027 | Reported | /t/944 |

## A3. Data feasibility (all checked 1 Oct 2026)

* `proposals` objects on hub.snapshot.org/graphql carry `privacy` (`""` or `"shutter"`); `privacy` is not filterable in `where`, so the pipeline pages all closed proposals by `created` and filters client-side.
* `votes` objects return `voter`, `created`, `vp`, `choice`; page size 1,000 works; `skip` 5,000 works; the documented limit is 100 requests per minute; API keys are available for more.
* Among the last 400 closed proposals, 21 were shielded.
* 2026 year-to-date pull (script `tools/snapshot_shielded_pull.py`, five API pages): 4,364 closed proposals, 146 shielded (3.35%), 47 spaces, 5,969 votes on shielded proposals; by month Jan 20, Feb 19, Mar 11, Apr 12, May 15, Jun 24, Jul 16, Aug 17, Sep 12 (September partial, closed proposals only); by type basic 63, single-choice 36, quadratic 24, ranked-choice 10, weighted 9, approval 2, Copeland 2; top spaces ShapeShift DAO 17, ODO DAO 17, Forgotten Runes 7, Shutter DAO 0x36 7, Grid Phantoms 7, Suzuverse 7.
* Caveat: the hub API excludes flagged spaces and proposals; the report must state this.
* No cross-DAO study of shielded voting effects was found in web search (results were launch announcements and forum threads).

## A4. Other tracks, for context (reported unless marked)

* Encrypted mempool on Gnosis: explorer API shows 4,721 shielded transactions executed since July 2024, 3 in the last month, estimated inclusion time about 11 hours, 37 registered validators (marketing pages say 8,000), roughly 26% of historical submissions "NotIncluded". GIP-153 moves Gnosis Chain to a centrally sequenced "Ethereum Economic Zone" rollup around Dec 2026 to Jan 2027, retiring the validator opt-in model the mempool depends on.
* Concorde: alpha framework (1 star, no LICENSE file as of 1 Oct), invite-only hosted launcher, no external deployment or usage number anywhere, no pricing; the Objective 3 track had no applicant as of 1 Oct.
* PEN: live on mainnet with 100 SEATs, 6 holders, 101 USDC idle, no vault, no yield, one executed on-chain proposal; three of three Round 1 applications target it.
* Shutter API: time-based decryption independent of transactions is production on Gnosis mainnet (free, rate-limited; paid keys by email, no published price); event-based decryption is beta; JS SDK is v0.0.2 (June 2025); sealed-bid RFP dApp at rfp.shutter.network is a PoC with off-chain reveal verification (checked: page loads).
* Tokenized markets: no Shutter relationship with any RWA operator exists; documented allocation-fairness pain is on token launchpads (Plasma, MetaDAO docs), not on tokenized equities.
