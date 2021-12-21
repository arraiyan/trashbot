
import logging

from telegram import *
from telegram.ext import *
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


API_KEY = '5066917014:AAESOvkyHk2Ug_IIwvmpF2jEtyfoCf5gjCk'

def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    reply_markup = ReplyKeyboardMarkup([['👨‍💻Profile']],resize_keyboard=False)
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )
    # text = '<b>Welcome to our service please have a try..... Wanna know user name Chat Id ha?? hey click the button belowWelcome to our service please have a try..... Wanna know user name Chat Id ha?? hey click the button below</b>'
    text ='<b>⚙️Welcome to our service for User Info. Please click the button below. 🛠</b>'

    update.message.reply_text(text=text,reply_markup=reply_markup,parse_mode='HTML')



def click(update: Update, context: CallbackContext)-> None:
    user = update.message.from_user
    first_name = user.full_name
    user_name = user.username
    user_id = user.id
    update.message.reply_text(f"welcome To the bot \nYour user name is {first_name}  {user_name}\nUser id : @{user_id}")


def echo(update: Update, context: CallbackContext) -> None:
    reply_markup = ReplyKeyboardMarkup([['👨‍💻Profile']],resize_keyboard=False)
    text ='<b>⚙️Welcome to our service for User Info. Please click the button below. 🛠</b>'

    update.message.reply_text(text=text,reply_markup=reply_markup,parse_mode='HTML')


def main() -> None:
    updater = Updater(API_KEY)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.regex(r'👨‍💻Profile'), click ))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
