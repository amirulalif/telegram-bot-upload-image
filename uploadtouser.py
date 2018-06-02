import telegram

def main():
  # Get token and connect to BOT
  TOKEN = "your-token"
  bot = telegram.Bot(token=TOKEN)

  # Chat id you can get from upload.py
  # Need to run that program first
  # After that enter command `/id`
  chat_id = "your-chat-id"

  # Enter the image name or you can insert the location of image
  bot.send_photo(chat_id=chat_id, photo=open('win8.png', 'rb'))

if __name__ == '__main__':
 main()
