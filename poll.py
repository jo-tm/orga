import datetime
import database

from telegram import Update, Poll  
from telegram.ext import CallbackContext

class Poll:

    def __init__(self, title, creator, duration, db_id=None):
        self.id = db_id
        self.title = title
        self.creator = creator
        self.created_at = datetime.datetime.now()
        self.duration = duration  
        self.options = []
        self.status = 'creation'

        self.vote_poll = None

    def save(self):
        database.save_poll(self)

    @staticmethod
    def get(poll_id):
        poll_data = database.get_poll(poll_id)
        return Poll(**poll_data)

    def add_option(self, option):
        if self.status != 'creation':
            return

        self.options.append(option)
        self.save()

    def start_vote(self):
        options = "/" + "/".join(self.options) + "/"  
        self.vote_poll = Poll(self.title, options)
        self.vote_poll.create(...) 
        self.status = 'voting'
        self.save()

    def handle_vote(self, update):
        if self.vote_poll:
            option = update.poll.option_ids[0]
            if option == "/cancel":
                return
                
            # Registrar voto  
            selected_option = self.options[option] 
            selected_option.votes += 1
            self.save()

    def is_expired(self):
        now = datetime.datetime.now()
        expires_at = self.created_at + datetime.timedelta(hours=self.duration)
        return now > expires_at

def receive_option(update, context):
    poll = Poll.get(context.args[0])
    option = update.message.text
    
    poll.add_option(option) 
    
def receive_vote(update, context):
    poll = Poll.get(context.args[0])
    option = update.poll.option_ids[0]
    
    if poll.vote_poll:
        poll.handle_vote(update)