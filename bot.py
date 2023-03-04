import logging
import telegram
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print('running on github tonight')
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

if __name__ == '__main__':
    application = ApplicationBuilder().token('6145570522:AAGwIUe5LiaEtXSvFan99bZ_02jcS1rXzh8').build()
    # application._proxy_url = "socks5://127.0.0.1:12123"
    # application = application.build()
    # request_client = telegram.request.HTTPXRequest(proxy_url="socks5://127.0.0.1:12123")
    # bot = telegram.Bot("6145570522:AAGwIUe5LiaEtXSvFan99bZ_02jcS1rXzh8", request=request_client)
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    application.run_polling()
