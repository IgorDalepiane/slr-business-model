#!/usr/bin/env python3
"""
Apply the R08 corpus correction (see corpus-correction-r08.md, same folder).

- Removes three duplicate records (copy 2 of each pair) and one out-of-window
  study (IP63, published in 2013) from the extraction data.
- Writes one revised extraction per duplicated study under the copy-1 article_id:
  closed-ended answers follow the approved decisions; open-ended answers and coded
  quotes are merged as a union with verification (option b).
- Fixes the transcription of three Q17 rows whose extracted value "Data" had not
  reached values_inside_scope (decision D2).
- Moves the removed raw files to excluded_records/.

Run once from any directory: python3 context/analysis/apply_corpus_correction_r08.py
Edits are block-level: JSON items that do not change keep their original bytes.
"""

import csv
import difflib
import io
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REVISION_DATE = "2026-10-19"
REFERENCE = "context/analysis/corpus-correction-r08.md"

PAIRS = {  # kept (copy 1) -> removed (copy 2)
    "190638760": "190655721",  # Wu, Wortmann and Tan (2014)
    "190638781": "190655555",  # Ojala (2014)
    "190638871": "190655386",  # Hedman and Xiao (2016)
}
OUT_OF_WINDOW = "190655747"  # Hannola et al. (IEEM 2013)
REMOVED = set(PAIRS.values()) | {OUT_OF_WINDOW}

NOT_REPORTED = {
    "response_found": False,
    "extracted_value": "not reported",
    "synonyms_found": [],
    "source_citation": "information not found in text",
    "confidence_level": "high",
}

# Approved closed-ended decisions (Section 2.3 of the analysis document).
# Each entry: (article_id, question_id) -> (fields for raw_data, values_inside_scope)
CLOSED = {
    ("190638760", "4"): ({
        "response_found": True,
        "extracted_value": "B2B (B2B SMB and Enterprise): small and medium enterprises have been the most aggressive adopters, and large corporations are equally attracted to acquiring software services on demand.",
        "source_citation": "Page 2: 'The second challenge comes from the diversity of SaaS clients, among which small and medium enterprises have been the most aggressive adopters. Likewise, large corporations are equally attracted to the idea of acquiring software services on demand'",
        "confidence_level": "medium",
    }, "B2B SMB;B2B;Enterprise"),
    ("190638760", "10"): ({
        "response_found": True,
        "extracted_value": "Proprietary",
        "source_citation": "Page 1: 'Traditionally, software license refers to an agreement granting a licensee the rights to utilize packaged software or components of that software' | Page 6: 'the pricing framework provides a comprehensive categorization of pricing components that can be leveraged by SaaS vendors in constructing software licenses'",
        "confidence_level": "medium",
    }, "Proprietary"),
    ("190638760", "12"): ({
        "response_found": True,
        "extracted_value": [
            "Subscription (recurring monthly subscription fees)",
            "Usage/consumption (pay-per-use, usage-dependent pricing)",
            "Support (helpdesk, setup/training, configuration/integration services)",
            "Others (backup and security services sold as add-ons)",
        ],
        "source_citation": "Page 1: 'clients are charged through recurring subscription fees on a pay-as-you-go basis' | Page 3: 'Monthly subscription fees are the most popular pricing model nowadays' | Page 3: 'Usage-based. In this category, software vendors charge clients for what they use' | Page 3: 'In SaaS, some routine services in traditional licensing model still exist, such as helpdesk support, software setup & training, software configuration and integration, etc.; while others such as backup and security, which were once regarded as being part of clients' responsibilities, are offered as purchasable services from SaaS vendors'",
        "confidence_level": "high",
    }, "Subscription;Usage/consumption;Support;Others"),
    ("190638760", "13"): ({
        "response_found": True,
        "extracted_value": "User/seat",
        "source_citation": "Page 5: 'Vendors from cluster one, making up 67% of our sample, prefer the user-based pricing component in software pricing' | Page 6: 'usage-independent based pricing components were used by about half of SaaS vendors while usage-dependent based pricing components were used by one-third of SaaS vendors'",
        "confidence_level": "medium",
    }, "User/seat"),
    ("190638760", "14"): ({
        "response_found": True,
        "extracted_value": [
            "Tiers/Plans (different pricing plans by functionality configuration)",
            "Pay-as-you-go (usage-dependent pricing)",
            "Prepaid credits (prepaid subscriptions with bulk payment discount)",
        ],
        "source_citation": "Page 3: 'a vendor may offer different pricing plans for an application according to certain product-related criteria (e.g., different combinations of functionality)' | Page 3: 'software vendors encourage clients to prepay their subscriptions. Sometimes software vendors offer some degree of discount for those bulk payment clients' | Page 6: 'it is natural for SaaS vendors to charge the client only for what he uses'",
        "confidence_level": "medium",
    }, "Tiers/Plans;Pay-as-you-go;Prepaid credits"),
    ("190638760", "17"): (dict(NOT_REPORTED), ""),
    ("190638760", "18"): (dict(NOT_REPORTED), ""),
    ("190638760", "19"): (dict(NOT_REPORTED), ""),
    ("190638760", "30"): ({
        "response_found": True,
        "extracted_value": "Secondary data analysis",
        "source_citation": "Page 3: 'To gain insights into pricing strategies of SaaS vendors, we conducted content analysis to investigate the software licensing practices for SaaS. The pricing data source is obtained through our examination of each SaaS vendor's website' | Page 4: 'we performed cluster analyses on these pricing data in order to gain insights into the SaaS licensing practice'",
        "confidence_level": "high",
    }, "Secondary data analysis"),
    ("190638781", "17"): (dict(NOT_REPORTED), ""),
    ("190638871", "8"): ({
        "response_found": True,
        "extracted_value": ["Application"],
        "source_citation": "Page 1, Section 1: 'software-as-a service (SaaS) (e.g. Salesforce.com cloud-based customer relationship management software delivered over the Internet)' | Page 4, Section 4.2: 'ERP Co is a leading vendor of enterprise resource planning (ERP), customer relationship management (CRM), and human resource management (HRM) systems' | Page 5, Section 5.1: 'In this study, we will only focus on the software SMB division of ERP Co.'",
        "confidence_level": "high",
    }, "Application"),
    ("190638871", "17"): (dict(NOT_REPORTED), ""),
}
# Copy-1 answers kept unchanged where the decision equals copy 1:
# Wu Q18/Q19 (already not reported), Ojala Q14/Q18, Hedman Q12/Q13.

