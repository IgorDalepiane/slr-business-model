# Context Repository Index

Quick reference guide to all context files organized by topic.

## Research Questions

- **`research_questions/research_questions.md`** - RQ overview and basic mapping
- **`research_questions/rq_detailed_explanations.md`** - Detailed explanations of each RQ
- **`research_questions/mapping_eq_rq.csv`** - Complete EQ→RQ mapping table
- **`research_questions/mapping_details.md`** - Detailed mapping explanations
- **`research_questions/research_questions_table.csv`** - RQ definitions table

## Extraction Questions

- **`extraction_questions/overview.md`** - All 33 EQs overview with response rates

## Closed-Ended Questions (Quantitative)

- **`closed_ended/overview.md`** - Overview of 12 closed-ended questions
- **`closed_ended/statistics_summary.md`** - Key statistics and distributions

**Source data**:
- `by_closed_ended_question/STATISTICS.md` - Complete statistics
- `by_closed_ended_question/question_XX.csv` - Article-level data
- `by_closed_ended_question/analysis/q_XX_distribution.json` - Distributions

## Open-Ended Questions (Qualitative)

- **`open_ended/overview.md`** - Overview of 21 open-ended questions

**Source data**:
- `by_open_ended_question/question_XX.json` - Extracted responses
- `by_open_ended_question/analysis/quotes_classification/q_XX_classification.json` - Classified quotes

## Coding Scheme

- **`coding_scheme/overview.md`** - Coding scheme overview (61 codes, 9 classes)
- **`coding_scheme/codes_summary.md`** - Top codes and class breakdown

**Source data**:
- `by_open_ended_question/analysis/codes_config.json` - Code definitions
- `by_open_ended_question/analysis/CODES_COUNT_REPORT.md` - Code counts
- `by_open_ended_question/analysis/code_hierarchy/` - Hierarchy files

## Prompts and Methodology

- **`prompts/overview.md`** - Prompts overview
- **`prompts/extraction_methodology.md`** - Four-stage extraction process

**Source data**:
- `prompts/prompt_closed_ended_extraction.md` - Closed-ended extraction prompt
- `prompts/prompt_json_extraction.md` - JSON extraction prompt
- `prompts/prompt_extract_codes.md` - Code extraction prompt
- `prompts/prompt_apply_codes.md` - Code application prompt

## Analysis and Findings

- **`analysis/key_findings.md`** - Consolidated key findings
- **`analysis/methodology_summary.md`** - SLR methodology summary
- **`analysis/correlations.md`** - Cross-question patterns and correlations

## Quick Stats Reference

- **67 papers** analyzed (2014-2024)
- **10 research questions** (RQ01-RQ10)
- **33 extraction questions** (12 closed, 21 open)
- **61 codes** in 9 classes, 35 subclasses
- **4,630 quote classifications**

## Usage Tips

1. **For writing RQ sections**: Start with `research_questions/` files
2. **For statistics**: Use `closed_ended/statistics_summary.md` or `analysis/key_findings.md`
3. **For qualitative evidence**: Use `coding_scheme/` and `open_ended/` files
4. **For methodology**: Use `analysis/methodology_summary.md` and `prompts/extraction_methodology.md`
5. **For correlations**: Use `analysis/correlations.md`

## Source File References

All context files point to specific source files in the repository:
- `by_closed_ended_question/` - Quantitative data
- `by_open_ended_question/` - Qualitative data
- `raw_data/` - Original paper data
- `prompts/` - Extraction prompts

Always verify claims against source files for accuracy.


