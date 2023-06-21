import asyncio
from datetime import datetime, timedelta
from aiogram.utils import executor
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from rnd import get_rnd_message, hello_msg, msg_list_vst
import time

TOKEN = '5689961299:AAF_cXmUhz-JtWuyF8n8xZzL_kJaNUVFv_4'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def get_video_note(message: types.Message):
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
    asyncio.create_task(get_video_note(message))

@dp.message_handler(commands=['start'])
async def get_video(message: types.Message):
    # make keyboard and video from message
    keyboard = types.InlineKeyboardMarkup()
    video_note = types.InputFile("video_file.mp4")
    button = types.InlineKeyboardButton(text="ПОДРОБНЫЕ УСЛОВИЯ", url="https://github.com")
    keyboard.add(button)
    await bot.send_video_note(message.chat.id, video_note, reply_markup=keyboard)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button = types.InlineKeyboardButton(text="❗️❗️Я НЕ БОТ❗️❗️", callback_data='f')
    keyboard.add(button)
    await message.answer(hello_msg['message'], reply_markup=keyboard, parse_mode=types.ParseMode.HTML)

@dp.message_handler(content_types=['text'])
async def not_bot(message: types.Message):
    if message.text == "❗️❗️Я НЕ БОТ❗️❗️":
        await bot.send_message(message.chat.id, "✅СПАСИБО! ПОДТВЕРЖДЕНИЕ ПОЛУЧЕНО✅")
        
        for msg in msg_list_vst:
            keyboard = types.InlineKeyboardMarkup()
            button = types.InlineKeyboardButton(text=msg['btn_text'], url=msg['url'])
            keyboard.add(button)

            # Отправляем сообщение с кнопкой
            await bot.send_message(message.chat.id, text=msg["message"], reply_markup=keyboard)
            time.sleep(10)
        await get_video_note(message)

if __name__ == '__main__':
    executor.start_polling(dp)
