import json
import os
import time
import html
import urllib.parse
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d")

SEARCH_KEYWORDS = [
    "HCI",
    "rehabilitation",
    "wearable sensing",
    "IMU / inertial sensing",
    "biofeedback",
    "assistive technology",
    "movement assessment",
    "posture assessment",
]

ARXIV_QUERY = (
    '(cat:cs.HC OR cat:cs.CY OR cat:cs.RO OR cat:eess.SP OR cat:cs.AI) '
    'AND '
    '(all:"rehabilitation" OR all:"wearable sensing" OR all:"IMU" OR all:"inertial" OR all:"biofeedback" OR all:"assistive technology" OR all:"posture" OR all:"movement assessment") '
    'ANDNOT '
    '(all:"pedestrian dead reckoning" OR all:"localization" OR all:"radio" OR all:"networking" OR all:"signal processing" OR all:"chip" OR all:"accelerator")'
)

MAX_RESULTS = 3

PRIORITY_TERMS = [
    "hci",
    "human-computer interaction",
    "rehabilitation",
    "wearable sensing",
    "wearable",
    "imu",
    "inertial",
    "biofeedback",
    "assistive",
    "posture",
    "movement assessment",
    "movement training",
]

EXCLUSION_TERMS = [
    "pedestrian",
    "pedestrian dead reckoning",
    "dead reckoning",
    "localization",
    "radio",
    "radio system",
    "radio systems",
    "wireless network",
    "networking",
    "signal processing",
    "signal processing only",
    "chip",
    "accelerator",
    "nand",
    "cim architecture",
]

MIN_RELEVANCE_SCORE = 1

def esc(value):
    return html.escape(str(value or ""), quote=True)

def arxiv_url():
    return (
        "https://export.arxiv.org/api/query?"
        + urllib.parse.urlencode({
            "search_query": ARXIV_QUERY,
            "start": 0,
            "max_results": MAX_RESULTS,
            "sortBy": "submittedDate",
            "sortOrder": "descending"
        })
    )

def fetch_arxiv():
    request = urllib.request.Request(
        arxiv_url(),
        headers={
            "User-Agent": "paper-briefing-os/0.1 contact: rofalfl42@gmail.com"
        }
    )

    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return response.read()
    except urllib.error.HTTPError as e:
        if e.code == 429:
            print("arXiv rate limit: 429 Too Many Requests. Keeping previous data if available.")
            return None
        raise

