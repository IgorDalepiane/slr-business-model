# Corpus Correction R08: Duplicate Records and Out-of-Window Study

**Status:** Applied (Phase 2). The proposal (Sections 1 to 8) was approved on 2026-10-19 with the adjustments recorded in Section 9, which also gives the final values. Sections 2.3 and 6 keep the proposal as written, annotated where the approval changed it.
**Date:** 2026-10-19 (proposal and approval); applied 2026-10-19 and 2026-10-20
**Related items:** R08 (SMS corpus with duplicates and an out-of-window study) and R24 (PRISMA 2020 flow diagram) in `sbm-ontology-dissertation/docs/defense/revision-tracker.md`.

Page references to the articles (p. N) follow the `=== PÁGINA N ===` markers in `raw_articles_txt/`, i.e., PDF pages. Line numbers (l.) refer to the same `.txt` file.

---

## 1. Facts and scope

### 1.1 Records to remove

| IP (current) | article_id | Study | Reason | Kept as |
|---|---|---|---|---|
| IP62 | 190655721 | Wu, Wortmann and Tan (2014), DOI 10.1109/INTECH.2014.6927738 | Duplicate of IP01 (190638760): same DOI, identical full text except the IEEE Xplore download watermark | IP01 |
| IP55 | 190655555 | Ojala (2014), DOI 10.1109/CloudCom.2014.27 | Duplicate of IP02 (190638781) | IP02 |
| IP47 | 190655386 | Hedman and Xiao (2016), DOI 10.1109/HICSS.2016.494 | Duplicate of IP03 (190638871) | IP03 |
| IP63 | 190655747 | Hannola et al., IEEM 2013, DOI 10.1109/IEEM.2013.6962664 | Published in 2013 (PDF footer `978-1-4799-0986-5/13/$31.00 ©2013 IEEE`, running header "Proceedings of the 2013 IEEE IEEM"; conference held 10 to 13 December 2013), outside the 2014 to 2024 window. The Crossref record of the DOI was only created in December 2014, which probably explains why it passed the date filter. | removed |

The appendix order of IP codes is exactly the ascending order of `article_id` (verified for all 67 rows). The duplicates therefore come from two different import batches: the three lowest IDs (1906387xx/1906388xx, together with IP04, 190638976) and the main batch (19065xxxx).

### 1.2 Which copy is kept

**Proposal:** keep the `article_id` of copy 1 (190638760, 190638781, 190638871) and remove copy 2. Reasons:

1. Copy 1 has much richer coded evidence (66, 57 and 53 classified quotes, against 19, 22 and 28 for copy 2).
2. IP01 to IP46 keep their numbers after renumbering; only the tail of the appendix shifts (Section 7.4).
3. The kept record receives one revised extraction (Sections 2 and 3), so the choice of ID has no effect on the data content.

### 1.3 Venue metadata

- IP55 row says "CloudCom 2015, pp. 863--868"; the correct venue is the 2014 IEEE 6th CloudCom (the row disappears; its page range is moved to IP02).
- IP62 row says "INTECH 2014 and FGCT 2014, pp. 152--157"; the correct venue is INTECH 2014 (the row disappears; its page range is moved to IP01).
- IP47 row page range (pp. 3989--3998) is moved to IP03.
- Additional finding (not in R08): IP53 (`kiss2015business`) says "Winter Simulation Conference 2016", but the `.bib` and the DOI (10.1109/WSC.2015.7408373) give the 2015 WSC. Proposed fix: "2015 Winter Simulation Conference (WSC)".

---

## 2. Closed-ended questions: divergences and proposed values

### 2.1 Comparison method

All 12 closed-ended questions (Q04, Q08, Q09, Q10, Q12, Q13, Q14, Q16, Q17, Q18, Q19, Q30) were compared for each pair, both on `values_inside_scope` and on `extracted_value`. The CSVs in `by_closed_ended_question/` were first checked against `raw_data/`: `extracted_value` and `response_found` match the JSONs in all 804 rows.

Result: **16 divergences**. Fifteen are visible in `values_inside_scope`; one (Hedman, Q17) is hidden because the CSV of copy 2 mapped the extracted value "Others (community-based, open innovation)" to `Data`.

### 2.2 Criteria applied

The decisions apply the vocabulary of `prompts/prompt_closed_ended_extraction.md` and the question definitions of `prompts/prompt_json_extraction.md`:

- **Single-selection questions** (Q04, Q10, Q13, Q16, Q17, Q30): one value from the controlled vocabulary, the one most emphasized in the article; a second value only when the article gives both explicit and comparable emphasis.
- **Multiple-selection questions** (Q08, Q09, Q12, Q14, Q18): all values explicitly supported by the article.
- **Absent information**: `response_found = false`, `extracted_value = "not reported"`, empty `values_inside_scope` ("mark as not reported if truly absent").
- **Q13**: a generic subscription or usage model is a revenue model, not a pricing unit; such cases stay empty (convention already documented in `STATISTICS.md`, cases 190655382 and 190655589).
- **Q19**: a platform counts only if it is used to distribute or sell software (criterion in the closed-ended prompt).
- **Q04**: every row with `B2B SMB` also carries `B2B` (convention verified in all 67 rows).
- `values_inside_scope` must remain a subset of the revised `extracted_value`.

### 2.3 Decision table