# Open-ended answers found by one copy only and rejected on verification (option b).
OPEN_NOT_REPORTED = {("190638760", "31"), ("190638871", "15")}

# D2: transcription fix of values_inside_scope (Q17 extracted value "Data").
D2_ROWS = {"190653582", "190653772", "190654058"}
D2_VALUE = "Data (more data = better product)"

OPEN_QIDS = ["1", "2", "3", "5", "6", "7", "11", "15", "20", "21", "22", "23", "24",
             "25", "26", "27", "28", "29", "31", "32", "33"]


# --------------------------------------------------------------------------- helpers
def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def same_quote(x, y):
    """Repeated quote: equal, contained, or >= 90% of the shorter covered by matching blocks."""
    a, b = norm(x), norm(y)
    if a == b or a in b or b in a:
        return True
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    covered = sum(bl.size for bl in sm.get_matching_blocks() if bl.size >= 15)
    return covered / min(len(a), len(b)) >= 0.9


def overlap(x, y):
    a, b = norm(x), norm(y)
    return difflib.SequenceMatcher(None, a, b, autojunk=False).find_longest_match(0, len(a), 0, len(b)).size >= 20


def split_items(text, indent):
    """Split a JSON array of objects written with one object per block at `indent`.
    Returns (prefix, [item_texts], suffix) so that prefix + ',\n'.join(items) + suffix == text."""
    opener = "\n" + indent + "{"
    closer = "\n" + indent + "}"
    starts = [m.start() + 1 for m in re.finditer(re.escape(opener), text)]
    items, ends = [], []
    for s in starts:
        e = text.index(closer, s) + len(closer)
        items.append(text[s:e])
        ends.append(e)
    prefix = text[:starts[0]]
    suffix = text[ends[-1]:]
    joined = prefix + ",\n".join(items) + suffix
    assert joined == text, "unexpected layout"
    return prefix, items, suffix


def dump_item(obj, indent, unit):
    body = json.dumps(obj, indent=unit, ensure_ascii=False)
    return "\n".join(indent + line if i else indent + line for i, line in enumerate(body.split("\n")))


def merge_list_or_str(a, b):
    if isinstance(a, list) or isinstance(b, list):
        la = a if isinstance(a, list) else [a]
        lb = b if isinstance(b, list) else [b]
        return la + [x for x in lb if norm(str(x)) not in {norm(str(y)) for y in la}]
    if norm(a) == norm(b):
        return a
    return a + " | " + b


