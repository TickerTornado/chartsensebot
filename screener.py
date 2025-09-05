from services.screener_service import get_fundamentals

def run(update, context):
    if not context.args:
        update.message.reply_text("Usage: /screener <SYMBOL>")
        return
    sym = context.args[0].upper()
    data = get_fundamentals(sym)
    pretty = "\n".join([f"{k}: {v}" for k, v in data.items()])
    update.message.reply_text(f"{sym} fundamentals:\n{pretty}")
