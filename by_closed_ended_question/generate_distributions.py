#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Regenerate the closed-ended distributions from the CSVs (single source of truth).

- Writes analysis/q_XX_distribution.json (vocabulary order, percentages over all articles).
- Updates, in STATISTICS.md, the article total, the "Estatísticas" bullets, the
  "Distribuição de Valores" tables and the response-coverage table. Narrative
  observations are left as written.

Usage: python3 generate_distributions.py
"""

import csv
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path

BASE = Path(__file__).parent

VOCABULARY = {
    "04": ["B2C", "B2B SMB", "B2B", "Mid-market", "Enterprise", "Developers/Dev-tools", "Government", "Others"],
    "08": ["Application", "Platform", "API", "SDK", "Data", "Managed Service", "Infrastructure", "Others"],
    "09": ["On-premises", "Single-tenant cloud", "Multi-tenant SaaS", "Edge", "Mobile", "Desktop", "Others"],
    "10": ["Proprietary", "Permissive Open Source", "Copyleft", "Dual License", "Open Core", "Others"],
    "12": ["Perpetual license", "Subscription", "Usage/consumption", "Transaction", "Advertising", "Support",
           "Dual licensing", "Open core", "Marketplace fees", "Others"],
    "13": ["User/seat", "MAU", "API calls", "Computing time", "Storage", "Transactions", "Devices", "Revenue sharing", "Others"],
    "14": ["Freemium", "Trial", "Tiers/Plans", "Pay-as-you-go", "Prepaid credits", "Annual contract", "Custom negotiation", "Others"],
    "16": ["Standalone product", "Two-sided platform", "Marketplace", "OEM component", "Plugin/Complement", "Others"],
    "17": ["None", "Direct (more users = more value)", "Cross-sided (distinct groups benefit)",
           "Data (more data = better product)", "Others"],
    "18": ["Product-led Growth", "Direct sales", "Partners/channels", "Marketplaces", "Digital marketing", "Referral", "Others"],
    "19": ["AWS Marketplace", "Azure Marketplace", "Google Cloud Marketplace", "Atlassian Marketplace",
           "Salesforce AppExchange", "Apple App Store", "Google Play Store", "Steam", "Others"],
    "30": ["Single case study", "Multiple cases", "Survey", "Experiment", "Secondary data analysis",
           "Literature review", "Expert opinion", "Others"],
}


def analyze(q):
    with open(BASE / f"question_{q}.csv", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    counts = Counter()
    for r in rows:
        counts.update({v.strip() for v in r["values_inside_scope"].split(";") if v.strip()})
    return {
        "total": len(rows),
        "with_response": sum(r["response_found"] == "yes" for r in rows),
        "with_values": sum(bool(r["values_inside_scope"].strip()) for r in rows),
        "counts": counts,
    }


def pct(n, total):
    return 100 * n / total if total else 0.0


def write_json(q, s):
    options = VOCABULARY[q] + sorted(set(s["counts"]) - set(VOCABULARY[q]))
    data = {
        "question": f"q_{q}",
        "total_articles": s["total"],
        "responses": [
            {"option": o, "quantity": s["counts"].get(o, 0), "percentage": round(pct(s["counts"].get(o, 0), s["total"]), 2)}
            for o in options
        ],
    }
    (BASE / "analysis" / f"q_{q}_distribution.json").write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def update_section(section, s):
    t, wr, wv = s["total"], s["with_response"], s["with_values"]
    section = re.sub(r"- Total de artigos: \d+", f"- Total de artigos: {t}", section)
    section = re.sub(r"- Artigos com resposta: .*", f"- Artigos com resposta: {wr} ({pct(wr, t):.1f}%)", section)
    section = re.sub(r"- Artigos sem resposta: .*", f"- Artigos sem resposta: {t - wr} ({pct(t - wr, t):.1f}%)", section)
    section = re.sub(r"(- Artigos com (?:valores|marketplaces/platforms) identificados): .*",
                     lambda m: f"{m.group(1)}: {wv} ({pct(wv, t):.1f}%)", section)
    head = section.index("### Distribuição de Valores")
    start = section.index("\n|", head) + 1
    end = section.find("\n\n", start)
    end = len(section) if end == -1 else end
    header = section[start:end].split("\n")[:2]
    rows = [f"| {v} | {n} | {pct(n, t):.1f}% |" for v, n in sorted(s["counts"].items(), key=lambda x: (-x[1], x[0]))]
    return section[:start] + "\n".join(header + rows) + section[end:]


def update_statistics(stats):
    path = BASE / "STATISTICS.md"
    text = path.read_text(encoding="utf-8")
    totals = {s["total"] for s in stats.values()}
    assert len(totals) == 1
    total = totals.pop()
    text = re.sub(r"\*\*Total de artigos analisados:\*\* \d+", f"**Total de artigos analisados:** {total}", text)
    text = re.sub(r"\*\*Última atualização:\*\* .*",
                  f"**Última atualização:** {date.today().isoformat()} (tabelas regeneradas a partir dos CSVs por `generate_distributions.py`)", text)
    parts = re.split(r"(?m)^(?=## Questão )", text)
    for i, part in enumerate(parts):
        m = re.match(r"## Questão (\d\d)", part)
        if m and m.group(1) in stats:
            nxt = part.find("\n## Insights Gerais")
            if nxt != -1:
                parts[i] = update_section(part[:nxt], stats[m.group(1)]) + part[nxt:]
            else:
                parts[i] = update_section(part, stats[m.group(1)])
    text = "".join(parts)

    def coverage(m):
        s = stats[m.group(1)]
        return f"| Q{m.group(1)} | {pct(s['with_response'], s['total']):.1f}% |"
    text = re.sub(r"\| Q(\d\d) \| \d+\.\d% \|", coverage, text)
    path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    stats = {q: analyze(q) for q in VOCABULARY}
    for q, s in stats.items():
        write_json(q, s)
    update_statistics(stats)
    for q, s in stats.items():
        top = ", ".join(f"{v} {n}" for v, n in s["counts"].most_common(3))
        print(f"Q{q}: N={s['total']}, with response={s['with_response']}; {top}")