| # | Study | EQ | Copy 1 | Copy 2 | Proposed | Article evidence (page) | Justification |
|---|---|---|---|---|---|---|---|
| 1 | Wu | Q04 | B2B SMB; B2B; Mid-market; Enterprise | B2B SMB; B2B | **B2B SMB; B2B; Enterprise** | p. 2: "small and medium enterprises have been the most aggressive adopters. Likewise, large corporations are equally attracted to the idea of acquiring software services on demand" | SMEs and large corporations are both named with comparable emphasis; "Mid-market" has no textual support. |
| 2 | Wu | Q10 | not reported | Proprietary | **Proprietary** | p. 1: "Traditionally, software license refers to an agreement granting a licensee the rights to utilize packaged software"; p. 6: "a comprehensive categorization of pricing components that can be leveraged by SaaS vendors in constructing software licenses" | The whole article is about vendors licensing their own SaaS to clients; no open source is mentioned. Same criterion that gave Proprietary to Ojala (190638781) from its licensing statements. Confidence: medium. |
| 3 | Wu | Q12 | Subscription; Support; Usage/consumption; Transaction; Others | Subscription; Support; Usage/consumption | **Subscription; Usage/consumption; Support; Others** | p. 3: "Monthly subscription fees are the most popular pricing model"; p. 3: "software vendors charge clients for what they use"; p. 3: "helpdesk support, software setup & training, software configuration and integration ... while others such as backup and security ... are offered as purchasable services" | "Transaction" in the vocabulary means transaction fees or commissions; here "transaction based" (Table I, p. 2) is a usage metric, already covered by Usage/consumption and by Q13. Backup and security sold as add-on services are kept as Others. |
| 4 | Wu | Q13 | User/seat; Transactions; Computing time; Storage | User/seat | **User/seat** | p. 5: "Vendors from cluster one, making up 67% of our sample, prefer the user-based pricing component"; p. 6: "usage-independent based pricing components were used by about half of SaaS vendors while usage-dependent based pricing components were used by one-third" | Single selection: Table I lists every unit as part of a framework, but the empirical results emphasize user-based pricing. |
| 5 | Wu | Q14 | Tiers/Plans; Prepaid credits; Pay-as-you-go; Custom negotiation | Pay-as-you-go; Tiers/Plans | **Tiers/Plans; Pay-as-you-go; Prepaid credits** | p. 3: "a vendor may offer different pricing plans for an application according to certain product-related criteria"; p. 3: "software vendors encourage clients to prepay their subscriptions. Sometimes software vendors offer some degree of discount for those bulk payment clients"; p. 6: "charge the client only for what he uses" | Prepayment with bulk discount is explicit. "Custom negotiation" is not supported: organization/region-based pricing (Table I) is price discrimination by fixed criteria, and the article never mentions negotiation. |
| 6 | Wu | Q17 | Direct | None | **not reported** | p. 2: "retain a sizeable pool of clients and achieve economies of scale"; p. 5: "vendors are supposed to expand clients base continuously in order to leverage on economy of scale" | Copy 1 read economies of scale (a supply-side effect) as a direct network effect; nothing in the article says that the value for a user grows with the number of users. Copy 2 cited a multi-tenancy passage that does not state absence either. The article does not discuss network effects at all, so the prompt rule for absent information applies. |
| 7 | Wu | Q18 | not reported | Direct sales | **not reported** | p. 3: "The pricing data source is obtained through our examination of each SaaS vendor's website" | Copy 2's citation describes the study's data collection, not how vendors acquire customers. The article does not discuss acquisition channels. |
| 8 | Wu | Q19 | not reported | Others (New Cloud Computing Showplace) | **not reported** | p. 3: "the vendor list provided by the New Cloud Computing Showplace website ... this website is regarded as the vendor-independent, resource center of industrial best practices" | The site is a vendor directory used as a sampling frame, not a platform that distributes or sells software. |
| 9 | Wu | Q30 | Multiple cases; Secondary data analysis; Literature review | Secondary data analysis | **Secondary data analysis** | p. 3: "we conducted content analysis to investigate the software licensing practices for SaaS. The pricing data source is obtained through our examination of each SaaS vendor's website"; p. 4: "we performed cluster analyses on these pricing data" | Content and cluster analysis of public website data from 353 vendors; there are no case studies, and the short background section is not a literature review. |
| 10 | Ojala | Q14 | Tiers/Plans; Custom negotiation; Annual contract | the same + Pay-as-you-go | **Tiers/Plans; Custom negotiation; Annual contract** | p. 4: "In practice, we could also use a pay-per-use model ... However, network operators have become accustomed to using rental models and that is why we have to use one too"; p. 3: "this was negotiated with each customer separately"; p. 4: "The initial rental agreement was for three years"; p. 4: "We have certain stages according to which we price" | The article states explicitly that pay-per-use is not used. |
| 11 | Ojala | Q17 | Direct | Data | **Direct (more users = more value)**. *Changed on approval to* **not reported** (Section 9.1) | p. 2: "Renting can also increase the positive network externality effect, owing to the lower initial costs ... The low costs increase the number of customers, and consequently increase the information available in the market regarding the product. Overall, this decreases customers' search costs" | More customers lower the search costs of other customers: a same-side effect. The product itself does not improve with data, so "Data" does not fit. Confidence: low (the passage is in the literature review section). |
| 12 | Ojala | Q18 | Direct sales; Partners/channels | Direct sales | **Direct sales; Partners/channels** | p. 3: "The network operators operate the platform and deliver games to players' set-top boxes or to PCs through their broadband network"; p. 4: "Because the content is delivered through network operators to game players, the network operator determines the revenue model used"; p. 6: "customers or delivery channels are the main driving force" | Firm B reaches customers through network operators and a portal; both copies agree on Direct sales. |
| 13 | Hedman | Q08 | Application; Managed Service | Application | **Application** | p. 5: "The second division of ERP Co provides BPO (business process outsourcing) services ... In this study, we will only focus on the software SMB division of ERP Co." | The only service-like offering (BPO) is explicitly outside the scope of the study; copy 1's citations support Application only. |
| 14 | Hedman | Q12 | Subscription; Perpetual license | Subscription | **Perpetual license; Subscription** | p. 5: "up to 50% of the initial ERP Co license fees do go to VAR"; p. 6: "the so-called hybrid model where both ends (SaaS-based and on-premise products) were handled in equal terms"; p. 7: "the upfront perpetual licenses fees would be replaced by long-term flowing of subscription fee" | Under the hybrid strategy, ERP Co keeps selling on-premise licenses alongside SaaS subscriptions. |
| 15 | Hedman | Q13 | not reported | Others; User/seat | **not reported** | p. 6: "the pay-as-you-go or subscription-based pricing model associated with cloud and SaaS" | No pricing unit is mentioned. Copy 2's own `extracted_value` was "Others (subscription-based, not specified per user/seat or usage metric)"; the `User/seat` in its CSV row was a parsing error. |
| 16 | Hedman | Q17 | Data | Others (community-based, open innovation); CSV mapped it to Data | **not reported** | p. 3: "many of the cloud vendors mentioned above operate around a user community where open innovation is flourishing, suggesting a paradigm shift from treating customers as value exchangers to value co-creators" | Both copies cite the same general remark about cloud vendors (Salesforce, Google, and others), not about ERP Co, and it does not describe value growing with users or data. |

### 2.4 Net effect per study

| Study | Values removed (relative to copy 1) | Values added (relative to copy 1) |
|---|---|---|
| Wu (IP01) | Q04 Mid-market; Q12 Transaction; Q13 Transactions, Computing time, Storage; Q14 Custom negotiation; Q17 Direct; Q30 Multiple cases, Literature review | Q10 Proprietary |
| Ojala (IP02) | none in the proposal; Q17 Direct after the approval adjustment (Section 9.1) | none |
| Hedman (IP03) | Q08 Managed Service; Q17 Data | none |

---

## 3. Open-ended questions and coded quotes

### 3.1 Merge rule (proposal)

1. **Responses** (`raw_data/*.json` and `by_open_ended_question/question_XX.json`): `extracted_value` of the kept record becomes "copy 1 | copy 2" when the two texts differ; `synonyms_found` and `source_citation` are merged as a union without repeated items; `response_found` is true when at least one copy found an answer that the article supports (see 3.3).
2. **Coded quotes** (`analysis/quotes_classification/q_XX_classification.json`): union of the two copies under the kept `article_id`. A copy-2 quote counts as repeated, and is not added, when its normalized text is equal to, contained in, or contains a copy-1 quote of the same question, or when at least 90% of the shorter quote is covered by matching blocks (this catches the same passage cut with different ellipses). For a repeated quote the longer text is kept, and copy-2 codes are added only if no overlapping copy-1 quote of the same question already carries them (avoids counting the same evidence twice).
3. Partial overlaps below the 90% threshold are kept as separate quotes, because they cover different text (Wu Q03, Q22; Hedman Q20, Q31, Q33; Ojala Q32 were inspected).

### 3.2 Summary per pair

| Pair | Quotes copy 1 | Quotes copy 2 | Repeated | Merged quotes | Code assignments (copy 1 + copy 2) |
|---|---|---|---|---|---|
| Wu | 66 | 19 | 12 | 73 | 156 + 53 = 209 |
| Ojala | 57 | 22 | 10 | 69 | 131 + 58 = 189 |
| Hedman | 53 | 28 | 10 | 71 | 127 + 75 = 202 |

Totals: 1,859 quotes before; 1,859 minus 17 (IP63) minus 69 (copy 2) plus 37 (non-repeated copy-2 quotes) = **1,810 quotes after**. Code assignments: 4,630 before, **4,522 after** (4,515 if option 3.3(b) is approved).

The full per-question comparison is in Appendix A.

### 3.3 Questions where only one copy found an answer

