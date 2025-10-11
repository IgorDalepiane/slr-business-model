#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script utilitário para gerar estatísticas de questões fechadas
Usado para atualizar o arquivo STATISTICS.md
"""

import csv
from pathlib import Path
from collections import Counter
from datetime import date

def analyze_question(question_num):
    """Analisa um CSV de questão e retorna estatísticas"""
    csv_path = Path(__file__).parent / f'question_{question_num}.csv'
    
    if not csv_path.exists():
        return None
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    total = len(rows)
    with_response = sum(1 for r in rows if r['response_found'] == 'yes')
    without_response = sum(1 for r in rows if r['response_found'] == 'no')
    with_values = sum(1 for r in rows if r['values_inside_scope'].strip())
    
    # Contar distribuição de valores
    value_counts = Counter()
    for row in rows:
        if row['values_inside_scope'].strip():
            values = [v.strip() for v in row['values_inside_scope'].split(';')]
            for v in values:
                value_counts[v] += 1
    
    return {
        'total': total,
        'with_response': with_response,
        'without_response': without_response,
        'with_values': with_values,
        'distribution': dict(value_counts)
    }

def generate_markdown_section(question_num, question_text, question_type, stats):
    """Gera seção Markdown para uma questão"""
    
    total = stats['total']
    with_response = stats['with_response']
    without_response = stats['without_response']
    with_values = stats['with_values']
    
    pct_with_response = (with_response / total * 100) if total > 0 else 0
    pct_without_response = (without_response / total * 100) if total > 0 else 0
    pct_with_values = (with_values / total * 100) if total > 0 else 0
    
    md = f"""## Questão {question_num}: [TÍTULO]

**Pergunta:** {question_text}

**Tipo:** {question_type}

### Estatísticas
- Total de artigos: {total}
- Artigos com resposta: {with_response} ({pct_with_response:.1f}%)
- Artigos sem resposta: {without_response} ({pct_without_response:.1f}%)
- Artigos com valores identificados: {with_values} ({pct_with_values:.1f}%)

### Distribuição de Valores
| Valor | Quantidade | Percentual |
|-------|------------|------------|
"""
    
    # Ordenar por quantidade (descendente)
    for value, count in sorted(stats['distribution'].items(), key=lambda x: -x[1]):
        pct = (count / total * 100) if total > 0 else 0
        md += f"| {value} | {count} | {pct:.1f}% |\n"
    
    md += """
**Observações:**

[ADICIONAR OBSERVAÇÕES AQUI]

---

"""
    
    return md

def print_stats_summary(question_num):
    """Imprime resumo de estatísticas no console"""
    stats = analyze_question(question_num)
    
    if not stats:
        print(f"❌ Arquivo question_{question_num}.csv não encontrado")
        return
    
    print(f"\n=== Questão {question_num} ===")
    print(f"Total: {stats['total']}")
    print(f"Com resposta: {stats['with_response']} ({stats['with_response']/stats['total']*100:.1f}%)")
    print(f"Com valores: {stats['with_values']} ({stats['with_values']/stats['total']*100:.1f}%)")
    print(f"\nTop 5 valores:")
    for value, count in sorted(stats['distribution'].items(), key=lambda x: -x[1])[:5]:
        pct = (count / stats['total'] * 100)
        print(f"  {value}: {count} ({pct:.1f}%)")

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1:
        question_num = sys.argv[1]
        print_stats_summary(question_num)
    else:
        print("Uso: python3 generate_stats.py <question_number>")
        print("Exemplo: python3 generate_stats.py 13")
        print("\nOu importe as funções para usar em scripts:")
        print("  from generate_stats import analyze_question, generate_markdown_section")

