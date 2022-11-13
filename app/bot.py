import telebot
from telebot.types import Message, ReplyKeyboardMarkup

import config
from api.cats import GET_CAT_BUTTON, get_cat
from api.dogs import GET_DOG_BUTTON, get_dog

bot = telebot.TeleBot(config.TOKEN)


def generate_markup() -> "ReplyKeyboardMarkup":
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    get_cat_button = telebot.types.KeyboardButton(GET_CAT_BUTTON)
    get_dog_button = telebot.types.KeyboardButton(GET_DOG_BUTTON)
    markup.add(*[get_cat_button, get_dog_button])
    return markup


@bot.message_handler(commands=["start"])
def start_message(message: "Message") -> None:
    markup = generate_markup()
    text = f"Hello {message.from_user.full_name}, push button to get a cat or dog!"
    bot.send_message(message.chat.id, text, reply_markup=markup)


@bot.message_handler(regexp=GET_CAT_BUTTON)
def get_cat_bot(message: "Message") -> None:
    content = get_cat()
    markup = generate_markup()
    bot.send_photo(message.chat.id, content, reply_markup=markup)


@bot.message_handler(regexp=GET_DOG_BUTTON)
def get_cat_bot(message: "Message") -> None:
    content = get_dog()
    markup = generate_markup()
    bot.send_photo(message.chat.id, content, reply_markup=markup)
