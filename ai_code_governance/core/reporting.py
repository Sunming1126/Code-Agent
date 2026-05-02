import os
import json
from datetime import datetime

def save_json_report(report, report_dir):
    os.makedirs(report_dir, exist_ok=True)
    filename = os.path.join(report_dir, "report.json")
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4, ensure_ascii=False)
    return filename

def save_html_report(report, report_dir):
    os.makedirs(report_dir, exist_ok=True)
    filename = os.path.join(report_dir, "report.html")

    html = f'''
    <html>
    <head><title>AI Governance Report</title></head>
    <body>
        <h1>AI Code Governance Report</h1>
        <p>Generated: {datetime.now()}</p>
        <pre>{json.dumps(report, indent=4)}</pre>
    </body>
    </html>
    '''

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)

    return filename