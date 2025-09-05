def run(update, context):
    update.message.reply_text(
        "Commands:\n"
        "/chartink - Latest scan results\n"
        "/screener <SYMBOL> - Key fundamentals\n"
        "/setalert <SYMBOL> <PRICE> - Price alert\n"
        "/listalerts - Your active alerts"
    )
