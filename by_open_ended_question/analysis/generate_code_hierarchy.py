#!/usr/bin/env python3
"""
Generate hierarchical tree view of codes from codes_config.json
"""

import json
from collections import defaultdict
from pathlib import Path


def load_codes_config(filepath):
    """Load codes configuration from JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['codes_config']


def organize_hierarchy(codes):
    """Organize codes into hierarchical structure: class -> subclass -> codes"""
    hierarchy = defaultdict(lambda: defaultdict(list))

    for code_entry in codes:
        class_name = code_entry['class']
        subclass_name = code_entry['subclass']
        code_info = {
            'code': code_entry['code'],
            'description': code_entry['description']
        }
        hierarchy[class_name][subclass_name].append(code_info)

    # Convert to regular dict and sort
    sorted_hierarchy = {}
    for class_name in sorted(hierarchy.keys()):
        sorted_hierarchy[class_name] = {}
        for subclass_name in sorted(hierarchy[class_name].keys()):
            sorted_hierarchy[class_name][subclass_name] = sorted(
                hierarchy[class_name][subclass_name],
                key=lambda x: x['code']
            )

    return sorted_hierarchy


def generate_tree_text(hierarchy):
    """Generate text-based tree visualization"""
    lines = []
    lines.append("# Hierarchical Code Structure")
    lines.append("")
    lines.append("```")

    class_items = list(hierarchy.items())
    for class_idx, (class_name, subclasses) in enumerate(class_items):
        is_last_class = class_idx == len(class_items) - 1
        class_prefix = "└── " if is_last_class else "├── "
        lines.append(f"{class_prefix}{class_name}")

        subclass_items = list(subclasses.items())
        for subclass_idx, (subclass_name, codes) in enumerate(subclass_items):
            is_last_subclass = subclass_idx == len(subclass_items) - 1

            if is_last_class:
                subclass_prefix = "    └── "
                code_prefix_base = "        "
            else:
                subclass_prefix = "│   └── " if is_last_subclass else "│   ├── "
                code_prefix_base = "│       " if is_last_subclass else "│   │   "

            lines.append(f"{subclass_prefix}{subclass_name}")

            for code_idx, code_info in enumerate(codes):
                is_last_code = code_idx == len(codes) - 1

                if is_last_subclass:
                    if is_last_class:
                        code_symbol = "└── " if is_last_code else "├── "
                    else:
                        code_symbol = "    └── " if is_last_code else "    ├── "
                else:
                    code_symbol = "└── " if is_last_code else "├── "

                lines.append(f"{code_prefix_base}{code_symbol}{code_info['code']}")

    lines.append("```")
    return "\n".join(lines)


def generate_markdown_detailed(hierarchy):
    """Generate detailed markdown with descriptions"""
    lines = []
    lines.append("# Hierarchical Code Structure (Detailed)")
    lines.append("")

    for class_name, subclasses in hierarchy.items():
        lines.append(f"## {class_name}")
        lines.append("")

        for subclass_name, codes in subclasses.items():
            lines.append(f"### {subclass_name}")
            lines.append("")

            for code_info in codes:
                lines.append(f"- **{code_info['code']}**")
                lines.append(f"  - {code_info['description']}")
                lines.append("")

    return "\n".join(lines)


def generate_statistics(hierarchy):
    """Generate statistics about the code structure"""
    stats = []
    stats.append("# Code Structure Statistics")
    stats.append("")

    total_classes = len(hierarchy)
    total_subclasses = sum(len(subclasses) for subclasses in hierarchy.values())
    total_codes = sum(
        len(codes)
        for subclasses in hierarchy.values()
        for codes in subclasses.values()
    )

    stats.append(f"- **Total Classes**: {total_classes}")
    stats.append(f"- **Total Subclasses**: {total_subclasses}")
    stats.append(f"- **Total Codes**: {total_codes}")
    stats.append("")

    stats.append("## Distribution by Class")
    stats.append("")

    for class_name, subclasses in sorted(hierarchy.items()):
        num_subclasses = len(subclasses)
        num_codes = sum(len(codes) for codes in subclasses.values())
        stats.append(f"### {class_name}")
        stats.append(f"- Subclasses: {num_subclasses}")
        stats.append(f"- Codes: {num_codes}")
        stats.append("")

        for subclass_name, codes in sorted(subclasses.items()):
            stats.append(f"  - **{subclass_name}**: {len(codes)} codes")
        stats.append("")

    return "\n".join(stats)


def main():
    # Define paths
    base_dir = Path(__file__).parent
    config_file = base_dir / "codes_config.json"
    output_dir = base_dir / "code_hierarchy"

    # Create output directory if it doesn't exist
    output_dir.mkdir(exist_ok=True)

    # Load and organize codes
    codes = load_codes_config(config_file)
    hierarchy = organize_hierarchy(codes)

    # Generate tree visualization
    tree_text = generate_tree_text(hierarchy)
    tree_output = output_dir / "CODES_HIERARCHY_TREE.md"
    with open(tree_output, 'w', encoding='utf-8') as f:
        f.write(tree_text)
    print(f"✓ Generated tree visualization: {tree_output}")

    # Generate detailed markdown
    detailed_markdown = generate_markdown_detailed(hierarchy)
    detailed_output = output_dir / "CODES_HIERARCHY_DETAILED.md"
    with open(detailed_output, 'w', encoding='utf-8') as f:
        f.write(detailed_markdown)
    print(f"✓ Generated detailed hierarchy: {detailed_output}")

    # Generate statistics
    statistics = generate_statistics(hierarchy)
    stats_output = output_dir / "CODES_HIERARCHY_STATS.md"
    with open(stats_output, 'w', encoding='utf-8') as f:
        f.write(statistics)
    print(f"✓ Generated statistics: {stats_output}")

    # Also save hierarchy as JSON for programmatic access
    hierarchy_json = output_dir / "codes_hierarchy.json"
    with open(hierarchy_json, 'w', encoding='utf-8') as f:
        json.dump(hierarchy, f, indent=2, ensure_ascii=False)
    print(f"✓ Generated hierarchy JSON: {hierarchy_json}")


if __name__ == "__main__":
    main()