| Study | EQ | Copy 1 | Copy 2 | Proposed | Reason |
|---|---|---|---|---|---|
| Wu | Q11 (licensing restrictions) | found | not reported | found | p. 2: "the 'perpetual' usage license fee is no longer applicable and clients are charged for only what they have utilized" supports a licensing restriction affecting monetization. |
| Ojala | Q11 | not reported | found | found | p. 4: "some customers had an IT policy that did not allow installation of any software outside their own internal data center" (licensing model constrained by customer policy). |
| Ojala | Q15 (currency and billing periodicity) | found | not reported | found | p. 4: "SaaS where there is a price per user per month". |
| Hedman | Q15 | not reported | found | **(b) not reported** | Copy 2 cites revenue figures ("80 million Euro", "800 million NOK") that are company figures, not billing currency, and "periodic subscription fee" without a period. |
| Wu | Q31 (companies or products cited) | found | not reported | **(b) not reported** | Copy 1 cites the New Cloud Computing Showplace directory and application categories (CRM, collaboration); neither is a company or product used as an example of the business model. |

Decision needed: **(a)** plain union, as requested (Hedman Q15 and Wu Q31 stay "found", with their 3 quotes); or **(b)** union with verification, which marks those two answers as not reported and drops their 3 quotes (codes affected: SaaS −2, B2B business model −1, Cross-industry applications −1, Cloud delivery model −1, Subscription-based pricing −1, Revenue stream transformation −1). Recommendation: **(b)**, because it applies the same "supported by the article" test used for the closed questions. **Approved: (b).**

### 3.4 Effect on the 61-code scheme

- **No code disappears.** All 61 codes keep at least one quote after the correction.
- **Codes that exist in a pair only because of copy 2:** `Value-based pricing` (Ojala Q22) and `High switching costs` (Hedman Q25 and Q26). With the union they are preserved for the kept study, so their study-level support does not change.
- **Codes that depend only on IP63:** none. IP63 contributes 39 code assignments (B2B business model 9, SaaS 8, Service-oriented model 3, Cross-industry applications 3, Data-driven monetization 3, Emerging business model 2, Economies of scale 2, Enterprise market focus 2, Value-based pricing 2, and 1 each for Cloud delivery model, Service quality improvement, Platform business model, Value-based orientation, Internet connectivity requirement), but every one of these codes is also supported by other studies.
- **Codes whose counts change** (option a): SaaS 289 to 268; B2B business model 161 to 150; Enterprise market focus 91 to 85; Established vendor transition 94 to 89; Growing business model 85 to 80; Cloud delivery model 152 to 148; Cross-industry applications 72 to 68; Service-oriented model 144 to 140; Subscription-based pricing 153 to 150; Data-driven monetization 108 to 105; Hybrid business model 77 to 74; Value-based pricing 33 to 30; SME market focus 60 to 57; Emerging business model 80 to 77; Future growth potential 49 to 46; Platform business model 391 to 389; Multi-tenant architecture 24 to 22; Startup company focus 127 to 125; Economies of scale 53 to 51; Market expansion 84 to 82; and minus 1 for Gaming industry focus, Cost-based pricing, Global market presence, USA-dominant market, Low switching costs, Cloud computing infrastructure, Remote hosting, On-demand access, Internet connectivity requirement, Security concerns, Organizational readiness, Partner ecosystem disruption, Flexible pricing strategies, Value-based orientation, Service quality improvement, Organizational preparedness, Ecosystem management. The other 24 codes are unchanged.
- **Classes and subclasses:** the 9 classes and 35 subclasses are unchanged, so the ontology mapping in Chapter 6 is not affected.

---

## 4. Pre-existing data issues found during the analysis (outside R08)

Approved: D1, D2 (recorded as a transcription correction), D6 and the IP53 fix. D3 was resolved by the new `generate_distributions.py`; D4 and D5 were left as known limitations.

| # | Issue | Evidence | Impact | Recommendation |
|---|---|---|---|---|
| D1 | Three chart bars do not come from the CSVs but from hand-written counts in `STATISTICS.md`: Enterprise 5 (CSV: 12), Advertising 13 (CSV: 17), Perpetual license 11 (CSV: 10). `STATISTICS.md` also differs from the CSVs on Support (9 vs 21), Developers/Dev-tools (5 vs 2), Government (3 vs 4), Others (1 vs 3), Desktop, API, SDK and Infrastructure. | `by_closed_ended_question/STATISTICS.md` lines 20 to 30 and 120 to 145; journal commit `5d4eec5` changed Enterprise from 17.9% to 7.5% without changing the CSV. | All percentages written in the dissertation text match the CSVs; only the three chart bars diverge. Regenerating the charts from the CSVs changes them: Enterprise 7.5% to 19.0%, Advertising 19.4% to 27.0%. Support (31.7%) would then outrank Advertising and Perpetual license in the revenue chart. | Use the CSVs as the single source of truth and regenerate `STATISTICS.md` and the charts from them. In the revenue chart, show six bars (adding Support) instead of hiding a category that is more frequent than two of the displayed ones. |
| D2 | Four Q17 rows have `extracted_value = "Data"` but an empty `values_inside_scope`: 190653582, 190653772, 190654058, 190655747 (IP63). | `question_17.csv` | "Data" is undercounted: 12 (19.0%) after the correction instead of 15 (23.8%). These three studies are absent from the network-effect chart. | Fix the three remaining rows (`Data (more data = better product)`), so the text would report 23.8%. |
| D3 | The distribution JSONs (`analysis/q_XX_distribution.json`) have the first percentage of every question equal to 41.79, and several counts differ from the CSVs. | e.g., `q_17_distribution.json`: None 3 (41.79%) | Not used by the dissertation. | Regenerate them from the CSVs with a script. |
| D4 | One quote carries the class name `Implementation challenges` as a code (not one of the 61 codes). | `codes_count_report` excludes it, hence 4,630 instead of 4,631 | None on the reported numbers. | Leave as is, or replace it by the intended code if it is evident from the quote. |
| D5 | Q17 row 190655186 extracted "Direct (...), Cross-sided (...)" but kept only Cross-sided; a few Q13 and Q14 rows have similar mapping gaps (e.g., Q14 row 190655389 extracted "Others (...)", yet "Others" never reaches `values_inside_scope` in Q14). | `question_17.csv`, `question_14.csv` | Small; Q13 and Q14 are not cited in the dissertation. | Out of scope for R08; record as known limitation. |
| D6 | `assets/sms/tables/included_primary_studies_refs.tex` in the dissertation is not `\input` anywhere (orphan file with the old IP01 to IP67 numbering). | grep over the dissertation sources | None on the PDF. | Delete it, so the old numbering does not survive in the repository. |

---

## 5. Dissertation inventory (as of the proposal)

### 5.1 Occurrences of "67" that refer to the number of studies

