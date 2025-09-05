from services.alert_manager import add_alert

def run(update, context):
    if len(context.args) < 2:
        update.message.reply_text("Usage: /setalert <SYMBOL> <PRICE>")
        return
    sym = context.args[0].upper()
    try:
        price = float(context.args[1])
    except ValueError:
        update.message.reply_text("Price must be a number.")
        return
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    add_alert(chat_id, user_id, sym, price)
    update.message.reply_text(f"🔔 Alert set: {sym} at ₹{price}")
