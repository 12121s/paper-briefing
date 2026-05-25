from datetime import datetime, UTC
from pathlib import Path
import json
import html

today = datetime.now(UTC).strftime("%Y-%m-%d")

REPORTS_DIR = Path("reports")
PAPERS_DIR = Path("papers")
DATA_DIR = Path("data")

REPORTS_DIR.mkdir(exist_ok=True)
PAPERS_DIR.mkdir(exist_ok=True)
DATA_DIR.mkdir(exist_ok=True)

papers = [
    {
        "id": "2605-00890",
        "title": "Skeleton-Based Posture Classification to Promote Safer Walker-Assisted Gait in Older Adults",
        "authors": "Sergio D. Sierra M., Monica Sinha, Marcela Múnera, Carlos A. Cifuentes",
        "arxiv_id": "2605.00890",
        "link": "https://arxiv.org/abs/2605.00890",
        "published": "2026-04-27",
        "categories": "cs.CV, cs.AI, cs.LG",
        "priority": "1순위",
        "keywords": [
            "posture classification",
            "movement assessment",
            "rehabilitation technology",
            "assistive interaction",
            "safety assessment"
        ],
        "summary": [
            "이 논문은 보행 보조기 사용 상황에서 고령자의 자세와 상태를 분류하기 위한 방법을 비교한 연구입니다.",
            "보행 보조기 사용 중 낙상 위험을 줄이기 위해 walker usage, standing vs. sitting, posture classification 문제를 다룹니다.",
            "geometric approach, XGBoost, SVM, deep learning models를 비교했으며, geometric approach와 XGBoost가 자세 분류에서 좋은 성능을 보였다고 보고합니다.",
            "스마트 워커 기반 human-robot interaction과 낙상 예방을 위한 posture assessment의 가능성을 제시합니다."
        ],
        "connection": [
            "이 논문은 재활승마를 직접 다루지는 않지만, ‘안전한 자세’, ‘위험 자세’, ‘보조가 필요한 상태’를 분류한다는 점에서 내 연구와 연결됩니다.",
            "재활승마에서도 기승자의 자세를 안정, 전방 쏠림, 좌우 비대칭, 균형 상실 위험 등으로 분류하는 평가 체계를 설계할 수 있습니다.",
            "카메라 기반 skeleton posture classification 연구이므로, 향후 IMU 기반 자세 평가와 비교하거나 결합하는 기준 논문으로 활용할 수 있습니다."
        ],
        "what_paper_says": "고령자의 walker-assisted gait 상황에서 posture classification 모델을 비교하고, smart walker 기반 보조 및 낙상 예방 가능성을 논의합니다.",
        "extension_idea": "재활승마 상황에서 IMU 또는 영상 기반 데이터를 활용해 기승자 자세를 안정/불안정/비대칭/보조 필요 상태로 분류하는 평가 체계로 확장할 수 있습니다."
    },
    {
        "id": "2605-00913",
        "title": "Leveraging Imperfect Medical Data: A Manifold-Consistent Spatio-Temporal Network for Sensor-based Human Activity Recognition",
        "authors": "Jiangtao Fan, Anish Jindal, Amir Atapour-Abarghouei",
        "arxiv_id": "2605.00913",
        "link": "https://arxiv.org/abs/2605.00913",
        "published": "2026-04-29",
        "categories": "cs.CV, cs.AI",
        "priority": "2순위",
        "keywords": [
            "sensor-based HAR",
            "wearable sensing",
            "imperfect sensing",
            "movement assessment",
            "robust model"
        ],
        "summary": [
            "이 논문은 의료 및 헬스케어 모니터링에서 sensor-based human activity recognition을 다룹니다.",
            "실제 wearable sensing 환경에서는 missing values, sensor failure, environmental noise 때문에 입력 신호가 불완전할 수 있다는 문제를 제기합니다.",
            "이를 해결하기 위해 Manifold-Consistent Spatio-Temporal Network, MCSTN을 제안합니다.",
            "PAMAP2, Opportunity, WISDM 데이터셋에서 실험했으며, 불완전한 센서 입력 상황에서도 강건성을 유지하는 결과를 보고합니다."
        ],
        "connection": [
            "이 논문은 재활승마나 자세 교정을 직접 다루지는 않지만, wearable sensing 기반 movement assessment에서 발생하는 센서 노이즈와 결측 문제를 다룬다는 점에서 중요합니다.",
            "재활승마 현장에서는 IMU 부착 위치가 흔들리거나, 말의 움직임 때문에 신호가 불안정해질 수 있습니다.",
            "따라서 현실적인 서비스 환경에서 안정적으로 자세와 균형 상태를 추정하기 위한 기술적 근거로 활용할 수 있습니다."
        ],
        "what_paper_says": "불완전한 센서 데이터 환경에서도 human activity recognition 성능을 유지하기 위한 spatio-temporal model을 제안합니다.",
        "extension_idea": "재활승마/자세 훈련 환경에서 IMU 신호가 흔들리거나 일부 누락되더라도 안정적으로 자세 변화와 균형 상태를 추정하는 모델 설계로 확장할 수 있습니다."
    },
    {
        "id": "2604-26214",
        "title": "Exploring the Feasibility and Acceptability of AI-Mediated Serious Illness Conversations in the Emergency Department",
        "authors": "Hasibur Rahman, Kenji Numata, Evelyn T Lai, Maria Cheriyan, Adrian Haimovich, Kei Ouchi, Smit Desai",
        "arxiv_id": "2604.26214",
        "link": "https://arxiv.org/abs/2604.26214",
        "published": "2026-04-29",
        "categories": "cs.HC",
        "priority": "3순위",
        "keywords": [
            "healthcare HCI",
            "acceptability",
            "AI-mediated interaction",
            "participatory design",
            "feedback boundary"
        ],
        "summary": [
            "이 논문은 응급실에서 중증 질환 관련 values-goals-preferences 대화를 지원하는 voice-based conversational agent의 feasibility와 acceptability를 평가한 HCI 연구입니다.",
            "55명의 고령 환자를 대상으로 상호작용 수용 가능성과 실행 가능성을 살펴봤습니다.",
            "많은 참여자가 대화를 완료하고 상호작용을 수용 가능하다고 평가했지만, hallucinated diagnostic statements 같은 boundary violation도 관찰되었습니다.",
            "의료 맥락에서 AI가 사용자에게 피드백하거나 해석을 제공할 때, 윤리적·정서적 위험과 경계 설정이 중요하다는 점을 보여줍니다."
        ],
        "connection": [
            "이 논문은 움직임 평가나 재활승마를 직접 다루지는 않지만, healthcare HCI와 AI-mediated feedback의 안전한 설계라는 관점에서 참고할 수 있습니다.",
            "재활승마 피드백 시스템이 사용자의 자세, 균형, 수행 상태를 해석할 때 의료적 진단처럼 들리는 표현을 피해야 합니다.",
            "치료사, 보호자, 참여자가 AI 피드백을 어떻게 받아들이는지 co-design 또는 participatory design으로 검토할 필요가 있다는 근거로 활용할 수 있습니다."
        ],
        "what_paper_says": "응급실 맥락에서 AI 대화 에이전트의 feasibility와 acceptability를 평가하고, 의료적 경계 위반의 위험을 논의합니다.",
        "extension_idea": "재활승마 디지털 피드백 시스템에서 AI가 제공하는 문장, 경고, 해석의 수용 가능성과 안전한 표현 경계를 co-design으로 설계하는 연구로 확장할 수 있습니다."
    }
]

