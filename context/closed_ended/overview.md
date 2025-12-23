# Closed-Ended Questions Context

## Overview

12 closed-ended questions with categorical responses. Data extracted from 67 papers, processed into CSV files with distributions and statistics.

**Source folder**: `by_closed_ended_question/`  
**Statistics file**: `by_closed_ended_question/STATISTICS.md`  
**Distribution files**: `by_closed_ended_question/analysis/q_XX_distribution.json`

## Questions Processed

### EQ04: Target Customer Type
- **Response rate**: 100% (67/67)
- **Type**: Single selection
- **Key findings**: B2B 53.7%, B2C 41.8%, B2B SMB 35.8%
- **Data**: `by_closed_ended_question/question_04.csv`
- **Distribution**: `by_closed_ended_question/analysis/q_04_distribution.json`

### EQ08: Product/Service Type
- **Response rate**: 100% (67/67)
- **Type**: Multiple selection
- **Key findings**: Application 89.6%, Platform 79.1%, Managed Service 35.8%
- **Data**: `by_closed_ended_question/question_08.csv`
- **Distribution**: `by_closed_ended_question/analysis/q_08_distribution.json`

### EQ09: Software Delivery/Deployment
- **Response rate**: 95.5% (64/67)
- **Type**: Multiple selection
- **Key findings**: Multi-tenant SaaS 71.6%, Mobile 40.3%, On-premises 26.9%
- **Data**: `by_closed_ended_question/question_09.csv`
- **Distribution**: `by_closed_ended_question/analysis/q_09_distribution.json`

### EQ10: Intellectual Property Regime
- **Response rate**: 50.7% (34/67)
- **Type**: Single selection
- **Key findings**: Proprietary 37.3% (when specified), Permissive Open Source 7.5%
- **Data**: `by_closed_ended_question/question_10.csv`
- **Distribution**: `by_closed_ended_question/analysis/q_10_distribution.json`

### EQ12: Revenue Sources
- **Response rate**: 95.5% (64/67)
- **Type**: Multiple selection
- **Key findings**: Subscription 76.1%, Usage/consumption 41.8%, Transaction 32.8%
- **Data**: `by_closed_ended_question/question_12.csv`
- **Distribution**: `by_closed_ended_question/analysis/q_12_distribution.json`

### EQ13: Base Pricing Unit
- **Response rate**: 82.1% (55/67)
- **Type**: Single selection
- **Key findings**: User/seat 32.8%, Transactions 19.4%, Computing time 13.4%
- **Data**: `by_closed_ended_question/question_13.csv`
- **Distribution**: `by_closed_ended_question/analysis/q_13_distribution.json`

### EQ14: Price Presentation Structure
- **Response rate**: 88.1% (59/67)
- **Type**: Multiple selection
- **Key findings**: Freemium 52.7%, Tiers/Plans 41.8%, Pay-as-you-go 41.8%
- **Data**: `by_closed_ended_question/question_14.csv`
- **Distribution**: `by_closed_ended_question/analysis/q_14_distribution.json`

### EQ16: Company Role in Ecosystem
- **Response rate**: 100% (67/67)
- **Type**: Single selection
- **Key findings**: Standalone product 49.3%, Two-sided platform 46.3%, Marketplace 13.4%
- **Data**: `by_closed_ended_question/question_16.csv`
- **Distribution**: `by_closed_ended_question/analysis/q_16_distribution.json`

### EQ17: Network Effect Type
- **Response rate**: 82.1% (55/67)
- **Type**: Single selection
- **Key findings**: Direct 35.8%, Cross-sided 31.3%, Data-driven 22.4%
- **Data**: `by_closed_ended_question/question_17.csv`
- **Distribution**: `by_closed_ended_question/analysis/q_17_distribution.json`

### EQ18: Customer Acquisition Channels
- **Response rate**: 92.5% (62/67)
- **Type**: Multiple selection
- **Key findings**: Direct sales 47.8%, Product-led Growth 41.8%, Partners/channels 38.8%
- **Data**: `by_closed_ended_question/question_18.csv`
- **Distribution**: `by_closed_ended_question/analysis/q_18_distribution.json`

### EQ19: Marketplace Usage
- **Response rate**: 55.2% (37/67)
- **Type**: Yes/No + Multiple selection
- **Key findings**: Apple App Store 20.9%, Google Play 19.4%, AWS Marketplace 3.0%
- **Data**: `by_closed_ended_question/question_19.csv`
- **Distribution**: `by_closed_ended_question/analysis/q_19_distribution.json`

### EQ30: Evidence Type
- **Response rate**: 100% (67/67)
- **Type**: Single selection
- **Key findings**: Multiple cases 50.7%, Single case 20.9%, Secondary data 16.4%
- **Data**: `by_closed_ended_question/question_30.csv`
- **Distribution**: `by_closed_ended_question/analysis/q_30_distribution.json`

## Key Statistics Summary

**Highest response rates**: EQ04, EQ08, EQ16, EQ30 (100%)  
**Lowest response rates**: EQ10 (50.7%), EQ19 (55.2%)

**Most common patterns**:
- Subscription revenue: 76.1%
- Multi-tenant SaaS delivery: 71.6%
- Application product type: 89.6%
- B2B customer type: 53.7%

## Data Format

Each CSV contains:
- `article_id`, `article_title`
- `response_found` (yes/no)
- `values_inside_scope` (categorical values, semicolon-separated)
- `extracted_value` (full extracted text)
- `confidence_level`, `source_citation`

## Usage

- **For statistics**: Use distribution JSON files or STATISTICS.md
- **For article-level data**: Use CSV files
- **For detailed insights**: See STATISTICS.md for each question