| File:line | Context | Action |
|---|---|---|
| `front_matter/abstract_en.tex:7` | "The SMS synthesized 67 primary studies" | 63 |
| `chapters/01_introduction.tex:19` | "maps 67 primary studies (2014--2024)" | 63 |
| `chapters/02_methodology.tex:35` | "a set of 67 primary studies" | 63 |
| `chapters/03_theoretical_background.tex:82` | "Across 67 primary studies ... subscription appearing in over 76\% of the studies" | 63; "in nearly 75\%" (74.6%) |
| `chapters/04_related_work.tex:86` | "synthesized from 67 primary studies" | 63 |
| `chapters/04_related_work.tex:134` | "evidence from 67 primary studies" | 63 |
| `chapters/05_sms.tex:90` | "each of the 67 included primary studies" | 63 |
| `chapters/05_sms.tex:99` | quality results and "Only the 67 studies classified as Excellent were accepted" | keep the assessment record (67 Excellent records) and add the post-selection verification sentence leading to 63 (see 7.2) |
| `chapters/05_sms.tex:113` | "across the 67 primary studies" | 63 |
| `chapters/05_sms.tex:206` | "based on 67 primary studies (2014--2024)" | 63 |
| `chapters/06_ontology.tex:75` | "synthesized 67 primary studies ... revenue sources reported in 76.1\% of studies" | 63; "subscription revenue reported in 74.6\% of studies" |
| `chapters/08_conclusion.tex:11` | "The mapping synthesized 67 primary studies" | 63 |
| `chapters/08_conclusion.tex:26` | "synthesized 67 primary studies" | 63 |
| `back_matter/appendices.tex:9` | "lists the 67 primary studies" | 63 |
| `assets/related_work/tables/related_work_comparison.tex:23` | "SMS (67 studies)" | 63 |
| `assets/methodology/tikz/research_process.tex:61` | "67 primary studies" (figure label) | 63 |
| `assets/sms/tikz/selection_flow.tex:10` | "67 studies included" | replaced by the PRISMA diagram |
| `assets/sms/tikz/quality_classification.tex:19` | pie slice `48.6/excellent/67` | see decision 7.3 |
| `assets/sms/tikz/{customer_channels,customer_types,network_effects,revenue_sources}.tex:4` | comment "% Total: 67 studies" | 63 |
| `assets/sms/tables/included_primary_studies.tex` | header comment "IP01--IP67" and 67 rows | renumber (7.4) |
| `primary_studies.bib:2` and the `% IPnn` comments | "IP01--IP67" | renumber comments; delete `hannola2013clarifying` and the "same as" comment stubs for IP47, IP55, IP62 |

**Unrelated "67" (do not touch):** `chapters/07_ontology_evaluation.tex:55`, `:120`, `:173` (67.7% operational cases) and `assets/ontology_evaluation/tikz/operational_status.tex:32`; the "0.674" values in Chapter 7 tables. `front_matter/abstract_pt.tex` contains no numbers. The qualification and defense slide decks under `docs/` also say 67; they are historical records of past presentations and are left unchanged.

### 5.2 SMS percentages and counts written in the text

- `chapters/05_sms.tex:122-123` (monetization and delivery): 76.1%, 41.8%, 32.8%, 71.6%, 40.3%.
- `chapters/05_sms.tex:135-136` (market): 53.7%, 41.8%, 47.8%, 41.8%, 38.8%, 37.3%.
- `chapters/05_sms.tex:155-156` (ecosystem and network effects): 49.3%, 46.3%, 35.8%, 31.3%, 22.4%.
- `chapters/05_sms.tex:168-169` (success factors and challenges): 138, 84, 64 mentions; 41 and 38 mentions.
- `chapters/05_sms.tex:188` (construct validity): "37--39\% for questions about licensing and billing periodicity" (response rates of Q11 and Q15).
- `chapters/03_theoretical_background.tex:82` (Section 3.2.2, "over 76\%") and `:96` ("a majority of the models ... growing or emerging rather than consolidated": still true, 80 + 77 against 23 code assignments).
- `chapters/06_ontology.tex:75` (76.1%).
- `chapters/08_conclusion.tex:13` (security concerns and revenue stream transformation as recurrent challenges: still the top two).

### 5.3 Figures and tables

| File | Content | Source |
|---|---|---|
| `assets/sms/tikz/revenue_sources.tex` | 5 bars (Q12) | CSV, except Advertising and Perpetual license (D1) |
| `assets/sms/tikz/customer_types.tex` | 4 bars (Q04) | CSV, except Enterprise (D1) |
| `assets/sms/tikz/customer_channels.tex` | 5 bars (Q18) | CSV |
| `assets/sms/tikz/network_effects.tex` | 6 bars (Q17; "Not Reported" = `response_found = no`) | CSV |
| `assets/sms/tikz/success_factors.tex` | 5 codes of the Success factors class, % over their sum (358) | code counts |
| `assets/sms/tikz/quality_classification.tex` | quality tiers of the 138 assessed records | protocol records |
| `assets/sms/tikz/selection_flow.tex` | selection flow | protocol records |
| `assets/sms/tikz/papers_per_db.tex` | 2,889 records per database | unaffected |
| `assets/sms/tables/business_models_distribution.tex` | 10 business-model codes, % over 4,630 | code counts |
| `assets/sms/tables/extracted_business_models.tex` | 14 business-model codes with mentions | code counts |
| `assets/sms/tables/implementation_challenges.tex` | 6 challenge codes, total 159 | code counts |
| `assets/sms/tables/included_primary_studies.tex` | Appendix A table | renumber |

---

## 6. Preview of the new numbers (63 studies)

Closed-ended percentages use the CSV values with the decisions of Section 2. Code counts use option 3.3(a); values under option (b) are given in brackets where they differ.

### 6.1 Numbers cited in the text

| Location | Item | Before (67) | After (63) | Change |
|---|---|---|---|---|
| Ch. 5, 5.2.2 | Subscription | 76.1% (51) | 74.6% (47) | −1.5 pp |
| Ch. 5, 5.2.2 | Usage/consumption | 41.8% (28) | 41.3% (26) | −0.5 pp |
| Ch. 5, 5.2.2 | Transaction | 32.8% (22) | 33.3% (21) | +0.5 pp |
| Ch. 5, 5.2.2 | Multi-tenant SaaS | 71.6% (48) | 69.8% (44) | −1.8 pp; "most frequent" still true |
| Ch. 5, 5.2.2 | Mobile | 40.3% (27) | 42.9% (27) | +2.6 pp |
| Ch. 5, 5.2.3 | B2B | 53.7% (36) | 50.8% (32) | −2.9 pp; still first |
| Ch. 5, 5.2.3 | B2C | 41.8% (28) | 44.4% (28) | +2.6 pp |
| Ch. 5, 5.2.3 | Direct sales | 47.8% (32) | 44.4% (28) | **ties with product-led growth** |
| Ch. 5, 5.2.3 | Product-led growth | 41.8% (28) | 44.4% (28) | **ties with direct sales** |
| Ch. 5, 5.2.3 | Partners/channels | 38.8% (26) | 39.7% (25) | **ties with digital marketing** |
| Ch. 5, 5.2.3 | Digital marketing | 37.3% (25) | 39.7% (25) | **ties with partners/channels** |
| Ch. 5, 5.2.4 | Standalone product | 49.3% (33) | 46.0% (29) | **order flips** |
| Ch. 5, 5.2.4 | Two-sided platform | 46.3% (31) | 49.2% (31) | **now the most frequent role** |
| Ch. 5, 5.2.4 | Direct network effect | 35.8% (24) | 36.5% (23) | +0.7 pp |
| Ch. 5, 5.2.4 | Cross-sided | 31.3% (21) | 33.3% (21) | +2.0 pp |
| Ch. 5, 5.2.4 | Data | 22.4% (15) | 19.0% (12) | −3.4 pp (23.8%, n = 15, if D2 is fixed) |
| Ch. 5, 5.2.5 | Ecosystem management | 138 | 137 | −1 |
| Ch. 5, 5.2.5 | Market expansion | 84 | 82 | −2 |
| Ch. 5, 5.2.5 | Organizational preparedness | 64 | 63 | −1 |
| Ch. 5, 5.2.5 | Security concerns | 41 | 40 | −1 |
| Ch. 5, 5.2.5 | Revenue stream transformation | 38 | 38 [37] | 0 [−1] |
| Ch. 5, 5.3.1 | Response rate Q11 (licensing) | 37.3% (25) | 39.7% (25) | |
| Ch. 5, 5.3.1 | Response rate Q15 (billing periodicity) | 38.8% (26) | 39.7% (25) [38.1% (24)] | text: "37--39%" becomes "about 40%" [or "38--40%"] |
| Ch. 3, 3.2.2 | Subscription | "over 76%" | 74.6% | wording becomes "nearly 75%" |
| Ch. 6, 6.2 | Subscription | 76.1% | 74.6% | |
| Several | Number of primary studies | 67 | 63 | |

