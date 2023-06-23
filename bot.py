import asyncio
from datetime import datetime, timedelta
from aiogram.utils import executor
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from rnd import get_rnd_message, hello_msg, msg_list_vst
import time


TOKEN = '6271039152:AAG6Va9SDCKXVitD-7lPxr7__nmgzqzrSqo'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.chat_join_request_handler()
async def get_video(update: types.ChatJoinRequest):
    # make keyboard and video from message
    keyboard = types.InlineKeyboardMarkup()
    video_note = types.InputFile("video_file.mp4")
    button = types.InlineKeyboardButton(text="ПОДРОБНЫЕ УСЛОВИЯ", url="https://github.com")
    keyboard.add(button)
    await bot.send_video_note(update.from_user.id, video_note, reply_markup=keyboard)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button = types.InlineKeyboardButton(text="❗️❗️Я НЕ БОТ❗️❗️", callback_data='button_click')
    keyboard.add(button)
    await bot.send_message(update.from_user.id, text=hello_msg['message'], reply_markup=keyboard, parse_mode=types.ParseMode.HTML)
    await update.approve()


@dp.message_handler(content_types=['text'])
async def not_bot(message: types.Message):
    if message.text == "❗️❗️Я НЕ БОТ❗️❗️":
        await bot.send_message(message.from_user.id, "✅СПАСИБО! ПОДТВЕРЖДЕНИЕ ПОЛУЧЕНО✅")

        for msg in msg_list_vst:
            keyboard = types.InlineKeyboardMarkup()
            button = types.InlineKeyboardButton(text=msg['btn_text'], url=msg['url'])
            keyboard.add(button)

            # Отправляем сообщение с кнопкой
            await bot.send_message(message.from_user.id, text=msg["message"], reply_markup=keyboard)
            time.sleep(10)
        await get_msg_note(message)


async def get_msg_note(message: types.Message):
    # Получаем текущее время
    now = datetime.now()
    print(now)

    msg = get_rnd_message()

    # Создаем объект InlineKeyboardMarkup и добавляем кнопку
    keyboard = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text=msg['btn_text'], url=msg['url'])
    keyboard.add(button)

    # Вычисляем время следующей отправки сообщения (в данном примере - через сутки)
    next_time = now + timedelta(days=1)
    print(next_time)

    # Отправляем сообщение с кнопкой
    await bot.send_message(message.chat.id, text=msg["message"], reply_markup=keyboard)

    print((next_time - datetime.now()).total_seconds())
    # Запускаем таймер на следующую отправку сообщения
    await asyncio.sleep((next_time - datetime.now()).total_seconds())
    asyncio.create_task(get_msg_note(message))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)