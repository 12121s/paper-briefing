from datetime import datetime
from pathlib import Path

today = datetime.utcnow().strftime("%Y-%m-%d")

html = f"""
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>Daily Research Briefing - {today}</title>
</head>
<body>
  <h1>Daily Research Briefing</h1>
  <p>Date: {today}</p>

  <h2>Test Report</h2>

  <p>
    This is a generated HTML research briefing test page.
  </p>

</body>
</html>
"""

Path("reports").mkdir(exist_ok=True)

with open(f"reports/{today}.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"Generated reports/{today}.html")
