# Prompts Used in Research

## Overview

Prompts used during data extraction and analysis phases of the SLR.

**Source folder**: `prompts/`

## Prompts

### 1. Closed-Ended Extraction
**File**: `prompts/prompt_closed_ended_extraction.md`

**Purpose**: Extract categorical data from papers for 12 closed-ended questions

**Process**:
- Read JSON files from `raw_data/`
- Extract values for specific question
- Create CSV with `values_inside_scope` field
- Update STATISTICS.md

**Output**: CSV files in `by_closed_ended_question/question_XX.csv`

**Questions covered**: EQ04, EQ08, EQ09, EQ10, EQ12, EQ13, EQ14, EQ16, EQ17, EQ18, EQ19, EQ30

### 2. Open-Ended JSON Extraction
**File**: `prompts/prompt_json_extraction.md`

**Purpose**: Extract textual responses for 21 open-ended questions

**Process**:
- Extract full text responses from papers
- Store in JSON format with metadata
- Include source citations

**Output**: JSON files in `by_open_ended_question/question_XX.json`

### 3. Code Extraction
**File**: `prompts/prompt_extract_codes.md`

**Purpose**: Extract qualitative codes from open-ended question responses

**Process**:
- Analyze `source_citation` fields
- Identify meaningful quotes
- Derive codes with class and subclass
- Incremental consolidation

**Output**: `by_open_ended_question/analysis/codes_config.json`

### 4. Code Application
**File**: `prompts/prompt_apply_codes.md`

**Purpose**: Classify quotes with extracted codes

**Process**:
- Read quotes from question JSON files
- Assign appropriate codes
- Generate classification files

**Output**: `by_open_ended_question/analysis/quotes_classification/q_XX_classification.json`

## Prompt Workflow

1. **Initial extraction**: `prompt_json_extraction.md` → JSON files
2. **Closed-ended processing**: `prompt_closed_ended_extraction.md` → CSV files
3. **Code extraction**: `prompt_extract_codes.md` → codes_config.json
4. **Code application**: `prompt_apply_codes.md` → classification files

## Key Instructions

- Preserve original values from JSONs
- Document decisions in STATISTICS.md
- Maintain consistency across questions
- Support incremental processing


