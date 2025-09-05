import os
from services.chartink_service import get_chartink_results

def run(update, context):
    payload = os.getenv("CHARTINK_SCAN_JSON")
    if not payload:
        update.message.reply_text("Chartink scan not configured.")
        return
    symbols = get_chartink_results(payload)
    if not symbols:
        update.message.reply_text("No results right now.")
        return
    update.message.reply_text("Chartink Scan:\n" + ", ".join(symbols[:50]))
