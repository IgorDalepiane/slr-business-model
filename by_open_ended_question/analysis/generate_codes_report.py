#!/usr/bin/env python3
"""
Generate CODES_COUNT_REPORT.md from codes_count_report.json (output of count_codes.py).

Usage: python3 count_codes.py && python3 generate_codes_report.py
"""

import json
from collections import OrderedDict
from pathlib import Path

BASE = Path(__file__).parent


def main():
    report = json.loads((BASE / "codes_count_report.json").read_text(encoding="utf-8"))
    summary, results = report["summary"], report["results"]

    by_class = OrderedDict()
    for r in sorted(results, key=lambda r: (-r["count"], r["code"])):
        by_class.setdefault(r["class"], []).append(r)
    class_totals = {c: sum(r["count"] for r in rs) for c, rs in by_class.items()}

    lines = [
        "# Relatório de Contagem de Códigos por Quotes",
        "",
        "## Resumo Executivo",
        "",
        f"- **Total de códigos definidos**: {summary['total_codes']}",
        f"- **Códigos com quotes classificadas**: {summary['codes_with_quotes']}",
        f"- **Códigos sem quotes classificadas**: {summary['codes_without_quotes']}",
        f"- **Total de classificações**: {summary['total_classifications']}",
        "",
        "> Gerado por `generate_codes_report.py` a partir de `codes_count_report.json`. Corpus de 63 estudos primários após a correção R08 (ver `context/analysis/corpus-correction-r08.md`).",
        "",
        "---",
        "",
        "## Top 10 Códigos Mais Utilizados",
        "",
        "| # | Código | Contagem |",
        "|---|--------|----------|",
    ]
    for i, r in enumerate(sorted(results, key=lambda r: (-r["count"], r["code"]))[:10], 1):
        lines.append(f"| {i} | {r['code']} | {r['count']} |")
    lines += ["", "---", "", "## Contagem Completa por Classe", ""]
    for cls in sorted(by_class, key=lambda c: -class_totals[c]):
        lines += [
            f"### {cls} ({class_totals[cls]} quotes)",
            "",
            "| Código | Subclasse | Contagem | Descrição |",
            "|--------|-----------|----------|------------|",
        ]
        for r in by_class[cls]:
            lines.append(f"| {r['code']} | {r['subclass']} | {r['count']} | {r['description']} |")
        lines.append("")
    (BASE / "CODES_COUNT_REPORT.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
