# -*- coding: utf-8 -*-
import requests
import sys
import traceback
from datetime import datetime, timedelta
from pathlib import Path

# ============================================================
# 搜索配置
# ============================================================
SEARCH_TOPICS = {
    "GDFT": [
        '"goal-directed fluid therapy"[Title/Abstract]',
        '"goal directed hemodynamic therapy"[Title/Abstract]',
        '"GDFT"[Title/Abstract] AND fluid[Title/Abstract]',
    ],
    "ABG": [
        '"arterial blood gas analysis"[Title/Abstract]',
        '"blood gas analysis"[Title/Abstract] AND arterial[Title/Abstract]',
        '"ABG analysis"[Title/Abstract]',
    ],
    "AnesthesiaAI": [
        '"artificial intelligence"[Title/Abstract] AND anesthesia[Title/Abstract]',
        '"machine learning"[Title/Abstract] AND anesthesiology[Title/Abstract]',
        '"deep learning"[Title/Abstract] AND anesthesia[Title/Abstract]',
        '"AI"[Title/Abstract] AND "anesthesia"[Title/Abstract]',
        '"large language model"[Title/Abstract] AND anesthesia[Title/Abstract]',
    ],
}

DAYS_BACK = 30
MAX_RESULTS_PER_QUERY = 10
BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
MIN_DATE = (datetime.now() - timedelta(days=DAYS_BACK)).strftime("%Y/%m/%d")


def search_pubmed(query, retmax=MAX_RESULTS_PER_QUERY):
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": retmax,
        "retmode": "json",
        "sort": "date",
        "mindate": MIN_DATE,
        "datetype": "pdat",
    }
    try:
        resp = requests.get(f"{BASE_URL}/esearch.fcgi", params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        return data.get("esearchresult", {}).get("idlist", [])
    except Exception as e:
        print(f"  [搜索失败] {query}: {e}")
        return []


def fetch_details(pmids):
    if not pmids:
        return []
    params = {
        "db": "pubmed",
        "id": ",".join(pmids),
        "retmode": "xml",
        "rettype": "abstract",
    }
    try:
        resp = requests.get(f"{BASE_URL}/efetch.fcgi", params=params, timeout=30)
        resp.raise_for_status()
        return parse_xml_articles(resp.text)
    except Exception as e:
        print(f"  [获取详情失败]: {e}")
        traceback.print_exc()
        return []


def parse_xml_articles(xml_text):
    import xml.etree.ElementTree as ET

    articles = []
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError as e:
        print(f"  [XML解析错误]: {e}")
        print(f"  [XML前500字符]: {xml_text[:500]}")
        return articles

    count = 0
    for article in root.iter("PubmedArticle"):
        try:
            pmid_elem = article.find(".//PMID")
            pmid = pmid_elem.text if pmid_elem is not None else "N/A"

            title_elem = article.find(".//ArticleTitle")
            title = title_elem.text if title_elem is not None else "无标题"

            journal_elem = article.find(".//Journal/Title")
            journal = journal_elem.text if journal_elem is not None else "N/A"

            pub_date = "N/A"
            pub_date_elem = article.find(".//PubDate")
            if pub_date_elem is not None:
                year = pub_date_elem.findtext("Year", "")
                month = pub_date_elem.findtext("Month", "")
                day = pub_date_elem.findtext("Day", "")
                pub_date = f"{year} {month} {day}".strip()

            authors = []
            for author in article.findall(".//Author"):
                last = author.findtext("LastName", "")
                fore = author.findtext("ForeName", "")
                if last:
                    authors.append(f"{last} {fore}"[:50])
            author_str = ", ".join(authors[:5])
            if len(authors) > 5:
                author_str += " et al."

            abstract_parts = []
            for abs_elem in article.iter("AbstractText"):
                label = abs_elem.get("Label", "")
                full_text = "".join(abs_elem.itertext())
                if label:
                    abstract_parts.append(f"**{label}**: {full_text}")
                else:
                    abstract_parts.append(full_text)
            abstract = " ".join(abstract_parts)[:2000]

            doi = "N/A"
            for eid in article.findall(".//ELocationID"):
                if eid.get("EIdType") == "doi":
                    doi = eid.text or "N/A"

            articles.append({
                "pmid": pmid,
                "title": title,
                "journal": journal,
                "pub_date": pub_date,
                "authors": author_str,
                "abstract": abstract,
                "doi": doi,
            })
            count += 1
        except Exception as e:
            print(f"  [解析单篇论文出错]: {e}")
            traceback.print_exc()
            continue

    print(f"  [XML解析完成]: 成功解析 {count} 篇")
    return articles


def make_pubmed_link(pmid):
    return f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"


def generate_markdown(topic, articles):
    today = datetime.now().strftime("%Y-%m-%d")
    lines = [
        f"# {topic} - PubMed Latest Papers",
        "",
        f"**Update Time**: {today}",
        f"**Search Range**: Last {DAYS_BACK} days",
        f"**Papers Found**: {len(articles)}",
        "",
        "---",
        "",
    ]

    if not articles:
        lines.append("> No new papers found in this search.")
        return "\n".join(lines)

    for i, art in enumerate(articles, 1):
        lines.append(f"## {i}. {art['title']}")
        lines.append("")
        lines.append(f"- **PMID**: [{art['pmid']}]({make_pubmed_link(art['pmid'])})")
        lines.append(f"- **Journal**: {art['journal']}")
        lines.append(f"- **Publication Date**: {art['pub_date']}")
        lines.append(f"- **Authors**: {art['authors']}")
        if art["doi"] != "N/A":
            lines.append(f"- **DOI**: https://doi.org/{art['doi']}")
        lines.append("")
        if art["abstract"]:
            lines.append("### Abstract")
            lines.append("")
            lines.append(art["abstract"])
            lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def main():
    print("=" * 60)
    print(f"PubMed Search Start - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Search Range: Last {DAYS_BACK} days (since {MIN_DATE})")
    print("=" * 60)

    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)

    for topic, queries in SEARCH_TOPICS.items():
        print(f"\n[Topic] {topic}")
        all_articles = {}

        for query in queries:
            print(f"  Query: {query}")
            pmids = search_pubmed(query)
            print(f"    Found {len(pmids)} PMIDs")

            if pmids:
                articles = fetch_details(pmids)
                print(f"    Parsed {len(articles)} articles")
                for art in articles:
                    all_articles[art["pmid"]] = art

        unique = list(all_articles.values())
        unique.sort(key=lambda x: x["pub_date"], reverse=True)

        md = generate_markdown(topic, unique)
        filepath = results_dir / f"{topic}.md"
        filepath.write_text(md, encoding="utf-8")
        print(f"  Saved: {filepath} ({len(unique)} papers after dedup)")

    # Generate index
    index_lines = [
        "# PubMed Search Index",
        "",
        f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        "| Topic | Report File |",
        "|-------|------------|",
    ]
    for topic in SEARCH_TOPICS:
        index_lines.append(f"| {topic} | [{topic}.md]({topic}.md) |")
    index_lines.append("")
    index_lines.append(
        "> Auto-generated weekly. [View workflow source](../.github/workflows/pubmed-search.yml)"
    )

    (results_dir / "README.md").write_text("\n".join(index_lines), encoding="utf-8")

    print("\n" + "=" * 60)
    print("Search Complete!")
    print("=" * 60)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n[FATAL ERROR] {e}")
        traceback.print_exc()
        sys.exit(1)
