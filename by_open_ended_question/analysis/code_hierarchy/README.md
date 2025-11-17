# Code Hierarchy Documentation

This directory contains the hierarchical organization of codes extracted from the systematic literature review on software business models.

## Files

### 📊 Visualization Files

- **`CODES_HIERARCHY_TREE.md`** - Visual tree representation of the code hierarchy

  - ASCII tree showing class → subclass → code structure
  - Easy to understand at a glance

- **`CODES_HIERARCHY_DETAILED.md`** - Detailed markdown documentation

  - Organized by class and subclass
  - Includes full descriptions for each code
  - Best for reading and understanding code definitions

- **`CODES_HIERARCHY_STATS.md`** - Statistical analysis

  - Total counts of classes, subclasses, and codes
  - Distribution of codes across classes
  - Breakdown by subclass

- **`codes_hierarchy.json`** - Machine-readable format
  - JSON structure for programmatic access
  - Organized as: class → subclass → [codes]
  - Use this for scripts and analysis tools

## Hierarchy Structure

The codes are organized in a three-level hierarchy:

1. **Class** (9 total)

   - Top-level categories (e.g., "Business model characteristics", "Technical architecture")

2. **Subclass** (35 total)

   - Mid-level categories within each class (e.g., "Pricing strategy", "Infrastructure")

3. **Code** (61 total)
   - Specific concepts with descriptions (e.g., "Subscription-based pricing", "Multi-tenant architecture")

## Usage

### Regenerating Files

To regenerate all hierarchy files, run:

```bash
cd /path/to/analysis
python3 generate_code_hierarchy.py
```

The script reads from `codes_config.json` in the parent directory and outputs all files to this `code_hierarchy/` directory.

## Quick Statistics

- **9** Classes
- **35** Subclasses
- **61** Codes

### Largest Classes

1. **Business model characteristics** - 21 codes
2. **Market positioning** - 10 codes
3. **Technical architecture** - 7 codes
4. **Implementation challenges** - 6 codes
5. **Success factors** - 5 codes
