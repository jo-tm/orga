import config
from colecta import Colecta
from telegram import Update
from telegram.ext import CallbackContext

treasury = Colecta(config.ZKSYNC_PROVIDER, config.DONATION_WALLET)
last_balance = 0

def handle_donation(update: Update, context: CallbackContext):

    donation = Donation(update.message)  
    donation.save()

    balance = treasury.get_balance()
    delta = balance - last_balance

    if delta > 0:
        text = f"Nueva donación! Saldo total: {balance} (+{delta})"
        context.bot.sendMessage(chat_id=config.GROUP_ID, text=text) 

    last_balance = balance

class Donation:
    def __init__(self, message):
        # Extraer monto del mensaje
        pass
    
    def save(self):
        # Persistir donación
        pass