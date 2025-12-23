# Open-Ended Questions Context

## Overview

21 open-ended questions with qualitative textual responses. Data extracted from 67 papers, stored as JSON files with quotes and classifications.

**Source folder**: `by_open_ended_question/`  
**Data files**: `by_open_ended_question/question_XX.json`  
**Classification files**: `by_open_ended_question/analysis/quotes_classification/q_XX_classification.json`

## Questions Overview

### High Response Rate (100%)
- EQ01: Name and definition (67/67)
- EQ02: Synonyms and alternative terms (67/67)
- EQ03: Vertical segment/industry (67/67)
- EQ21: Ecosystem actors and interactions (67/67)
- EQ22: Adoption motivations (67/67)
- EQ23: Success factors (67/67)
- EQ24: Prerequisites and necessary conditions (67/67)
- EQ25: Restrictions and incompatibilities (67/67)
- EQ26: Implementation challenges (67/67)
- EQ27: Mitigation practices (67/67)
- EQ29: Temporal period and maturity (67/67)
- EQ32: Variations and subtypes (67/67)
- EQ33: Future trends (67/67)

### Medium Response Rate (90-99%)
- EQ07: Specific customer segment (66/67, 98.5%)
- EQ20: Business Model Canvas elements (63/67, 94.0%)
- EQ28: Metrics and quantitative results (64/67, 95.5%)
- EQ31: Companies/products cited as examples (64/67, 95.5%)
- EQ05: Offering company size (64/67, 95.5%)
- EQ06: Geographic region (65/67, 97.0%)

### Low Response Rate (<50%)
- EQ11: Licensing restrictions (25/67, 37.3%)
- EQ15: Currency and periodicity (26/67, 38.8%)

## Data Structure

Each JSON file contains:
```json
{
  "question_metadata": {
    "question_id": "XX",
    "question_text": "...",
    "total_articles": 67,
    "articles_with_response": N
  },
  "responses_by_article": [
    {
      "article_id": "...",
      "article_title": "...",
      "extracted_value": "...",
      "source_citation": "...",
      "confidence_level": "..."
    }
  ]
}
```

## Quote Classification

**Total classifications**: 4,630 quotes classified with 61 codes

**Classification files**: `by_open_ended_question/analysis/quotes_classification/q_XX_classification.json`

Each classification file contains:
- Quotes extracted from `source_citation` fields
- Codes assigned to each quote
- Article references

## Key Questions by Category

### Model Identification
- **EQ01**: Name and definition → Used for taxonomy (RQ01, RQ09)
- **EQ02**: Synonyms and alternative terms → Terminology standardization (RQ01)

### Application Context
- **EQ03**: Vertical segment/industry → Market segmentation (RQ02)
- **EQ05**: Offering company size → Context analysis (RQ02)
- **EQ06**: Geographic region → Context analysis (RQ02)
- **EQ07**: Specific customer segment → Detailed segmentation (RQ02)

### Adoption and Success
- **EQ22**: Adoption motivations → Why models are adopted (RQ06)
- **EQ23**: Success factors → What leads to success (RQ06)
- **EQ24**: Prerequisites → Necessary conditions (RQ03, RQ06)
- **EQ25**: Restrictions → Limiting conditions (RQ06)

### Challenges and Mitigation
- **EQ26**: Implementation challenges → Problems faced (RQ07)
- **EQ27**: Mitigation practices → Solutions used (RQ07)

### Temporal and Evidence
- **EQ29**: Temporal period and maturity → Evolution analysis (RQ08)
- **EQ31**: Companies/products examples → Evidence and evolution (RQ08, RQ10)
- **EQ33**: Future trends → Projections (RQ08)

## Usage

- **For quotes**: Read JSON files directly
- **For classified quotes**: Use classification JSON files
- **For code analysis**: See `context/coding_scheme/`

