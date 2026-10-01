#!/usr/bin/env python3
"""Pull every closed Snapshot proposal created since a start date and summarise
which ones used Shutter shielded voting (privacy == "shutter").

Public API, no key needed. Pages backwards by `created` so it is not limited by
Snapshot's skip cap. Stays well under the 100 req/min limit.

Usage: python3 tools/snapshot_shielded_pull.py 2026-01-01 data/
"""
import csv, datetime as dt, json, sys, time, urllib.request, collections

HUB = "https://hub.snapshot.org/graphql"
Q = """{ proposals(first: 1000, orderBy: "created", orderDirection: desc,
  where: {state: "closed", created_lt: %d, created_gte: %d}) {
  id privacy created start end votes scores_total type quorum space { id } } }"""

def gql(q):
    req = urllib.request.Request(HUB, data=json.dumps({"query": q}).encode(),
                                 headers={"content-type": "application/json", "user-agent": "shielded-voting-evidence-pack/0.1 (+https://github.com/let-the-dreamers-rise/shutter)"})
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)["data"]
        except Exception as e:  # rate limit or transient
            time.sleep(5 * (attempt + 1))
    raise SystemExit("API failed repeatedly")

def main(start_str, out_dir):
    start = int(dt.datetime.fromisoformat(start_str).replace(tzinfo=dt.timezone.utc).timestamp())
    cursor = int(time.time())
    rows, pages = [], 0
    while True:
        batch = gql(Q % (cursor, start))["proposals"]
        pages += 1
        if not batch:
            break
        rows.extend(batch)
        cursor = batch[-1]["created"]
        if len(batch) < 1000:
            break
        time.sleep(0.7)
    seen = {}
    for p in rows:
        seen[p["id"]] = p
    rows = list(seen.values())
    with open(f"{out_dir}/proposals_since_{start_str}.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "space", "privacy", "type", "created_utc", "end_utc", "votes", "scores_total", "quorum"])
        for p in rows:
            w.writerow([p["id"], p["space"]["id"], p["privacy"] or "", p["type"],
                        dt.datetime.utcfromtimestamp(p["created"]).isoformat(),
                        dt.datetime.utcfromtimestamp(p["end"]).isoformat(),
                        p["votes"], p["scores_total"], p["quorum"]])
    sh = [p for p in rows if p["privacy"] == "shutter"]
    by_month = collections.Counter(dt.datetime.utcfromtimestamp(p["created"]).strftime("%Y-%m") for p in sh)
    all_month = collections.Counter(dt.datetime.utcfromtimestamp(p["created"]).strftime("%Y-%m") for p in rows)
    by_space = collections.Counter(p["space"]["id"] for p in sh)
    votes_sh = sum(p["votes"] for p in sh)
    summary = {
        "pulled_at_utc": dt.datetime.utcnow().isoformat(),
        "window_start": start_str,
        "api_pages": pages,
        "closed_proposals_total": len(rows),
        "shielded_proposals": len(sh),
        "shielded_share_pct": round(100 * len(sh) / max(1, len(rows)), 2),
        "shielded_votes_total": votes_sh,
        "spaces_using_shielded": len(by_space),
        "shielded_by_month": dict(sorted(by_month.items())),
        "all_by_month": dict(sorted(all_month.items())),
        "top_25_spaces_by_shielded_proposals": by_space.most_common(25),
        "shielded_by_type": dict(collections.Counter(p["type"] for p in sh)),
    }
    with open(f"{out_dir}/summary_since_{start_str}.json", "w") as f:
        json.dump(summary, f, indent=2)
    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "2026-01-01", sys.argv[2] if len(sys.argv) > 2 else "data")
