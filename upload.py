from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(bot, update):
  bot.send_message(chat_id=update.message.chat_id, text="Hello there")

def upload(bot, update):
  bot.send_photo(chat_id=update.message.chat_id, photo=open('win8.png', 'rb'))

def gid(bot, update):
  bot.send_message(chat_id=update.message.chat_id, text=update.message.chat_id)

def main():
  # Create Updater object and attach dispatcher to it
  TOKEN = "353229890:AAFyKlEp8ps6FAj7cChugjvIxYDIklAhmyU"
  updater = Updater(TOKEN)
  dispatcher = updater.dispatcher
  print("Waiting for command")

  # Add command handler to dispatcher
  start_handler = CommandHandler('start',start)
  dispatcher.add_handler(start_handler)

  # Add image to bot
  image = CommandHandler('image',upload)
  dispatcher.add_handler(image)

  # Get chat id with current bot
  cid = CommandHandler('id',gid)
  dispatcher.add_handler(cid)

  # Start the bot
  updater.start_polling()

  # Run the bot until you press Ctrl-C
  updater.idle()

if __name__ == '__main__':
 main()