def esc(value):
    return html.escape(str(value), quote=True)

def render_list(items):
    return "\n".join(f"<li>{esc(item)}</li>" for item in items)

def paper_page(paper):
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>{esc(paper["title"])}</title>
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, 'Noto Sans KR', sans-serif; line-height: 1.75; max-width: 980px; margin: 40px auto; padding: 0 24px; color: #222; }}
    a {{ color: #2563eb; }}
    .badge {{ display: inline-block; padding: 4px 10px; border-radius: 999px; background: #eef2ff; margin-right: 6px; font-size: 13px; }}
    section {{ border-top: 1px solid #e5e7eb; padding-top: 24px; margin-top: 28px; }}
    .box {{ background: #f8fafc; border: 1px solid #e5e7eb; border-radius: 14px; padding: 18px; }}
  </style>
</head>
<body>
  <p><a href="../index.html">← Overview</a></p>
  <h1>{esc(paper["title"])}</h1>
  <p>
    <span class="badge">{esc(paper["priority"])}</span>
    <span class="badge">arXiv: {esc(paper["arxiv_id"])}</span>
    <span class="badge">{esc(paper["published"])}</span>
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
    <ul>
      {render_list(paper["summary"])}
    </ul>
  </section>

  <section>
    <h2>3) 논문 내용과 내 연구 아이디어 분리</h2>
    <div class="box">
      <h3>What the paper says</h3>
      <p>{esc(paper["what_paper_says"])}</p>
      <h3>Extension idea for my research</h3>
      <p>{esc(paper["extension_idea"])}</p>
    </div>
  </section>

  <section>
    <h2>4) 내 연구와의 연결점</h2>
    <ul>
      {render_list(paper["connection"])}
    </ul>
  </section>
</body>
</html>
"""

for paper in papers:
    with open(PAPERS_DIR / f"{paper['id']}.html", "w", encoding="utf-8") as f:
        f.write(paper_page(paper))

report_html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>Daily Research Briefing - {today}</title>
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
  <h1>Daily Research Briefing</h1>
  <p><strong>Date:</strong> {today}</p>

  <div class="note">
    <p>오늘의 검색 축은 IMU, movement assessment, posture classification, wearable sensing, biofeedback, healthcare HCI, participatory design입니다.</p>
    <p>직접적으로 재활승마를 다룬 신규 arXiv 논문은 많지 않았으나, 움직임 평가·센서 기반 자세 분류·AI 피드백 안전성 측면에서 연결 가능한 후보 3편을 정리했습니다.</p>
  </div>

  <h2>오늘의 추천 논문</h2>
  {"".join(f'''
  <article class="paper">
    <p><span class="badge">{esc(p["priority"])}</span><span class="badge">arXiv: {esc(p["arxiv_id"])}</span></p>
    <h3><a href="../papers/{esc(p["id"])}.html">{esc(p["title"])}</a></h3>
    <p><strong>연결점:</strong> {esc(p["connection"][0])}</p>
    <p><a href="{esc(p["link"])}">arXiv 원문 보기</a></p>
  </article>
  ''' for p in papers)}
</body>
</html>
"""

with open(REPORTS_DIR / f"{today}.html", "w", encoding="utf-8") as f:
    f.write(report_html)

papers_meta = [
    {
        "id": p["id"],
        "title": p["title"],
        "authors": p["authors"],
        "arxiv_id": p["arxiv_id"],
        "link": p["link"],
        "published": p["published"],
        "categories": p["categories"],
        "priority": p["priority"],
        "keywords": p["keywords"],
        "page": f"papers/{p['id']}.html"
    }
    for p in papers
]

reports_meta = [
    {
        "date": today,
        "title": f"Daily Research Briefing - {today}",
        "page": f"reports/{today}.html",
        "paper_count": len(papers)
    }
]

with open(DATA_DIR / "papers.json", "w", encoding="utf-8") as f:
    json.dump(papers_meta, f, ensure_ascii=False, indent=2)

with open(DATA_DIR / "reports.json", "w", encoding="utf-8") as f:
    json.dump(reports_meta, f, ensure_ascii=False, indent=2)

index_html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>Paper Briefing OS</title>
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, 'Noto Sans KR', sans-serif; line-height: 1.75; max-width: 1080px; margin: 40px auto; padding: 0 24px; color: #222; background: #fafafa; }}
    a {{ color: #2563eb; }}
    header {{ margin-bottom: 32px; }}
    .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; }}
    .card {{ background: white; border: 1px solid #e5e7eb; border-radius: 16px; padding: 20px; }}
    .badge {{ display: inline-block; padding: 4px 10px; border-radius: 999px; background: #eef2ff; margin-right: 6px; font-size: 13px; }}
  </style>
</head>
<body>
  <header>
    <h1>Paper Briefing OS</h1>
    <p>IMU · Movement Assessment · Biofeedback · Technology Probe · Co-design 중심의 논문 브리핑 아카이브입니다.</p>
  </header>

  <section>
    <h2>Daily Reports</h2>
    <div class="grid">
      <article class="card">
        <p><span class="badge">{today}</span><span class="badge">{len(papers)} papers</span></p>
        <h3><a href="reports/{today}.html">Daily Research Briefing - {today}</a></h3>
        <p>오늘의 연구 관심사 기반 arXiv 논문 후보 리포트입니다.</p>
      </article>
    </div>
  </section>

  <section>
    <h2>Paper Summaries</h2>
    <div class="grid">
      {"".join(f'''
      <article class="card">
        <p><span class="badge">{esc(p["priority"])}</span><span class="badge">arXiv: {esc(p["arxiv_id"])}</span></p>
        <h3><a href="papers/{esc(p["id"])}.html">{esc(p["title"])}</a></h3>
        <p>{esc(p["connection"][0])}</p>
      </article>
      ''' for p in papers)}
    </div>
  </section>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_html)

print(f"Generated reports/{today}.html")
print(f"Generated {len(papers)} paper summary pages")
print("Updated index.html, data/papers.json, data/reports.json")