**Changes of order or interpretation:**

1. **Ecosystem role (Q16):** the text says the role "was almost balanced between standalone products (49.3%) and two-sided platforms (46.3%)". After the correction two-sided platforms lead (49.2% against 46.0%). The "almost balanced" reading still holds, but the order of the sentence must be inverted. Cause: the three duplicates were all coded as standalone products, and IP63 too.
2. **Acquisition channels (Q18):** direct sales is no longer the single most frequent channel; it ties with product-led growth (44.4% each), and partners/channels ties with digital marketing (39.7% each).
3. **Code table (Table 5.1):** Mobile app market (279) moves ahead of SaaS (268); Subscription-based pricing and B2B business model tie at 150.
4. **Revenue chart:** depends on D1 (Support would become the fourth source at 31.7%).
5. Everything else keeps its order: subscription remains dominant, multi-tenant SaaS remains the most frequent delivery mode, B2B remains ahead of B2C, direct network effects remain the most frequent, and the top two challenges and top three success factors keep their positions.

### 6.2 Charts

| Chart | Bar | Before (as drawn) | After (from CSV) |
|---|---|---|---|
| Revenue sources | Subscription | 76.1 (51) | 74.6 (47) |
| | Usage/consumption | 41.8 (28) | 41.3 (26) |
| | Transaction | 32.8 (22) | 33.3 (21) |
| | Support (not drawn) | 13.4 (9) per STATISTICS.md; 31.3 (21) per CSV | 31.7 (20), proposed new bar (D1) |
| | Advertising | 19.4 (13) | 27.0 (17) |
| | Perpetual license | 16.4 (11) | 14.3 (9) |
| Customer types | B2B | 53.7 (36) | 50.8 (32) |
| | B2C | 41.8 (28) | 44.4 (28) |
| | SME (B2B SMB) | 35.8 (24) | 31.7 (20) |
| | Enterprise | 7.5 (5) | 19.0 (12) (D1) |
| Acquisition channels | Direct sales | 47.8 (32) | 44.4 (28) |
| | Product-led growth | 41.8 (28) | 44.4 (28) |
| | Partners/channels | 38.8 (26) | 39.7 (25) |
| | Digital marketing | 37.3 (25) | 39.7 (25) |
| | Marketplaces | 22.4 (15) | 23.8 (15) |
| Network effects | Direct | 35.8 (24) | 36.5 (23) |
| | Cross-sided | 31.3 (21) | 33.3 (21) |
| | Data | 22.4 (15) | 19.0 (12), or 23.8 (15) with D2 |
| | None | 4.5 (3) | 3.2 (2) |
| | Others | 3.0 (2) | 3.2 (2) |
| | Not reported | 17.9 (12) | 22.2 (14) |
| Success factors (% of 358 / 352) | Ecosystem management | 138 (38.5) | 137 (38.9) |
| | Market expansion | 84 (23.5) | 82 (23.3) |
| | Organizational preparedness | 64 (17.9) | 63 (17.9) |
| | Service quality improvement | 36 (10.1) | 35 (9.9) |
| | Value-based orientation | 36 (10.1) | 35 (9.9) |

### 6.3 Tables

**Table "Distribution of Main Identified Business Models"** (same 10 codes as today, re-sorted; % over total classifications):

| Code | Before (of 4,630) | After (of 4,522) [of 4,515] |
|---|---|---|
| Platform business model | 391 (8.4%) | 389 (8.6%) |
| SaaS (Software as a Service) | 289 (6.2%) | 268 (5.9%) [266] |
| Mobile app market | 279 (6.0%) | 279 (6.2%), now second |
| Freemium model | 264 (5.7%) | 264 (5.8%) |
| Open source business model | 188 (4.1%) | 188 (4.2%) |
| B2B business model | 161 (3.5%) | 150 (3.3%) [149] |
| Subscription-based pricing | 153 (3.3%) | 150 (3.3%) [149] |
| Cloud delivery model | 152 (3.3%) | 148 (3.3%) [147] |
| Service-oriented model | 144 (3.1%) | 140 (3.1%) |
| Network effects | 133 (2.9%) | 133 (2.9%) |

Note: the table is a curated list of business-model codes, not the raw top 10 (Ecosystem management, 137, and Startup company focus, 125, rank above Network effects but are not business models). This is unchanged.

**Table "Software Business Models Identified"** (mentions): Platform 391 to 389; SaaS 289 to 268 [266]; Freemium 264; Open source 188; Subscription-based pricing 153 to 150 [149]; Cloud delivery 152 to 148 [147]; Service-oriented 144 to 140; Data-driven monetization 108 to 105; Hybrid 77 to 74; Marketplace 63; API-based 44; Pay-as-you-go 40; Value-based pricing 33 to 30; Perpetual licensing 14. Order unchanged.

**Table "Identified Implementation Challenges":** Security concerns 41 to 40; Revenue stream transformation 38 [37]; Organizational readiness 23 to 22; Partner ecosystem disruption 23 to 22; Customer trust maintenance 19; Quality management 15; total 159 to 156 [155]. Order unchanged.

### 6.4 Totals

| Quantity | Before | After (a) | After (b) |
|---|---|---|---|
| Primary studies | 67 | 63 | 63 |
| Classified quotes | 1,859 | 1,810 | 1,807 |
| Code assignments (61 codes) | 4,630 | 4,522 | 4,515 |

---

## 7. Proposed Phase 2

### 7.1 Data repository

1. Create `excluded_records/` with the four removed `raw_data/*.json` and `raw_articles_txt/*.txt` files and a `README.md` stating, for each, the reason and the record it duplicates. The original copy-1 JSONs of IP01 to IP03 are preserved in git history (the commit message will reference them).
2. Apply the revised extraction to `raw_data/190638760.json`, `190638781.json`, `190638871.json` (closed answers per Section 2, with `source_citation` updated to the quoted evidence; open answers merged per Section 3.1); add an `extraction_metadata.revision` note referencing this document.
3. Remove the four rows from the 12 CSVs and update the three kept rows.
4. Update the 21 `by_open_ended_question/question_XX.json` files (remove, merge, `total_articles` = 63, recount `articles_with_response`).
5. Update the 21 quote classification files (merge rule 3.1).
6. Rerun `count_codes.py` and `generate_code_hierarchy.py`; regenerate `STATISTICS.md` numbers and the distribution JSONs with a small reproducible script (`by_closed_ended_question/generate_distributions.py`), keeping the hand-written observations.
7. Update the corpus figures in `context/` (INDEX "Quick Stats", key findings, statistics summaries) and add a pointer to this document. `ieee_journal_slr/` (old copy of the journal draft) is left untouched, like `sbm-sms-journal/`.

### 7.2 Dissertation text (Chapter 5, Results), draft

> Of the 138 evaluated studies, 67 (48.6\%) were classified as ``Excellent'', [...] and 39 (28.3\%) as ``Poor''. The 67 records classified as ``Excellent'' were selected for inclusion. A post-selection verification of these records identified three duplicate records of the same publications and one study published outside the 2014--2024 window, which were removed (Section~\ref{sec:sms_threats}). The final corpus therefore comprises 63 primary studies (Appendix~\ref{appendix:included-studies}). Figure~\ref{fig:sms_selection_flow} summarizes the selection process in the PRISMA 2020 format \cite{page2021prisma}.