def parse_entries(xml_data):
    if not xml_data:
        return []

    root = ET.fromstring(xml_data)
    ns = {"atom": "http://www.w3.org/2005/Atom"}

    papers = []

    for entry in root.findall("atom:entry", ns):
        title = entry.findtext("atom:title", default="", namespaces=ns).replace("\n", " ").strip()
        summary = entry.findtext("atom:summary", default="", namespaces=ns).replace("\n", " ").strip()
        raw_id = entry.findtext("atom:id", default="", namespaces=ns).split("/")[-1]
        published = entry.findtext("atom:published", default="", namespaces=ns)[:10]

        authors = [
            author.findtext("atom:name", default="", namespaces=ns)
            for author in entry.findall("atom:author", ns)
        ]

        categories = [
            c.attrib.get("term", "")
            for c in entry.findall("atom:category", ns)
        ]

        relevance_text = f"{title} {summary} {' '.join(categories)}".lower()
        if any(term in relevance_text for term in EXCLUSION_TERMS):
            continue

        relevance_score = sum(1 for term in PRIORITY_TERMS if term in relevance_text)
        if relevance_score < MIN_RELEVANCE_SCORE:
            continue

        paper_id = raw_id.replace(".", "-").replace("/", "-")

        papers.append({
            "id": paper_id,
            "citation": f"arXiv {raw_id}",
            "year": int(published[:4]) if published[:4].isdigit() else "",
            "title": title,
            "authors": ", ".join([a for a in authors if a]),
            "arxiv_id": raw_id,
            "link": f"https://arxiv.org/abs/{raw_id}",
            "published": published,
            "categories": ", ".join(categories),
            "method": "arXiv metadata search",
            "status": "To Read",
            "keywords": SEARCH_KEYWORDS,
            "abstract": [
                summary
            ],
            "terms": [
                ["IMU / inertial sensing", "움직임, 자세, 균형 상태를 측정하기 위해 사용하는 관성 센서 기반 측정 방식입니다."],
                ["Movement assessment", "사람의 움직임, 자세, 균형, 수행 상태를 평가하는 연구 영역입니다."],
                ["Biofeedback", "센서로 측정한 신체 또는 행동 데이터를 사용자에게 다시 보여주어 자기 조절과 학습을 돕는 피드백 방식입니다."]
            ],
            "researchQuestions": [
                "이 논문이 wearable sensing, movement assessment, rehabilitation, HCI 중 어떤 축과 연결되는가?",
                "이 논문의 방법 또는 시스템 설계가 재활승마/움직임 피드백 서비스에 어떻게 확장될 수 있는가?"
            ],
            "design": [
                "현재 페이지는 arXiv metadata와 abstract 기반 자동 요약입니다.",
                "정밀 리뷰가 필요한 논문은 원문 PDF 확인 후 연구 방법론, 데이터, 실험 설계를 별도로 보완해야 합니다."
            ],
            "findings": [
                "자동 수집 단계에서는 abstract 기반 핵심 내용만 저장합니다.",
                "상세 결과와 수치 성능은 원문 확인 후 수동 또는 LLM 요약 단계에서 보완합니다."
            ],
            "interpretation": [
                "이 논문은 내 연구 관심사와 일부 키워드 또는 분야 축에서 연결될 가능성이 있습니다.",
                "직접 관련성은 원문 확인 후 To Read, Reading, Used in Thesis 등으로 분류합니다."
            ],
            "contributions": [
                "최신 연구 후보를 자동으로 수집해 데일리 브리핑 후보군으로 축적합니다."
            ],
            "limitations": [
                "arXiv metadata 기반 검색이므로 relevance가 완벽하지 않을 수 있습니다.",
                "논문에 없는 주장은 생성하지 않고, 연구 연결점은 별도 해석으로 관리해야 합니다."
            ],
            "significance": [
                "IMU, movement assessment, biofeedback, rehabilitation HCI 관련 최신 연구 흐름을 추적하는 데 활용할 수 있습니다."
            ],
            "connection": [
                "재활승마를 직접 다루지 않더라도, 움직임 평가·센서 기반 피드백·재활 상호작용 설계 관점에서 참고 가능성을 검토할 수 있습니다."
            ],
            "page": f"papers/{paper_id}.html"
        })

    return papers

