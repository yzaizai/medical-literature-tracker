import requests
import json
from datetime import datetime, timedelta

MIN_DATE = (datetime.now() - timedelta(days=60)).strftime("%Y/%m/%d")
print(f"搜索起始日期: {MIN_DATE}")
print("=" * 60)

# 测试不同查询方式
queries = [
    ("GDFT精确", '"goal-directed fluid therapy"[Title/Abstract]'),
    ("GDFT宽泛", 'goal-directed fluid therapy'),
    ("血气精确", '"arterial blood gas analysis"[Title/Abstract]'),
    ("血气宽泛", 'arterial blood gas analysis'),
]

for label, q in queries:
    params = {
        "db": "pubmed",
        "term": q,
        "retmax": 5,
        "retmode": "json",
        "sort": "date",
        "mindate": MIN_DATE,
        "datetype": "pdat",
    }
    try:
        r = requests.get(
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi",
            params=params, timeout=30
        )
        data = r.json()
        count = data.get("esearchresult", {}).get("count", "0")
        ids = data.get("esearchresult", {}).get("idlist", [])
        print(f"{label}: 总数={count}, 获取ID数={len(ids)}")
        if ids:
            print(f"  PMIDs: {ids[:5]}")
    except Exception as e:
        print(f"{label}: 出错 - {e}")

print("=" * 60)
print("测试不带日期限制...")

# 测试不带日期限制
for label, q in [("GDFT不限日期", 'goal-directed fluid therapy'), ("血气不限日期", 'arterial blood gas analysis')]:
    params = {
        "db": "pubmed",
        "term": q,
        "retmax": 3,
        "retmode": "json",
        "sort": "date",
    }
    try:
        r = requests.get(
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi",
            params=params, timeout=30
        )
        data = r.json()
        count = data.get("esearchresult", {}).get("count", "0")
        ids = data.get("esearchresult", {}).get("idlist", [])
        print(f"{label}: 总数={count}, ID数={len(ids)}")
        if ids:
            print(f"  PMIDs: {ids[:3]}")
    except Exception as e:
        print(f"{label}: 出错 - {e}")
