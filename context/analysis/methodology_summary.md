# SLR Methodology Summary

## Study Scope

- **Time period**: 2014-2024 (10 years)
- **Databases**: ACM Digital Library, IEEE Xplore, Scopus
- **Initial results**: 2,889 papers
- **After deduplication**: 2,673 papers
- **After screening**: 312 potentially relevant
- **After quality assessment**: **67 papers included**

**Source**: Article methodology section and repository structure

## Data Extraction

### Extraction Questions
- **Total**: 33 questions
- **Closed-ended**: 12 questions (categorical responses)
- **Open-ended**: 21 questions (qualitative textual responses)

**Source**: `context/extraction_questions/overview.md`

### Response Rates
- **100% response rate**: EQ01, EQ02, EQ03, EQ04, EQ08, EQ16, EQ21-EQ27, EQ29, EQ30, EQ32, EQ33
- **High response rate (90-99%)**: EQ05, EQ06, EQ07, EQ09, EQ12, EQ14, EQ18, EQ20, EQ28, EQ31
- **Medium response rate (50-89%)**: EQ10, EQ13, EQ15, EQ17, EQ19
- **Low response rate (<50%)**: EQ11 (37.3%), EQ15 (38.8%)

## Coding Scheme

- **Total codes**: 61
- **Classes**: 9
- **Subclasses**: 35
- **Quote classifications**: 4,630

**Source**: `context/coding_scheme/overview.md`

## Analysis Process

1. **Data extraction**: 33 questions × 67 papers = 2,211 extractions
2. **Quantitative analysis**: Closed-ended questions → distributions and statistics
3. **Qualitative analysis**: Open-ended questions → codes and classifications
4. **Synthesis**: Integration of quantitative and qualitative findings

**Source**: Repository structure and analysis files

## Key Statistics

See `context/analysis/key_findings.md` for detailed statistics.

## Data Sources

- **Raw data**: `raw_data/*.json` (67 files)
- **Closed-ended**: `by_closed_ended_question/question_XX.csv`
- **Open-ended**: `by_open_ended_question/question_XX.json`
- **Classifications**: `by_open_ended_question/analysis/quotes_classification/`
- **Statistics**: `by_closed_ended_question/STATISTICS.md`

