import os, time, threading
from collections import defaultdict
from typing import Dict, List
import requests

# In-memory store (swap with SQLite or Postgres for persistence)
alerts: Dict[int, List[dict]] = defaultdict(list)  # chat_id -> list of {user_id, symbol, price}

def add_alert(chat_id, user_id, symbol, price):
    alerts[chat_id].append({"user_id": user_id, "symbol": symbol, "price": price})

def list_alerts_for_user(chat_id, user_id):
    return [a for a in alerts.get(chat_id, []) if a["user_id"] == user_id]

def fetch_prices(symbols):
    # Placeholder: plug in your preferred price source
    # Return dict like {"TCS": 3520.5, ...}
    return {}

def price_checker_job(context):
    bot = context.bot
    for chat_id, items in list(alerts.items()):
        if not items:
            continue
        symbols = list({a["symbol"] for a in items})
        prices = fetch_prices(symbols)
        to_remove = []
        for a in items:
            last = prices.get(a["symbol"])
            if last is not None and last >= a["price"]:
                bot.send_message(chat_id, f"🚨 {a['symbol']} hit ₹{a['price']}")
                to_remove.append(a)
        for a in to_remove:
            alerts[chat_id].remove(a)
