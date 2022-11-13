# # TODO
# import asyncio
#
# import telebot
# from telebot.types import Message
#
# import config
# import aiohttp
#
# bot = telebot.TeleBot(config.TOKEN)
#
#
# async def get_cat(client: aiohttp.ClientSession) -> bytes:
#     async with client.get(config.CAT_URL) as response:
#         print(response.status)
#         return await response.read()
#         # await write_to_disk(result, idx)
#
#
# async def get_all_cats():
#     async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(15)) as client:
#         tasks = [get_cat(client)]
#         return await asyncio.gather(*tasks)
#
#
# @bot.message_handler(commands=["start"])
# async def start_message(message: "Message"):
#     markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
#     get_cat_button = telebot.types.KeyboardButton("Get Cat")
#     markup.add(get_cat_button)
#     await photo = get_all_cat()
#     bot.send_photo()