def paper_page(paper):
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>{esc(paper["title"])}</title>
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, 'Noto Sans KR', sans-serif; line-height: 1.75; max-width: 980px; margin: 40px auto; padding: 0 24px; color: #222; }}
    a {{ color: #2563eb; }}
    section {{ border-top: 1px solid #e5e7eb; padding-top: 24px; margin-top: 28px; }}
    .badge {{ display: inline-block; padding: 4px 10px; border-radius: 999px; background: #eef2ff; margin-right: 6px; font-size: 13px; }}
    .box {{ background: #f8fafc; border: 1px solid #e5e7eb; border-radius: 14px; padding: 18px; }}
  </style>
</head>
<body>
  <p><a href="../index.html">← Overview</a></p>
  <h1>{esc(paper["title"])}</h1>
  <p>
    <span class="badge">arXiv: {esc(paper["arxiv_id"])}</span>
    <span class="badge">{esc(paper["published"])}</span>
    <span class="badge">{esc(paper["status"])}</span>
  </p>

  <section>
    <h2>1) 개요</h2>
    <p><strong>저자:</strong> {esc(paper["authors"])}</p>
    <p><strong>분야:</strong> {esc(paper["categories"])}</p>
    <p><strong>링크:</strong> <a href="{esc(paper["link"])}">{esc(paper["link"])}</a></p>
    <p><strong>Keywords:</strong> {", ".join(esc(k) for k in paper["keywords"])}</p>
  </section>

  <section>
    <h2>2) Abstract 요약</h2>
    <div class="box">
      <p>{esc(paper["abstract"][0])}</p>
    </div>
  </section>

  <section>
    <h2>3) 내 연구와의 연결점</h2>
    <ul>
      {"".join(f"<li>{esc(item)}</li>" for item in paper["connection"])}
    </ul>
  </section>

  <section>
    <h2>4) 검토 메모</h2>
    <p>이 페이지는 자동 생성된 1차 후보 요약입니다. 원문 확인 후 연구 방법론, 결과, 한계, 내 연구 적용 가능성을 보완하세요.</p>
  </section>
</body>
</html>
"""

def report_page(papers):
    if papers:
        paper_list = "\n".join(
            f"""
            <article class="paper">
              <p><span class="badge">arXiv: {esc(p["arxiv_id"])}</span><span class="badge">{esc(p["published"])}</span></p>
              <h3><a href="../{esc(p["page"])}">{esc(p["title"])}</a></h3>
              <p>{esc(p["connection"][0])}</p>
              <p><a href="{esc(p["link"])}">arXiv 원문 보기</a></p>
            </article>
            """
            for p in papers
        )
    else:
        paper_list = """
        <div class="note">
          <p>오늘은 설정한 검색 조건에서 강하게 관련된 신규 arXiv 논문을 찾지 못했습니다.</p>
        </div>
        """

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>{today} 오늘의 논문 브리핑</title>
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, 'Noto Sans KR', sans-serif; line-height: 1.75; max-width: 1080px; margin: 40px auto; padding: 0 24px; color: #222; }}
    a {{ color: #2563eb; }}
    .paper {{ border: 1px solid #e5e7eb; border-radius: 16px; padding: 20px; margin: 18px 0; background: #fff; }}
    .badge {{ display: inline-block; padding: 4px 10px; border-radius: 999px; background: #eef2ff; margin-right: 6px; font-size: 13px; }}
    .note {{ background: #f8fafc; border-left: 4px solid #64748b; padding: 14px 18px; }}
  </style>
</head>
<body>
  <p><a href="../index.html">← Overview</a></p>
  <h1>{today} 오늘의 논문 브리핑</h1>
  <div class="note">
    <p>검색 축: IMU, wearable sensing, movement assessment, posture assessment, rehabilitation, biofeedback, assistive technology, HCI</p>
    <p>자동 수집 결과이므로 논문 relevance는 원문 확인 후 조정해야 합니다.</p>
  </div>
  <h2>오늘의 후보 논문</h2>
  {paper_list}
</body>
</html>
"""

def load_json(path, fallback):
    if not os.path.exists(path):
        return fallback
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return fallback

def dedupe_papers(existing, new):
    by_id = {p.get("id"): p for p in existing if p.get("id")}
    for p in new:
        by_id[p["id"]] = p
    return list(by_id.values())

def main():
    os.makedirs("papers", exist_ok=True)
    os.makedirs("reports", exist_ok=True)
    os.makedirs("data", exist_ok=True)

    time.sleep(3)
    xml_data = fetch_arxiv()
    new_papers = parse_entries(xml_data)

    existing_papers = load_json("data/papers.json", [])
    all_papers = dedupe_papers(existing_papers, new_papers)

    for paper in new_papers:
        with open(paper["page"], "w", encoding="utf-8") as f:
            f.write(paper_page(paper))

    report_path = f"reports/{today}.html"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report_page(new_papers))

    with open("data/papers.json", "w", encoding="utf-8") as f:
        json.dump(all_papers, f, ensure_ascii=False, indent=2)

    reports = load_json("data/reports.json", [])
    reports = [r for r in reports if r.get("date") != today]
    reports.insert(0, {
        "date": today,
        "title": f"{today} 오늘의 논문 브리핑",
        "page": report_path,
        "paper_count": len(new_papers)
    })

    with open("data/reports.json", "w", encoding="utf-8") as f:
        json.dump(reports, f, ensure_ascii=False, indent=2)

    print(f"Generated {report_path}")
    print(f"Generated {len(new_papers)} new paper candidates")
    print("Updated data/papers.json and data/reports.json")
    print("index.html was not modified")

if __name__ == "__main__":
    main()
