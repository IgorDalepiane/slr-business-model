#!/usr/bin/env python3
"""
Script to count the number of quotes classified with each code across all classification files.
"""

import json
import os
from pathlib import Path
from collections import defaultdict

def main():
    # Define paths
    base_dir = Path(__file__).parent
    codes_config_path = base_dir / "codes_config.json"
    classifications_dir = base_dir / "quotes_classification"

    # Load codes configuration
    with open(codes_config_path, 'r', encoding='utf-8') as f:
        codes_config = json.load(f)

    # Initialize counter for each code
    code_counts = defaultdict(int)

    # Get all classification files
    classification_files = sorted(classifications_dir.glob("q_*_classification.json"))

    print(f"Processing {len(classification_files)} classification files...\n")

    # Process each classification file
    for file_path in classification_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Count codes in this file
        if 'qualitative_analysis' in data:
            for item in data['qualitative_analysis']:
                if 'assigned_codes' in item:
                    for code in item['assigned_codes']:
                        code_counts[code] += 1

    # Prepare results
    results = []
    for config in codes_config['codes_config']:
        code = config['code']
        count = code_counts.get(code, 0)
        results.append({
            'code': code,
            'count': count,
            'class': config['class'],
            'subclass': config['subclass'],
            'description': config['description']
        })

    # Sort by count (descending) then by code name
    results.sort(key=lambda x: (-x['count'], x['code']))

    # Display results
    print("=" * 100)
    print("CONTAGEM DE QUOTES POR CÓDIGO")
    print("=" * 100)
    print()

    # Group by class
    current_class = None
    total_quotes = 0

    for result in results:
        if result['class'] != current_class:
            if current_class is not None:
                print()
            current_class = result['class']
            print(f"\n{'=' * 100}")
            print(f"CLASSE: {current_class}")
            print(f"{'=' * 100}")

        print(f"\n{result['code']}")
        print(f"  Subclasse: {result['subclass']}")
        print(f"  Descrição: {result['description']}")
        print(f"  → Quotes classificadas: {result['count']}")

        total_quotes += result['count']

    print()
    print("=" * 100)
    print(f"TOTAL DE CLASSIFICAÇÕES: {total_quotes}")
    print("=" * 100)
    print()

    # Summary statistics
    codes_with_quotes = sum(1 for r in results if r['count'] > 0)
    codes_without_quotes = sum(1 for r in results if r['count'] == 0)

    print("\nESTATÍSTICAS:")
    print(f"  - Total de códigos definidos: {len(results)}")
    print(f"  - Códigos com quotes classificadas: {codes_with_quotes}")
    print(f"  - Códigos sem quotes classificadas: {codes_without_quotes}")
    print(f"  - Total de classificações: {total_quotes}")

    # Top 10 codes
    print("\n" + "=" * 100)
    print("TOP 10 CÓDIGOS MAIS UTILIZADOS")
    print("=" * 100)
    for i, result in enumerate(results[:10], 1):
        print(f"{i:2d}. {result['code']:50s} → {result['count']:4d} quotes")

    # Export to JSON
    output_file = base_dir / "codes_count_report.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({
            'summary': {
                'total_codes': len(results),
                'codes_with_quotes': codes_with_quotes,
                'codes_without_quotes': codes_without_quotes,
                'total_classifications': total_quotes
            },
            'results': results
        }, f, indent=2, ensure_ascii=False)

    print(f"\n✓ Relatório exportado para: {output_file}")

if __name__ == "__main__":
    main()
