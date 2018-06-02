import telegram

def main():
  # Get token and connect to BOT
  TOKEN = "353229890:AAFyKlEp8ps6FAj7cChugjvIxYDIklAhmyU"
  chat_id = "127839460"
  bot = telegram.Bot(token=TOKEN)

  # Chat id you can get from upload.py
  # Need to run that program first
  # After that enter command `/id`
  chat_id = "your-chat-id"

  # Enter the image name or you can insert the location of image
  bot.send_photo(chat_id=chat_id, photo=open('win8.png', 'rb'))

if __name__ == '__main__':
 main()
