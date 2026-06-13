from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging
import tweepy
import datetime


def start(update, context):
    print("[start]", update.message)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, I'm Alice Bot, I'm in development!")


def document_response(update, context): #to-do: check if document is valid image (same for photo)
    print("[document]", update.message.chat_id)
    if (update.message.chat_id == ""):
        document = update.message.document.get_file()
        global path
        path = document.file_path
        print(path)
        document.download()


def photo_response(update, context):
    print("[photo]", update.message.chat_id)
    if (update.message.chat_id == ""):
        photo = update.message.photo[-1].get_file()
        global path
        path = photo.file_path
        print(path)
        photo.download()


def default_response(update, context):
    print("[default]", update.message.chat_id)
    if (update.message.chat_id == ""):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Ok")


def tweet_response(update, context):
    if (update.message.chat_id == ""):
        print("[tweet]", update.message.chat_id)
        tweet = ' '.join(context.args)
        global path
        send_tweet(tweet, path)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Tweet published!")

        
def unknown(update, context):
    print("[unknown]", update.message.chat_id)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


def send_tweet(tweet="", path=""):
    auth = tweepy.OAuthHandler("", "")
    auth.set_access_token("", "")
    api = tweepy.API(auth)
    print(tweet.replace("#photo", ""))
    if (tweet.find("#photo")==-1):
        api.update_status(tweet)
    else:
        if (path != ""):
            photo = api.media_upload(path.split("/")[-1])
            print(photo)
            print(path)
            api.update_status(tweet.replace("#photo", ""), media_ids=[photo.media_id])
        else:
            api.update_status(tweet.replace("#photo", ""))


path = ""
updater = Updater(token="", use_context=True)
dispatcher = updater.dispatcher
job_q = updater.job_queue
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

dispatcher.add_handler(CommandHandler('start', start))
updater.start_polling()
dispatcher.add_handler(MessageHandler(Filters.document, document_response))
dispatcher.add_handler(MessageHandler(Filters.photo, photo_response))
dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), default_response))
dispatcher.add_handler(CommandHandler('tweet', tweet_response))
dispatcher.add_handler(MessageHandler(Filters.command, unknown))