def merge_citations(a, b):
    parts = [p.strip() for p in a.split(" | ") if p.strip()]
    seen = {norm(p) for p in parts}
    for p in (x.strip() for x in b.split(" | ")):
        if p and norm(p) not in seen and not any(norm(p) in s or s in norm(p) for s in seen):
            parts.append(p)
            seen.add(norm(p))
    return " | ".join(parts)


# --------------------------------------------------------------------------- raw_data
def revise_raw():
    log = {}
    for keep, drop in PAIRS.items():
        path = ROOT / "raw_data" / f"{keep}.json"
        text = path.read_text(encoding="utf-8")
        prefix, items, suffix = split_items(text, "\t\t")
        other = {q["question_id"]: q for q in json.loads((ROOT / "raw_data" / f"{drop}.json").read_text(encoding="utf-8"))["extracted_data"]}
        changed = []
        for i, block in enumerate(items):
            q = json.loads(block)
            qid = q["question_id"]
            new = dict(q)
            if (keep, qid) in CLOSED:
                new.update(CLOSED[(keep, qid)][0])
            elif qid in OPEN_QIDS:
                b = other[qid]
                if (keep, qid) in OPEN_NOT_REPORTED:
                    new.update(NOT_REPORTED)
                elif q["response_found"] and b["response_found"]:
                    new["extracted_value"] = merge_list_or_str(q["extracted_value"], b["extracted_value"])
                    new["synonyms_found"] = merge_list_or_str(q.get("synonyms_found", []), b.get("synonyms_found", []))
                    new["source_citation"] = merge_citations(q["source_citation"], b["source_citation"])
                elif b["response_found"]:
                    for k in ("response_found", "extracted_value", "synonyms_found", "source_citation", "confidence_level"):
                        new[k] = b[k]
            if new != q:
                items[i] = dump_item(new, "\t\t", "\t")
                changed.append(qid)
        meta_text = prefix
        meta = json.loads(prefix + "]}")["extraction_metadata"]
        meta["revision"] = {
            "date": REVISION_DATE,
            "reference": REFERENCE,
            "merged_from_duplicate_record": drop,
            "description": "Single revised extraction for a publication imported twice. Closed-ended divergences were resolved by re-reading the full text; open-ended answers are the union of both extractions, without repeated content, after verification against the article.",
            "questions_changed": changed,
        }
        new_meta = "{\n\t\"extraction_metadata\": " + json.dumps(meta, indent="\t", ensure_ascii=False).replace("\n", "\n\t") + ",\n\t\"extracted_data\": [\n"
        assert meta_text.startswith("{\n\t\"extraction_metadata\"")
        out = new_meta + ",\n".join(items) + suffix
        json.loads(out)
        path.write_text(out, encoding="utf-8")
        log[keep] = changed
    return log


# --------------------------------------------------------------------------- closed CSVs
def csv_value(qid, value):
    if not isinstance(value, list):
        return value
    if qid == "14":
        return str(value)
    if qid == "8":
        return "; ".join(value)
    return ", ".join(value)


def revise_csvs():
    for f in sorted((ROOT / "by_closed_ended_question").glob("question_*.csv")):
        qid = str(int(f.stem.split("_")[1]))
        raw = f.read_text(encoding="utf-8")
        rows = list(csv.reader(io.StringIO(raw)))
        header, body = rows[0], rows[1:]
        col = {h: i for i, h in enumerate(header)}
        out = [header]
        for r in body:
            aid = r[col["article_id"]]
            if aid in REMOVED:
                continue
            if (aid, qid) in CLOSED:
                fields, scope = CLOSED[(aid, qid)]
                r[col["response_found"]] = "yes" if fields["response_found"] else "no"
                r[col["values_inside_scope"]] = scope
                r[col["extracted_value"]] = csv_value(qid, fields["extracted_value"])
                r[col["confidence_level"]] = fields["confidence_level"]
                r[col["source_citation"]] = fields["source_citation"]
            if qid == "17" and aid in D2_ROWS:
                assert r[col["extracted_value"]] == "Data" and r[col["values_inside_scope"]] == ""
                r[col["values_inside_scope"]] = D2_VALUE
            out.append(r)
        buf = io.StringIO()
        csv.writer(buf, lineterminator="\r\n").writerows(out)
        f.write_text(buf.getvalue(), encoding="utf-8", newline="")


