from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from decouple import config
import logging


TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await bot.send_message(message.chat.id, f"йоу это домашка_1 {message.from_user.full_name}")

@dp.message_handler(commands=['end'])
async def hello(message: types.Message):
    await bot.send_message(message.chat.id, f"10? получил или нет?((  {message.from_user.full_name}")


@dp.message_handler(commands=['stop'])
async def hello(message: types.Message):
    await bot.send_message(message.chat.id, f"все таки получил? {message.from_user.full_name}")




@dp.message_handler(commands=['mem'])
async def mem(message:types.Message):
    photo = open('media1/brawlstars1.jfif', "rb")
    await bot.send_photo(message.chat.id, photo=photo)

    photo = open('media1/brawlstars2.jfif', "rb")
    await bot.send_photo(message.chat.id, photo=photo)


@dp.message_handler(commands=['quiz1'])
async def quiz_1(message: types.Message):
    murkup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton(
        "NEXT",
        callback_data="button_call_1"
    )
    murkup.add(button_call_1)

    photo = open("media1/brawlstars2.jfif", "rb")
    await bot.send_photo(message.chat.id, photo=photo)


    question = "сколько пальцев на руке?:"
    answers = ['1', '2', '4', '3', "5?"]
    await bot.send_poll(message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=4,
                        open_period=10,
                        reply_markup=murkup
                        )



@dp.message_handler(commands=['quiz2'])
async def quiz_2(message: types.Message):
    markup1 = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton(
        "NEXT",
        callback_data="button_call_2"
    )
    markup1.add(button_call_2)

    photo = open("media1/brawlstars1.jfif", "rb")
    await bot.send_photo(message.chat.id, photo=photo),


    question = "H2O или СО2?"
    answers = ['co2', 'H2O']
    await bot.send_poll(message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=1,
                        open_period=10,
                        reply_markup=markup1
                        )




@dp.message_handler(commands=['quiz3'])
async def quiz_3(message: types.Message):
    markup2 = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton(
        "NEXT",
        callback_data="botton_call_3"
    )
    markup2.add(button_call_3)

    photo = open("media1/brawlstars1.jfif", "rb")
    await bot.send_photo(message.chat.id, photo=photo),


    question = "Python or JavaScripts?"
    answers = ['JavaScripts', 'Python']
    await bot.send_poll(message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=1,
                        open_period=10,
                        reply_markup= markup2
                        )

#
# @dp.message_handler(commands=['quiz4'])
# async def quiz_4(message: types.Message):
#     markup3 = InlineKeyboardMarkup()
#     button_call_4 = InlineKeyboardButton(
#         "NEXT",
#         callback_data="botton_call_4"
#     )
#      markup3.add(button_call_4)
#
#      photo = open("media1/brawlstars2.jfif", "rb")
#      await bot.send_photo(message.chat.id, photo=photo),
#
#
#     question = "Как называется упорядоченное движение заряженных частиц??"
#     answers = ['Электрический ток', 'Реакция', 'Растворение']
#     await bot.send_poll(message.chat.id,
#                         question=question,
#                         options=answers,
#                         is_anonymous=False,
#                         type='quiz',
#                         correct_option_id=0,
#                         open_period=10,
#                         # reply_markup=markup3
#                         # )


@dp.message_handler()
async def echo_message(message: types.Message):
    if message.text.isdigit():
        a = int(message.text)
        await message.answer( a ** 2 )
    else:
        await message.answer(message.text)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False)
