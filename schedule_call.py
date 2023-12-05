def schedule_call(update: Update, context: CallbackContext) -> None:
    # Extract the call time from the message
    time = context.args[0]

    # Schedule the call (you need to implement this part)

    # Notify the group
    update.message.reply_text(f'Llamada programada para {time}.')
