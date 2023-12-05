from telegram import Update  
from telegram.ext import CallbackContext
from create_poll import create_poll as create_poll_handler

import twitter, nft, database, poll, donation

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome! Type /help for available commands.")

def join(update: Update, context: CallbackContext):
    user = update.message.from_user
    database.add_user(user) 
    update.message.reply_text("You have joined the group!")

def leave(update: Update, context: CallbackContext):
    user = update.message.from_user
    database.remove_user(user)
    update.message.reply_text("You have left the group") 

def create_poll(update: Update, context: CallbackContext):
    # Use the poll handler implemented previously
    create_poll_handler(update, context)
    
def vote(update: Update, context: CallbackContext):
   poll.handle_vote(update)
   
def donate(update: Update, context: CallbackContext):
    donation.process_donation(update.message)
    
def expel(update: Update, context: CallbackContext):
    if not context.bot.get_chat_member(update.effective_chat.id, update.message.from_user.id).status in ["creator", "administrator"]:
        update.message.reply_text("You don't have permission for this!")
        return
    member_id = context.args[0]
    member_name = get_member_name(member_id)
    try:
        context.bot.kick_chat_member(update.effective_chat.id, member_id)
    except:
        update.message.reply_text(f"No se pudo expulsar a {member_name}")
        return
    update.message.reply_text(f"{member_name} ha sido expulsado")

def call_private(update: Update, context: CallbackContext):
    if not context.bot.get_chat_member(update.effective_chat.id, update.message.from_user.id).status in ["creator", "administrator"]:
        update.message.reply_text("You don't have permission for this!")
        return

    result = schedule_telegram_call(update.message)

    if result:
        notify_call_scheduled(update, result['call_time'])
    else:
        update.message.reply_text("No se pudo agendar la llamada")

def call_public(update: Update, context: CallbackContext):
    if not context.bot.get_chat_member(update.effective_chat.id, update.message.from_user.id).status in ["creator", "administrator"]:
        update.message.reply_text("You don't have permission for this!")
        return

    result = twitter.schedule_space(update.message)

    if result:
        notify_call_scheduled(update, result['start_time'])
    else: 
        update.message.reply_text("No se pudo agendar el Twitter Space")

def handle_message(update: Update, context: CallbackContext):
    process_custom_logic(update)

def process_custom_logic(update):
    message = update.message.text

    # Poll commands
    if message.startswith("/poll"):
        return create_poll(update)
        
    # Voting 
    if update.poll:
        return vote(update)

    # Donation    
    if message.startswith("/donate"):
        return donate(update)

    # Membership commands
    if message in ["/join", "/leave"]:
        return eval(message)(update)

    # Moderator commands  
    if message.startswith("/expel"):
        return expel(update)
    
    if message.startswith("/call"):
        return call(update)

    # Default handler
    return handle_message(update)

def handle_message(update: Update, context: CallbackContext):
    # Send help text
    update.message.reply_text("Invalid command. Type /help for available commands.") 
    