from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import random




token = ""
updater = Updater(token , use_context=True)

nosesize = ["voldermort" , "small" , "large" , " XL" , '2XL' , "elephant"]

def start(update: Update, context: CallbackContext):
    size = random.choice(nosesize)
    (update.message.reply_text("you are " + size))


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('nosesize', start))
  
updater.start_polling()

