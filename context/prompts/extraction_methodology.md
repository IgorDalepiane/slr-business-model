# Data Extraction Methodology

## Overview

Four-stage extraction process used to collect and analyze data from 67 papers.

**Source folder**: `prompts/`

## Stage 1: Initial JSON Extraction

**Prompt**: `prompts/prompt_json_extraction.md`

**Process**:
- Extract textual responses for 33 extraction questions
- Store in structured JSON format
- Include source citations for traceability

**Output**: `by_open_ended_question/question_XX.json` (21 files)

**Questions**: All 33 questions (both open and closed-ended initially extracted as JSON)

## Stage 2: Closed-Ended Processing

**Prompt**: `prompts/prompt_closed_ended_extraction.md`

**Process**:
- Process 12 closed-ended questions from JSON files
- Extract categorical values
- Create CSV with `values_inside_scope` field
- Generate distribution statistics

**Output**: 
- `by_closed_ended_question/question_XX.csv` (12 files)
- `by_closed_ended_question/analysis/q_XX_distribution.json` (11 files)
- `by_closed_ended_question/STATISTICS.md`

**Key feature**: `values_inside_scope` field filters extracted values to match valid categories

## Stage 3: Code Extraction

**Prompt**: `prompts/prompt_extract_codes.md`

**Process**:
- Analyze `source_citation` fields from open-ended questions
- Identify meaningful quotes
- Derive codes with class and subclass
- Incremental consolidation across multiple files

**Output**: `by_open_ended_question/analysis/codes_config.json`

**Result**: 61 codes in 9 classes, 35 subclasses

## Stage 4: Code Application

**Prompt**: `prompts/prompt_apply_codes.md`

**Process**:
- Read quotes from question JSON files
- Match quotes to codes from codes_config.json
- Generate classification files per question

**Output**: `by_open_ended_question/analysis/quotes_classification/q_XX_classification.json` (21 files)

**Result**: 4,630 quote classifications

## Quality Assurance

- **Preserve original values**: No modification of extracted text
- **Document decisions**: Special cases documented in STATISTICS.md
- **Traceability**: Source citations link back to original papers
- **Consistency**: Same prompts used across all papers

## Data Flow

```
raw_data/*.json
  ↓ [prompt_json_extraction.md]
by_open_ended_question/question_XX.json
  ↓ [prompt_closed_ended_extraction.md] (for 12 questions)
by_closed_ended_question/question_XX.csv
  ↓ [prompt_extract_codes.md]
by_open_ended_question/analysis/codes_config.json
  ↓ [prompt_apply_codes.md]
by_open_ended_question/analysis/quotes_classification/q_XX_classification.json
```

