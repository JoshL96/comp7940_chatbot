from telegram import Update
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, CallbackContext)
#import configparser
import logging
import redis
from ChatGPT_HKBU import HKBU_ChatGPT
import os
#global redis1
global chatgpt
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
def main():
    # Load your token and create an Updater for your Bot
    #config = configparser.ConfigParser()
    #config.read('config.ini')
    updater = Updater(token=(os.environ['ACCESS_TOKEN']), use_context=True)
    dispatcher = updater.dispatcher
    #global redis1
    #redis1 = redis.Redis(host=(config['REDIS']['HOST']),
    #                     password=(config['REDIS']['PASSWORD']),
    #                     port=(config['REDIS']['REDISPORT']))
    # You can set this logging module, so you will know when
    # and why things do not work as expected Meanwhile, update your config.ini as:
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    # register a dispatcher to handle message: here we register an echo dispatcher
    #echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    #dispatcher.add_handler(echo_handler)

    global chatgpt
    chatgpt = HKBU_ChatGPT(os)
    chatgpt_handler = MessageHandler(Filters.text & (~Filters.command), equiped_chatgpt)
    dispatcher.add_handler(chatgpt_handler)

    # 注册错误处理程序
    dispatcher.add_error_handler(error_handler)

    # on different commands - answer in Telegram
    #dispatcher.add_handler(CommandHandler("add", add))
    #dispatcher.add_handler(CommandHandler("help", help_command))
    # To start the bot:
    updater.start_polling()
    updater.idle()

#def echo(update, context):
#    reply_message = update.message.text.upper()
#    logging.info("Update: " + str(update))
 #   logging.info("context: " + str(context))
 #   context.bot.send_message(chat_id=update.effective_chat.id, text= reply_message)

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
#def help_command(update: Update, context: CallbackContext) -> None:
#    """Send a message when the command /help is issued."""
#    update.message.reply_text('Helping you helping you.')

#def add(update: Update, context: CallbackContext) -> None:
#    """Send a message when the command /add is issued."""
 #   try:
  #      global redis1
  #      logging.info(context.args[0])
  #      msg = context.args[0] # /add keyword <-- this should store the keyword
  #      redis1.incr(msg)
#
  #      update.message.reply_text('You have said ' + msg + ' for ' +
  #                      redis1.get(msg).decode('UTF-8') + ' times.')
  #  except (IndexError, ValueError):
 #       update.message.reply_text('Usage: /add <keyword>')

def equiped_chatgpt(update, context):
    global chatgpt
    try:
        reply_message = chatgpt.submit(update.message.text)
        logging.info("Update: " + str(update))
        logging.info("context: " + str(context))

         # 提取 Response 对象中的内容并转换为字符串
        reply_text = reply_message[0]
        context.bot.send_message(chat_id=update.effective_chat.id, text=reply_message)
    except Exception as e:
        logging.error("An error occurred while processing the message: %s", str(e))


def error_handler(update, context):
    """Log Errors caused by Updates."""
    logging.error("Exception while handling an update:", exc_info=context.error)


if __name__ == '__main__':
    main()
