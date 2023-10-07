from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.types.inline_keyboard_button import InlineKeyboardButton as IButton
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from text1 import START_TEXT
from text2 import BUTTON_TEXT
from db.shopdb import save_question, fcars
from bot import bot
from datetime import timedelta, datetime


admin_router = Router()

@admin_router.message()
async def banw(message: types.Message):
    administrators = await bot.get_chat_administrators(message.chat.id)
    admin_ids = [admin.user.id for admin in administrators]
    banword = ['тест', 'аы']
    for b in banword:
        if message.text is not None and b in message.text and message.from_user.id\
                not in admin_ids:
            kb = InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        IButton(text="Забанить!!!", callback_data=f'ban {message.from_user.id}'),
                    ],
                ]
            )
            await message.reply('Забанить?', reply_markup=kb)

@admin_router.callback_query(lambda query: query.data.startswith('ban'))
async def callban(query: types.CallbackQuery):
    user_id = query.data.replace('ban ', '')
    administrators = await bot.get_chat_administrators(query.message.chat.id)
    admin_ids = [admin.user.id for admin in administrators]
    if query.from_user.id in admin_ids:
        await bot.ban_chat_member(chat_id=query.message.chat.id, user_id=user_id, until_date=datetime.now()+timedelta(minutes=1))