(`page2021prisma` would be added to `references.bib`: Page, M. J. et al., "The PRISMA 2020 statement: an updated guideline for reporting systematic reviews", BMJ 372:n71, 2021, DOI 10.1136/bmj.n71.)

**Threats to validity (new paragraph at the end of 5.3.2 Internal Validity), draft:**

> A post-selection verification of the corpus, carried out while preparing the final version of this dissertation, identified four records that should not have been included. Three were duplicate records of the same publications (identical DOI and full text) that had been imported as separate entries and were not detected during duplicate removal. The fourth study was published in 2013, outside the 2014--2024 window; it probably passed the date filter because its DOI record was only created in December 2014. For each duplicated publication, the two extractions were merged into a single revised extraction, with divergent closed-ended answers resolved by re-reading the full text; the out-of-window study was removed. All distributions, code counts, figures, and tables in this chapter were recalculated over the resulting 63 primary studies, and the data repository documents each change.

### 7.3 Quality pie (decision needed)

- **Option A (recommended):** keep the pie as the record of the quality assessment (138 records, 67 Excellent; tier bands untouched, R12 is a separate item) and add to the caption: "Counts refer to the 138 records assessed, before the post-selection verification." There are no per-record quality data in the repositories, so the non-Excellent tiers cannot be re-verified for duplicates.
- Option B: show 134 records (63 Excellent 47.0%, Very Good 24 17.9%, Good 3 2.2%, Fair 4 3.0%, Weak 1 0.7%, Poor 39 29.1%). Exact for the Excellent tier, but it suggests that all 138 records were re-verified, which did not happen.

### 7.4 PRISMA 2020 flow (R24), layout

Counts come only from existing records (Chapter 5 text and current figure); the four removals appear as an explicit post-selection step.

```
IDENTIFICATION
 [Records identified from databases (n = 2,889)      ]  -> [Records removed before screening:      ]
 [ ACM DL (n = 57), IEEE Xplore (n = 225),           ]     [ duplicate records (n = 216)           ]
 [ Scopus (n = 2,607)                                ]
SCREENING
 [Records screened, title and abstract (n = 2,673)   ]  -> [Records excluded, IC/EC (n = 2,361)    ]
 [Reports sought for retrieval (n = 312)             ]  -> [Reports not assessed in full text      ]
                                                           [ (n = 174), no reason stated (9.2)     ]
 [Reports assessed for eligibility, full text and    ]  -> [Reports excluded, quality below        ]
 [ quality (n = 138)                                 ]     [ "Excellent" (n = 71): Very Good 24,   ]
                                                           [ Good 3, Fair 4, Weak 1, Poor 39       ]
 [Records meeting all criteria (n = 67)              ]  -> [Removed after post-selection           ]
                                                           [ verification (n = 4): duplicate       ]
                                                           [ records (n = 3), outside the time     ]
                                                           [ window (n = 1)                        ]
INCLUDED
 [Studies included in the review (n = 63)            ]
```

PRISMA 2020 folds "eligibility" into the Screening phase; the three phase labels (Identification, Screening, Included) would be drawn as vertical bars on the left, as in the official template.

### 7.5 Appendix renumbering

Removed rows: IP47 (Hedman copy), IP55 (Ojala copy), IP62 (Wu copy), IP63 (Hannola). New numbering:

| Old | New |
|---|---|
| IP01 to IP46 | unchanged (IP01 to IP03 receive the page ranges listed in 1.3) |
| IP48 to IP54 | IP47 to IP53 |
| IP56 to IP61 | IP54 to IP59 |
| IP64 to IP67 | IP60 to IP63 |

IP codes appear only in the appendix table and in `primary_studies.bib` comments; no chapter cites an IP code. `hannola2013clarifying` is cited only in the appendix table, so its `.bib` entry can be deleted.

---

## 8. Decisions requested before Phase 2

1. Keep copy-1 `article_id`s (Section 1.2).
2. Approve the 16 closed-ended decisions (Section 2.3).
3. Merge rule for open answers: option (a) plain union or (b) union with verification (Section 3.3). Recommendation: (b).
4. D1: regenerate the charts from the CSVs (Enterprise and Advertising bars change) and add Support to the revenue chart. Recommendation: yes.
5. D2: fix the three Q17 "Data" rows (text would say 23.8% instead of 19.0%). Recommendation: yes.
6. Quality pie: option A (Section 7.3). Recommendation: A.
7. PRISMA: confirm that the 174 reports between 312 and 138 were excluded for full-text availability, as the current figure says ("Reports not retrieved"), and not also for IC2 (minimum six pages). **Answered: no record exists; see 9.2.**
8. D6: delete the orphan `included_primary_studies_refs.tex`; fix the IP53 venue year (Section 1.3).

---

## 9. Approval and applied values

### 9.1 Decisions approved on 2026-10-19

| # | Decision | Outcome |
|---|---|---|
| 1 | Keep the copy-1 `article_id` of each pair | Approved |
| 2 | 16 closed-ended decisions (Section 2.3) | Approved, **except #11** (Ojala Q17), changed to **not reported**: like #16, the cited passage is a generic statement from the literature review section (p. 2, "Renting can also increase the positive network externality effect [24]"), not a description of the four case firms, so it does not show a network effect in the business model studied. |
| 3 | Open-ended merge rule | Option **(b)**, union with verification: Wu Q31 and Hedman Q15 recorded as not reported; their 3 quotes dropped |
| 4 | D1: charts regenerated from the CSVs, Support added to the revenue chart | Approved |
| 5 | D2: Q17 rows 190653582, 190653772, 190654058 | Approved as a **transcription correction**: `values_inside_scope` set to `Data (more data = better product)`, which is what their `extracted_value` ("Data") already said; no extraction was changed |
| 6 | Quality pie | Option A: 138 assessed records and 67 "Excellent", with a caption note pointing to the post-selection verification |
| 7 | The 174 reports between 312 and 138 | See 9.2 |
| 8 | Delete the orphan `included_primary_studies_refs.tex`; fix the IP53 venue year | Approved |

### 9.2 Reports between 312 and 138

There is no record, in any repository, of the reason why 174 of the 312 potentially relevant reports were not assessed in full text. The annotation "full-text availability" in the former selection figure had no documented source and was removed. The PRISMA diagram now says "Reports not assessed in full text (n = 174)", without a reason, and Chapter 5 states no reason either.

**Note for future recovery:** the reason for these 174 exclusions may be recoverable from the SMS records in Thoth (the selection tool used for the study) or in the SMS Google Sheets spreadsheet. If it is recovered, the PRISMA box can state it and, if needed, split it by reason.

### 9.3 Applied values (63 studies)

