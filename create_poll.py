from telegram import Update
from telegram.ext import CallbackContext
from poll import Poll 

active_polls = []

def create_poll(update: Update, context: CallbackContext) -> None:
    title, options, creation_time, voting_time = context.args

    poll = Poll(title, options, update.message.from_user, creation_time, voting_time)
    
    message = context.bot.send_poll(
        update.effective_chat.id, 
        question=poll.title,
        options=poll.options,
        is_anonymous=False,
        allows_multiple_answers=True,
    )
    
    poll.message_id = message.message_id
    active_polls.append(poll)

    update.message.reply_text(f'Nueva encuesta creada: {title}')


def receive_poll_vote(update: Update, context: CallbackContext) -> None:
    for poll in active_polls:
        if update.poll.id == poll.message_id:
            # Register vote on poll object
            break