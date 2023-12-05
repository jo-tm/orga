from telegram import Update, Bot, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from tweepy import OAuthHandler, API
from web3 import Web3
from zksync2.module.module_builder import ZkSyncBuilder
from dateutil.parser import parse
from pytz import timezone
from nft import verify_nft
from poll import Poll
from estatuto import Estatuto
from colecta import Colecta
from blacklist import Blacklist

import yaml

with open('config.yaml') as f:
    config = yaml.safe_load(f)

with open('estatuto.yaml') as f:
    estatuto_data = yaml.safe_load(f)

with open('blacklist.yaml') as f:
    blacklist_data = yaml.safe_load(f)

TOKEN = config['telegram']['token']  
TWITTER_API_KEY = config['twitter']['api_key']
TWITTER_API_SECRET_KEY = config['twitter']['api_secret']
TWITTER_ACCESS_TOKEN = config['twitter']['access_token'] 
TWITTER_ACCESS_TOKEN_SECRET = config['twitter']['access_token_secret']  

class Bot:
    def __init__(self, token, twitter_api_key, twitter_api_secret_key, twitter_access_token, twitter_access_token_secret, eth_provider_url, zksync_net_url):
        self.updater = Updater(token=token, use_context=True)
        self.dispatcher = self.updater.dispatcher
        self.twitter_auth = OAuthHandler(twitter_api_key, twitter_api_secret_key)
        self.twitter_auth.set_access_token(twitter_access_token, twitter_access_token_secret)
        self.twitter_api = API(self.twitter_auth)
        self.web3 = Web3(Web3.HTTPProvider(eth_provider_url))
        self.zksync_web3 = ZkSyncBuilder.build(zksync_net_url)
        self.polls = []
        self.estatuto = Estatuto(estatuto_data)
        self.colectas = []
        self.blacklist = Blacklist(blacklist_data)
        self.audio_calls = []

    def start(self):
        self.dispatcher.add_handler(CommandHandler("start", self.start_command))
        self.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, self.message_handler))
        self.updater.start_polling()
        self.updater.idle()

    def start_command(self, update: Update, context: CallbackContext) -> None:
        update.message.reply_text('Bienvenido al bot de la Asociación Civil para Militantes Políticos o Sociales.')

    def message_handler(self, update: Update, context: CallbackContext) -> None:
        message = update.message.text
        # Aquí se manejarán los mensajes recibidos y se llamarán a las funciones correspondientes según el contenido del mensaje.

if __name__ == "__main__":
    bot = Bot(TOKEN, TWITTER_API_KEY, TWITTER_API_SECRET_KEY, 
              TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET,
              config['nodes']['ethereum'], config['nodes']['zksync']) 
    bot.start()
