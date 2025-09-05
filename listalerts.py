from services.alert_manager import list_alerts_for_user

def run(update, context):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    alerts = list_alerts_for_user(chat_id, user_id)
    if not alerts:
        update.message.reply_text("No active alerts.")
        return
    lines = [f"{a['symbol']} @ ₹{a['price']}" for a in alerts]
    update.message.reply_text("Your alerts:\n" + "\n".join(lines))