# --------------------------------------------------------------------------- open-ended files
def revise_open_questions():
    raw = {aid: {q["question_id"]: q for q in json.loads((ROOT / "raw_data" / f"{aid}.json").read_text(encoding="utf-8"))["extracted_data"]} for aid in PAIRS}
    for f in sorted((ROOT / "by_open_ended_question").glob("question_*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        qid = d["question_metadata"]["question_id"]
        resp = []
        for e in d["responses_by_article"]:
            if e["article_id"] in REMOVED:
                continue
            if e["article_id"] in PAIRS:
                src = raw[e["article_id"]][qid]
                for k in ("response_found", "extracted_value", "synonyms_found", "source_citation", "confidence_level"):
                    e[k] = src[k]
            resp.append(e)
        d["responses_by_article"] = resp
        m = d["question_metadata"]
        m["total_articles"] = len(resp)
        m["articles_with_response"] = sum(1 for e in resp if e["response_found"])
        m["articles_without_response"] = m["total_articles"] - m["articles_with_response"]
        f.write_text(json.dumps(d, indent=2, ensure_ascii=False), encoding="utf-8")


# --------------------------------------------------------------------------- coded quotes
def revise_quotes():
    stats = {"repeated": 0, "moved": 0, "dropped_ip63": 0, "dropped_unverified": 0}
    for f in sorted((ROOT / "by_open_ended_question/analysis/quotes_classification").glob("q_*_classification.json")):
        qid = str(int(f.stem.split("_")[1]))
        text = f.read_text(encoding="utf-8")
        unit = "\t" if text.startswith("{\n\t") else "  "  # q_02 uses two spaces
        prefix, blocks, suffix = split_items(text, unit * 2)
        objs = [json.loads(b) for b in blocks]
        out_blocks, out_objs = [], []
        for b, o in zip(blocks, objs):
            aid = o["article_id"]
            if aid == OUT_OF_WINDOW:
                stats["dropped_ip63"] += 1
                continue
            if aid in PAIRS.values():
                continue  # handled below
            if (aid, qid) in OPEN_NOT_REPORTED:
                stats["dropped_unverified"] += 1
                continue
            out_blocks.append(b)
            out_objs.append(o)
        for keep, drop in PAIRS.items():
            copy2 = [o for o in objs if o["article_id"] == drop]
            if not copy2:
                continue
            if (keep, qid) in OPEN_NOT_REPORTED:
                stats["dropped_unverified"] += len(copy2)
                continue
            idx_a = [i for i, o in enumerate(out_objs) if o["article_id"] == keep]
            insert_at = (idx_a[-1] + 1) if idx_a else len(out_objs)
            new_items = []
            for j in copy2:
                hit = next((i for i in idx_a if same_quote(out_objs[i]["quote"], j["quote"])), None)
                if hit is not None:
                    stats["repeated"] += 1
                    h = out_objs[hit]
                    covered = set(h["assigned_codes"])
                    for i in idx_a:
                        if overlap(out_objs[i]["quote"], j["quote"]):
                            covered |= set(out_objs[i]["assigned_codes"])
                    extra = [c for c in j["assigned_codes"] if c not in covered]
                    longer = len(j["quote"]) > len(h["quote"])
                    if extra or longer:
                        h = dict(h)
                        h["assigned_codes"] = h["assigned_codes"] + extra
                        if longer:
                            h["quote"] = j["quote"]
                        out_objs[hit] = h
                        out_blocks[hit] = dump_item(h, unit * 2, unit)
                else:
                    k = dict(j)
                    k["article_id"] = keep
                    new_items.append(k)
                    stats["moved"] += 1
            for n, k in enumerate(new_items):
                out_objs.insert(insert_at + n, k)
                out_blocks.insert(insert_at + n, dump_item(k, unit * 2, unit))
        out = prefix + ",\n".join(out_blocks) + suffix
        json.loads(out)
        f.write_text(out, encoding="utf-8")
    return stats


# --------------------------------------------------------------------------- excluded records
def move_excluded():
    for aid in sorted(REMOVED):
        for sub, ext in (("raw_data", "json"), ("raw_articles_txt", "txt")):
            dest = ROOT / "excluded_records" / sub
            dest.mkdir(parents=True, exist_ok=True)
            subprocess.run(["git", "mv", f"{sub}/{aid}.{ext}", f"excluded_records/{sub}/{aid}.{ext}"], cwd=ROOT, check=True)


if __name__ == "__main__":
    if not (ROOT / "raw_data" / f"{OUT_OF_WINDOW}.json").exists():
        raise SystemExit("Correction already applied (IP63 is no longer in raw_data/).")
    print("raw_data questions changed:", revise_raw())
    revise_csvs()
    revise_open_questions()
    print("quotes:", revise_quotes())
    move_excluded()
    print("done")
