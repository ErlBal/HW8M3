import db.shopdb
from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.types.keyboard_button import KeyboardButton
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.reply_keyboard_remove import ReplyKeyboardRemove
from db.shopdb import get_product_by_category


shop_router = Router()


@shop_router.message(Command("shop"))
async def shop(message: types.Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(text="Купить Фрукты"),
            KeyboardButton(text="Купить Ягоды"),
            KeyboardButton(text="Купить Овощи"),
        ]]

    )
    await message.answer("Выберите категорию: ",
                         reply_markup=kb)

@shop_router.message(F.text == "Купить Фрукты")
async def show_frukt(message: types.Message):
    frukt = get_product_by_category(1)
    kb = ReplyKeyboardRemove()
    await message.answer("Список фруктов:", reply_markup=kb)
    for f in frukt:
        await message.answer(f[1])


@shop_router.message(F.text == "Купить Ягоды")
async def show_yagod(message: types.Message):
    yagod = get_product_by_category(2)
    kb = ReplyKeyboardRemove()
    await message.answer("Список ягод:", reply_markup=kb)
    for y in yagod:
        await message.answer(y[1])


@shop_router.message(F.text == "Купить Овощи")
async def show_ovosh(message: types.Message):
    ovosh = get_product_by_category(3)
    kb = ReplyKeyboardRemove()
    await message.answer("Список овощей:", reply_markup=kb)
    for o in ovosh:
        await message.answer(o[1])