# Coding Scheme Overview

## Summary

**Total codes**: 61  
**Classes**: 9  
**Subclasses**: 35  
**Total quote classifications**: 4,630

**Source**: `by_open_ended_question/analysis/codes_config.json`  
**Count report**: `by_open_ended_question/analysis/CODES_COUNT_REPORT.md`  
**Hierarchy**: `by_open_ended_question/analysis/code_hierarchy/`

## Code Structure

### 9 Classes

1. **Business model characteristics** (2,290 quotes, 21 codes)
   - Subclasses: Value creation, Delivery model, Revenue model, Pricing strategy, Value proposition, Value delivery, Model type, Customer retention, Cost structure

2. **Market positioning** (990 quotes, 10 codes)
   - Subclasses: Industry focus, Customer type, Customer segments, Geographic scope

3. **Success factors** (358 quotes, 5 codes)
   - Subclasses: Relationship management, Growth strategy, Organizational capability, Quality management, Strategic approach

4. **Company characteristics** (221 quotes, 2 codes)
   - Subclasses: Company size, Company maturity

5. **Technical architecture** (203 quotes, 7 codes)
   - Subclasses: Infrastructure, Software architecture, Access model

6. **Model maturity** (188 quotes, 3 codes)
   - Subclasses: Maturity level

7. **Implementation challenges** (159 quotes, 6 codes)
   - Subclasses: Customer barriers, Financial impact, Ecosystem impact, Operational impact

8. **Future trends** (139 quotes, 3 codes)
   - Subclasses: Technology impact, Growth expectations, Market development

9. **Mitigation strategies** (82 quotes, 4 codes)
   - Subclasses: Pricing solutions, Transition approach, Implementation approach, Partner support

## Top 10 Codes by Frequency

1. **Platform business model** - 391 mentions
2. **SaaS (Software as a Service)** - 289 mentions
3. **Mobile app market** - 279 mentions
4. **Freemium model** - 264 mentions
5. **Open source business model** - 188 mentions
6. **B2B business model** - 161 mentions
7. **Subscription-based pricing** - 153 mentions
8. **Cloud delivery model** - 152 mentions
9. **Service-oriented model** - 144 mentions
10. **Ecosystem management** - 138 mentions

## Classification Process

**Source**: Quotes extracted from `source_citation` fields in open-ended question JSON files

**Process**:
1. Extract quotes from 21 open-ended question files
2. Analyze quotes for themes and concepts
3. Assign codes (with class and subclass)
4. Classify each quote with appropriate codes
5. Generate classification files per question

**Classification files**: `by_open_ended_question/analysis/quotes_classification/q_XX_classification.json`

## Code Definitions

**Source**: `by_open_ended_question/analysis/codes_config.json`

Each code includes:
- `code`: Short label
- `description`: One-line meaning
- `class`: Main category
- `subclass`: Specific subcategory

## Hierarchy Files

**Location**: `by_open_ended_question/analysis/code_hierarchy/`

- `CODES_HIERARCHY_TREE.md` - Visual tree representation
- `CODES_HIERARCHY_DETAILED.md` - Detailed documentation
- `CODES_HIERARCHY_STATS.md` - Statistical breakdown
- `codes_hierarchy.json` - Machine-readable format

## Usage

- **For code definitions**: See `codes_config.json`
- **For code counts**: See `CODES_COUNT_REPORT.md`
- **For hierarchy**: See `code_hierarchy/` files
- **For classified quotes**: See `quotes_classification/` files

