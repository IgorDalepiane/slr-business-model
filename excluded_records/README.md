# Excluded Records

Records removed from the SMS corpus by the post-selection verification of 2026-10-19 (revision item R08). The corpus went from 67 records to 63 primary studies. Full analysis, decisions, and before/after numbers: [`../context/analysis/corpus-correction-r08.md`](../context/analysis/corpus-correction-r08.md); the change was applied by [`../context/analysis/apply_corpus_correction_r08.py`](../context/analysis/apply_corpus_correction_r08.py).

The files are kept unchanged for traceability. They are no longer read by any analysis script.

| article_id | Former appendix ID | Study | Reason | Data now held by |
|---|---|---|---|---|
| 190655721 | IP62 | Wu, Wortmann and Tan, "A Pricing Framework for Software-as-a-Service", INTECH 2014, DOI 10.1109/INTECH.2014.6927738 | Duplicate record: same DOI and identical full text as 190638760 (only the IEEE Xplore download watermark differs) | 190638760 (merged revised extraction) |
| 190655555 | IP55 | Ojala, "Selection of the Proper Revenue and Pricing Model for SaaS", CloudCom 2014, DOI 10.1109/CloudCom.2014.27 | Duplicate record of 190638781 | 190638781 (merged revised extraction) |
| 190655386 | IP47 | Hedman and Xiao, "Transition to the Cloud: A Vendor Perspective", HICSS 2016, DOI 10.1109/HICSS.2016.494 | Duplicate record of 190638871 | 190638871 (merged revised extraction) |
| 190655747 | IP63 | Hannola, Tervonen, Ojanen and Kässi, "Clarifying the Value Elements of Business Models for Disturbance Management in Supply Chains", IEEM 2013, DOI 10.1109/IEEM.2013.6962664 | Published in 2013 (conference held 10 to 13 December 2013; PDF footer "©2013 IEEE"), outside the 2014 to 2024 window. Its Crossref DOI record was only created in December 2014, which probably explains why it passed the date filter. | removed |

Folders:

- `raw_data/`: the original extraction JSONs of the four records.
- `raw_articles_txt/`: the full texts used for extraction.

The quotes and closed-ended answers of these records were removed from `by_closed_ended_question/` and `by_open_ended_question/`; for the duplicates, their content was merged into the kept record as described in the analysis document. The pre-merge version of the three kept JSONs is available in the git history (commit preceding the R08 correction).
