from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import requests
import time
from web3 import Web3, HTTPProvider
import json
from web3 import Web3
import asyncio
w3 = Web3(Web3.HTTPProvider("https://data-seed-prebsc-1-s1.binance.org:8545/"))
w3.eth.get_block('latest')

updater = Updater("5477295799:AAGJgOox03QvGthD0zzhvUEDVyg5Fa36zbA",use_context=True)

print('Bot Is Active')



def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hello sir, Welcome to the Bot.Please write\
        /help to see the commands available.")
  
def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
    /youtube - To get the youtube URL
    /linkedin - To get the LinkedIn profile URL
    /gmail - To get gmail URL
    /geeks - To get the GeeksforGeeks URL""")
  
  
def gmail_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Your gmail link here (I am not\
        giving mine one for security reasons)")
  
def bapbol(update: Update, context: CallbackContext):
    update.message.reply_text(
        "chala ja yaha sai")


def youtube_url(update: Update, context: CallbackContext):
    update.message.reply_text("Youtube Link =>\
    https://www.youtube.com/")
  
  
def linkedIn_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "LinkedIn URL => \
        https://www.linkedin.com/in/dwaipayan-bandyopadhyay-007a/")
  
  
def geeks_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "GeeksforGeeks URL => https://www.geeksforgeeks.org/")
  
  
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)
  
  
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)
  
  
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('bapbol', bapbol))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_url))
updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
updater.dispatcher.add_handler(CommandHandler('geeks', geeks_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown))  # Filters out unknown commands
  
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
value = True
while(value):
    time.sleep(5)
    requests.get('https://api.telegram.org/bot5477295799:AAGJgOox03QvGthD0zzhvUEDVyg5Fa36zbA/sendMessage?chat_id=-600699212&text=this is automatic message sending after 5s')

