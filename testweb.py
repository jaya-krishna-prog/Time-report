from flask import Flask
from datetime import datetime
import zoneinfo

app = Flask(__name__)

def get_time(timezone):
    now = datetime.now(zoneinfo.ZoneInfo(timezone))
    return now.strftime("%H:%M:%S | %d/%m/%y")

@app.route('/')
def home():
    india_time = get_time("Asia/Kolkata")
    usa_time = get_time("America/New_York")
    china_time = get_time("Asia/Shanghai")

    return f"""
    <html>
<head>
<meta http-equiv="refresh" content="1">
</head>
<body>
<h1>🌍 World Time Dashboard</h1>
<p><b>🇮🇳 India:</b> {india_time}</p>
<p><b>🇺🇸 USA (New York):</b> {usa_time}</p>
<p><b>🇨🇳 China:</b> {china_time}</p>
</body>
</html>
"""

@app.route('/health')
def health():
    return {"status": "OK"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
