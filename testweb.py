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
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #0f172a;
                color: white;
                text-align: center;
            }}
            .card {{
                background: #1e293b;
                padding: 20px;
                margin: 15px auto;
                width: 300px;
                border-radius: 12px;
                box-shadow: 0 0 10px rgba(0,0,0,0.5);
            }}
            img {{
                width: 40px;
                vertical-align: middle;
                margin-right: 10px;
            }}
        </style>
    </head>

    <body>
        <h1>🌍 World Time Dashboard</h1>

        <div class="card">
            <p>
                <img src="https://flagcdn.com/w40/in.png">
                <b>India:</b> {india_time}
            </p>
        </div>

        <div class="card">
            <p>
                <img src="https://flagcdn.com/w40/us.png">
                <b>USA (New York):</b> {usa_time}
            </p>
        </div>

        <div class="card">
            <p>
                <img src="https://flagcdn.com/w40/cn.png">
                <b>China:</b> {china_time}
            </p>
        </div>

    </body>
    </html>
    """
@app.route('/health')
def health():
  return {"status": "OK"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
