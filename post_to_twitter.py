import yaml
import tweepy

with open('config.yaml') as f:
    config = yaml.safe_load(f)

consumer_key = config['twitter']['api_key']
consumer_secret = config['twitter']['api_secret'] 

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

def post_to_twitter(update: Update, context: CallbackContext) -> None:

    content = context.args[0]
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    
    api.update_status(content)
  
    update.message.reply_text('Tweet publicado!')