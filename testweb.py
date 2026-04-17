from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

def get_time(timezone):
    tz = pytz.timezone(timezone)
    now = datetime.now(tz)
    return now.strftime("%H:%M:%S | %d/%m/%y")

@app.route('/')
def home():
    india_time = get_time("Asia/Kolkata")
    usa_time = get_time("America/New_York")
    china_time = get_time("Asia/Shanghai")
    europe_time = get_time("Europe/Paris")
    russia_time = get_time("Europe/Moscow")
    japan_time = get_time("Asia/Tokyo")

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
                transition: all 0.3s ease;
            }}

            .card:hover {{
                transform: scale(1.08);
                box-shadow: 0 0 25px rgba(59,130,246,0.7);
                cursor: pointer;
            }}

            img {{
                width: 40px;
                vertical-align: middle;
                margin-right: 10px;
                transition: transform 0.3s ease;
            }}

            .card:hover img {{
                transform: scale(1.2);
            }}
        </style>
    </head>

    <body>
        <h1>🌍 World Time Dashboard</h1>

        <div class="card">
            <p><img src="https://flagcdn.com/w40/in.png"><b>India:</b> {india_time}</p>
        </div>

        <div class="card">
            <p><img src="https://flagcdn.com/w40/us.png"><b>USA (New York):</b> {usa_time}</p>
        </div>

        <div class="card">
            <p><img src="https://flagcdn.com/w40/cn.png"><b>China:</b> {china_time}</p>
        </div>

        <div class="card">
            <p><img src="https://flagcdn.com/w40/eu.png"><b>Europe (Paris):</b> {europe_time}</p>
        </div>

        <div class="card">
            <p><img src="https://flagcdn.com/w40/ru.png"><b>Russia (Moscow):</b> {russia_time}</p>
        </div>

        <div class="card">
            <p><img src="https://flagcdn.com/w40/jp.png"><b>Japan (Tokyo):</b> {japan_time}</p>
        </div>

    </body>
    </html>
    """

@app.route('/health')
def health():
    return {"status": "OK"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
