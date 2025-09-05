import os, telegram
from flask import Flask, request

app = Flask(__name__)
bot = telegram.Bot(token=os.getenv("BOT_TOKEN"))
GROUP_ID = os.getenv("ALERT_GROUP_ID")
SECRET = os.getenv("WEBHOOK_SECRET")

@app.route(f"/tvhook/{SECRET}", methods=["POST"])
def tvhook():
    payload = request.get_json(silent=True) or {}
    ticker = payload.get("ticker") or payload.get("symbol") or "N/A"
    message = payload.get("message") or "Signal"
    bot.send_message(chat_id=GROUP_ID, text=f"📈 TV: {ticker} — {message}")
    return "ok", 200

# Expose Flask app for a second process if you choose to run it separately.
flask_app = app