Final values after all approved decisions. They differ from the preview in Section 6 only where the approval changed the proposal: Ojala Q17 (#11), D2, and option (b).

| Item | Before (67) | After (63) |
|---|---|---|
| Subscription | 76.1% (51) | 74.6% (47) |
| Usage/consumption | 41.8% (28) | 41.3% (26) |
| Transaction | 32.8% (22) | 33.3% (21) |
| Support (new bar) | 31.3% (21) | 31.7% (20) |
| Advertising | 25.4% (17); chart showed 19.4% (13) | 27.0% (17) |
| Perpetual license | 14.9% (10); chart showed 16.4% (11) | 14.3% (9) |
| Multi-tenant SaaS | 71.6% (48) | 69.8% (44) |
| Mobile | 40.3% (27) | 42.9% (27) |
| B2B | 53.7% (36) | 50.8% (32) |
| B2C | 41.8% (28) | 44.4% (28) |
| SME (B2B SMB) | 35.8% (24) | 31.7% (20) |
| Enterprise | 17.9% (12); chart showed 7.5% (5) | 19.0% (12) |
| Direct sales | 47.8% (32) | 44.4% (28) |
| Product-led growth | 41.8% (28) | 44.4% (28) |
| Partners/channels | 38.8% (26) | 39.7% (25) |
| Digital marketing | 37.3% (25) | 39.7% (25) |
| Marketplaces | 22.4% (15) | 23.8% (15) |
| Standalone product | 49.3% (33) | 46.0% (29) |
| Two-sided platform | 46.3% (31) | 49.2% (31) |
| Direct network effect | 35.8% (24) | 34.9% (22) |
| Cross-sided | 31.3% (21) | 33.3% (21) |
| Data | 22.4% (15) | 23.8% (15) |
| None / Others | 4.5% (3) / 3.0% (2) | 3.2% (2) / 3.2% (2) |
| Network effect not reported | 17.9% (12) | 23.8% (15) |
| Response rate Q11 / Q15 | 37.3% / 38.8% | 39.7% / 38.1% |
| Ecosystem management / Market expansion / Organizational preparedness | 138 / 84 / 64 | 137 / 82 / 63 |
| Service quality improvement / Value-based orientation | 36 / 36 | 35 / 35 |
| Security concerns / Revenue stream transformation | 41 / 38 | 40 / 37 |
| Challenges total (6 codes) | 159 | 155 |
| Classified quotes / code assignments | 1,859 / 4,630 | 1,807 / 4,515 |
| Platform / Mobile app market / SaaS (mentions) | 391 / 279 / 289 | 389 / 279 / 266 |

Interpretation changes carried into the dissertation: two-sided platforms now lead standalone products; direct sales ties with product-led growth and partners/channels ties with digital marketing; Mobile app market moves ahead of SaaS in the code table; subscription falls below 75% ("nearly 75%" in Chapter 3). All other orders are unchanged; no code of the 61-code scheme disappears.

### 9.4 Files changed in this repository

- `raw_data/190638760.json`, `190638781.json`, `190638871.json`: revised extraction (closed answers per 2.3 and 9.1; open answers merged; `extraction_metadata.revision` added).
- `excluded_records/`: the four removed records (`raw_data/` and `raw_articles_txt/`) and a README.
- `by_closed_ended_question/question_*.csv` (12 files): four rows removed, three rows revised, D2 transcription fix.
- `by_closed_ended_question/STATISTICS.md`, `analysis/q_*_distribution.json`: regenerated by the new `generate_distributions.py`.
- `by_open_ended_question/question_*.json` (21 files) and `analysis/quotes_classification/q_*_classification.json` (21 files): merged and recounted.
- `by_open_ended_question/analysis/codes_count_report.json` (rerun of `count_codes.py`) and `CODES_COUNT_REPORT.md` (new `generate_codes_report.py`, which also fixes the class grouping of the former report).
- `context/`: INDEX quick stats updated; notes added to context files that cite the 67-record numbers.
- `context/analysis/apply_corpus_correction_r08.py`: the script that applied the change (edits are block-level, so unchanged JSON items keep their bytes).

`ieee_journal_slr/` (old copy of the journal draft) was not changed; the correction will be applied to `sbm-sms-journal` together with R23, as recorded in the revision tracker.

---

## Appendix A. Open-ended questions: per-question comparison

"Repeated" counts copy-2 quotes that match a copy-1 quote under rule 3.1. "Codes only in copy N" is computed per question; across the whole study, only `Value-based pricing` (Ojala) and `High switching costs` (Hedman) exist in copy 2 alone.

#### Wu et al. 2014 (copy 1 = 190638760, copy 2 = 190655721)

| EQ | Answer found (1 / 2) | Quotes 1 | Quotes 2 | Repeated | Merged | Codes only in copy 1 | Codes only in copy 2 |
|----|----|----|----|----|----|----|----|
| Q01 | yes / yes | 4 | 1 | 0 | 5 | Cloud computing infrastructure; Growing business model; Pay-as-you-go pricing; Remote hosting; Revenue stream transformation; Service-oriented model; Single-version deployment; Subscription-based pricing | Cloud delivery model; Emerging business model |
| Q02 | yes / yes | 4 | 1 | 1 | 4 | Cloud computing infrastructure; Cloud delivery model; Emerging business model; Single-version deployment | none |
| Q03 | yes / yes | 2 | 2 | 1 | 3 | Healthcare technology | none |
| Q05 | yes / yes | 1 | 1 | 1 | 1 | none | SaaS (Software as a Service) |
| Q06 | yes / yes | 1 | 1 | 1 | 1 | none | SaaS (Software as a Service) |
| Q07 | yes / yes | 1 | 1 | 0 | 2 | Cross-industry applications; Pay-as-you-go pricing | B2B business model; SME market focus |
| Q11 | yes / no **(differs)** | 3 | 0 | 0 | 3 | Perpetual licensing; SaaS (Software as a Service); Service-oriented model; Single-version deployment; Subscription-based pricing | none |
| Q15 | yes / yes | 2 | 1 | 1 | 2 | none | none |
| Q20 | yes / yes | 5 | 0 | 0 | 5 | Cost-based pricing; Economies of scale; Enterprise market focus; On-demand access; Pay-as-you-go pricing; Remote hosting; SME market focus; SaaS (Software as a Service); Service-oriented model; Single-version deployment; Subscription-based pricing | none |
| Q21 | yes / yes | 3 | 0 | 0 | 3 | Enterprise market focus; On-demand access; Pay-as-you-go pricing; Remote hosting; SME market focus; SaaS (Software as a Service); Service-oriented model; Subscription-based pricing | none |
| Q22 | yes / yes | 4 | 1 | 0 | 5 | Economies of scale; Future growth potential; Growing business model; Market expansion; Pay-as-you-go pricing; Service-oriented model; Subscription-based pricing | none |
| Q23 | yes / yes | 5 | 1 | 0 | 6 | Economies of scale; Flexible pricing strategies; Market expansion; Pay-as-you-go pricing; Service quality improvement; Subscription-based pricing | none |
| Q24 | yes / yes | 4 | 2 | 1 | 5 | Cloud computing infrastructure; Economies of scale; Internet connectivity requirement; Service-oriented model; Single-version deployment | none |
| Q25 | yes / yes | 4 | 1 | 1 | 4 | Flexible pricing strategies; Pay-as-you-go pricing; Perpetual licensing; Revenue stream transformation; Single-version deployment | SaaS (Software as a Service) |
| Q26 | yes / yes | 3 | 1 | 0 | 4 | Enterprise market focus; Low switching costs; Revenue stream transformation; SME market focus | Service quality improvement |
| Q27 | yes / yes | 3 | 1 | 1 | 3 | Economies of scale; Flexible pricing strategies; Service quality improvement; Value-based orientation | SaaS (Software as a Service) |
| Q28 | yes / yes | 4 | 1 | 1 | 4 | Cost-based pricing; Future growth potential; Startup company focus; Subscription-based pricing; Value-based pricing | none |
| Q29 | yes / yes | 2 | 1 | 1 | 2 | Emerging business model | none |
| Q31 | yes / no **(differs)** | 2 | 0 | 0 | 2 | B2B business model; Cloud delivery model; Cross-industry applications; SaaS (Software as a Service) | none |
| Q32 | yes / yes | 4 | 1 | 1 | 4 | Service-oriented model; Subscription-based pricing | none |
| Q33 | yes / yes | 5 | 1 | 1 | 5 | Flexible pricing strategies; Global market presence; Market expansion; Pay-as-you-go pricing; Value-based orientation; Value-based pricing | none |

#### Ojala 2014 (copy 1 = 190638781, copy 2 = 190655555)

| EQ | Answer found (1 / 2) | Quotes 1 | Quotes 2 | Repeated | Merged | Codes only in copy 1 | Codes only in copy 2 |
|----|----|----|----|----|----|----|----|
| Q01 | yes / yes | 3 | 1 | 0 | 4 | Cloud computing infrastructure; Cloud delivery model; Multi-instance architecture; Multi-tenant architecture; Service-oriented model | Flexible pricing strategies |
| Q02 | yes / yes | 2 | 2 | 2 | 2 | none | none |
| Q03 | yes / yes | 4 | 1 | 0 | 5 | B2B business model; Enterprise market focus; Gaming industry focus; Platform business model | Cloud delivery model; SaaS (Software as a Service) |
| Q05 | yes / yes | 2 | 1 | 1 | 2 | SME market focus | SaaS (Software as a Service) |
| Q06 | yes / yes | 1 | 1 | 1 | 1 | none | SaaS (Software as a Service) |
| Q07 | yes / yes | 3 | 1 | 1 | 3 | Cloud delivery model; Market expansion; Perpetual licensing; SME market focus; SaaS (Software as a Service); Subscription-based pricing | B2B business model; Cross-industry applications |
| Q11 | no / yes **(differs)** | 0 | 2 | 0 | 2 | none | Enterprise market focus; Organizational readiness; SaaS (Software as a Service); Security concerns |
| Q15 | yes / no **(differs)** | 2 | 0 | 0 | 2 | SaaS (Software as a Service); Service-oriented model; Subscription-based pricing | none |
| Q20 | yes / yes | 3 | 0 | 0 | 3 | Cloud delivery model; Economies of scale; Marketplace model; On-demand access; Platform business model; SaaS (Software as a Service); Subscription-based pricing | none |
| Q21 | yes / yes | 2 | 1 | 1 | 2 | Cloud computing infrastructure; Partner ecosystem disruption; SaaS (Software as a Service) | none |
| Q22 | yes / yes | 3 | 1 | 0 | 4 | Cloud delivery model; Economies of scale; Low switching costs; Market expansion; SME market focus | Value-based pricing |
| Q23 | yes / yes | 4 | 1 | 1 | 4 | Cloud computing infrastructure; Economies of scale; Low switching costs; Value-based orientation | SaaS (Software as a Service) |
| Q24 | yes / yes | 3 | 2 | 1 | 4 | Cloud computing infrastructure; Internet connectivity requirement; SaaS (Software as a Service) | Organizational readiness |
| Q25 | yes / yes | 3 | 1 | 1 | 3 | Hybrid model adoption; Internet connectivity requirement; Remote hosting | Cloud delivery model |
| Q26 | yes / yes | 4 | 1 | 0 | 5 | Economies of scale; Low switching costs; Revenue stream transformation | High switching costs; Organizational readiness |
| Q27 | yes / yes | 3 | 1 | 0 | 4 | Flexible pricing strategies; Multi-instance architecture | none |
| Q28 | yes / yes | 2 | 1 | 0 | 3 | Cloud delivery model; Customer trust maintenance; Ecosystem management; Marketplace model; Platform business model | B2B business model; SaaS (Software as a Service); Subscription-based pricing |
| Q29 | yes / yes | 2 | 1 | 0 | 3 | Technology evolution | none |
| Q31 | yes / yes | 4 | 1 | 0 | 5 | Cloud delivery model; Data-driven monetization; Gaming industry focus; Hybrid business model; Multi-instance architecture | none |
| Q32 | yes / yes | 3 | 1 | 0 | 4 | High switching costs; Low switching costs; Multi-instance architecture; Multi-tenant architecture | none |
| Q33 | yes / yes | 4 | 1 | 1 | 4 | Economies of scale; Established vendor transition; Hybrid business model; Low switching costs; Market expansion; Multi-tenant architecture; SME market focus; Technology evolution | none |

#### Hedman and Xiao 2016 (copy 1 = 190638871, copy 2 = 190655386)

| EQ | Answer found (1 / 2) | Quotes 1 | Quotes 2 | Repeated | Merged | Codes only in copy 1 | Codes only in copy 2 |
|----|----|----|----|----|----|----|----|
| Q01 | yes / yes | 3 | 1 | 1 | 3 | Established vendor transition; Revenue stream transformation; SME market focus; Subscription-based pricing | none |
| Q02 | yes / yes | 3 | 2 | 1 | 4 | Service-oriented model | SME market focus |
| Q03 | yes / yes | 1 | 1 | 0 | 2 | none | Cloud delivery model |
| Q05 | yes / yes | 2 | 1 | 1 | 2 | none | Cloud delivery model |
| Q06 | yes / yes | 1 | 1 | 1 | 1 | none | SaaS (Software as a Service) |
| Q07 | yes / yes | 2 | 1 | 1 | 2 | Market expansion | Cloud delivery model |
| Q11 | no / no | 0 | 0 | 0 | 0 | none | none |
| Q15 | no / yes **(differs)** | 0 | 1 | 0 | 1 | none | Revenue stream transformation; SaaS (Software as a Service); Subscription-based pricing |
| Q20 | yes / yes | 4 | 2 | 0 | 6 | Ecosystem management; Partner ecosystem disruption; Pay-as-you-go pricing; SME market focus; Startup company focus | On-demand access |
| Q21 | yes / yes | 3 | 1 | 0 | 4 | Ecosystem management; Partner compensation; Perpetual licensing; Platform business model; SME market focus | Established vendor transition |
| Q22 | yes / yes | 2 | 1 | 0 | 3 | Cloud computing infrastructure; Established vendor transition; Market consolidation; On-demand access; Technology evolution | Cloud delivery model; Low switching costs; Market expansion |
| Q23 | yes / yes | 4 | 2 | 1 | 5 | Ecosystem management; Partner compensation; Pilot implementation | none |
| Q24 | yes / yes | 3 | 3 | 0 | 6 | Organizational readiness; Partner ecosystem disruption; Pilot implementation | Ecosystem management; Quality management; Technology evolution |
| Q25 | yes / yes | 3 | 2 | 1 | 4 | Low switching costs; Organizational preparedness | High switching costs |
| Q26 | yes / yes | 5 | 2 | 0 | 7 | Hybrid model adoption; Low switching costs; Quality management; Revenue stream transformation | Established vendor transition |
| Q27 | yes / yes | 3 | 1 | 0 | 4 | Ecosystem management; Organizational readiness; Partner compensation; Pilot implementation | none |
| Q28 | yes / yes | 3 | 0 | 0 | 3 | Cloud computing infrastructure; Digital transformation; Established vendor transition; Future growth potential; Hybrid business model; Hybrid model adoption; Partner ecosystem disruption; Revenue stream transformation | none |
| Q29 | yes / yes | 2 | 2 | 1 | 3 | Hybrid model adoption | Cloud computing infrastructure |
| Q31 | yes / yes | 3 | 1 | 0 | 4 | Cloud delivery model; Hybrid business model; Platform business model; Startup company focus | Revenue stream transformation |
| Q32 | yes / yes | 1 | 1 | 1 | 1 | none | none |
| Q33 | yes / yes | 5 | 2 | 1 | 6 | Digital transformation; Established vendor transition; Network effects; Platform business model; SME market focus; SaaS (Software as a Service); Service-oriented model | none |
