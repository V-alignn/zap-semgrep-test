import json

with open("semgrep-report.json") as f:
    data = json.load(f)

html = """
<html>
<head>
  <title>SAST Report - Semgrep</title>
  <style>
    body { font-family: Arial; margin: 20px; }
    h1 { color: #2c3e50; }
    table { border-collapse: collapse; width: 100%; }
    th, td { border: 1px solid #ccc; padding: 8px; }
    th { background-color: #f4f4f4; }
    .HIGH { background-color: #ffcccc; }
    .MEDIUM { background-color: #fff0b3; }
    .LOW { background-color: #e6f7ff; }
  </style>
</head>
<body>
<h1>SAST Findings (Semgrep)</h1>
<table>
<tr>
  <th>Severity</th>
  <th>Rule</th>
  <th>File</th>
  <th>Line</th>
  <th>Description</th>
</tr>
"""

for result in data.get("results", []):
    severity = result.get("extra", {}).get("severity", "LOW").upper()
    rule = result.get("check_id", "")
    path = result.get("path", "")
    line = result.get("start", {}).get("line", "")
    message = result.get("extra", {}).get("message", "")

    html += f"""
    <tr class="{severity}">
      <td>{severity}</td>
      <td>{rule}</td>
      <td>{path}</td>
      <td>{line}</td>
      <td>{message}</td>
    </tr>
    """

html += "</table></body></html>"

with open("sast-report.html", "w") as f:
    f.write(html)
