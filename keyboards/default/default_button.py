from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import dp


def burger_default_button():
    rkm=ReplyKeyboardMarkup(resize_keyboard=True,
                            one_time_keyboard=True,row_width=2)

    button = KeyboardButton(text="🍽️ Menyu")
    button1 = KeyboardButton(text="🔎 Kafe lokatsiya")
    button2 = KeyboardButton(text="🚁 Buyurtma haqida")
    button3 = KeyboardButton(text="☎ Kontaktlar ")
    button4 = KeyboardButton(text="🗑️ Savatga olish")
    rkm.add(button, button1, button2, button3, button4)
    return rkm


def menyu_inner():
    rkm=ReplyKeyboardMarkup(resize_keyboard=True,
                            one_time_keyboard=True,
                            row_width=2)

    button = KeyboardButton(text="🌯 Fast-Food")
    button1 = KeyboardButton(text="🍔 Burger")
    button2 = KeyboardButton(text="🍹 Ichimliklar")
    button3 = KeyboardButton("⬅️Back to home")
    button4 = KeyboardButton("🗑️ Savatga qo'shish")
    rkm.add(button, button1, button2, button3, button4)
    return rkm


def pepsi_capacity():

    rkm = ReplyKeyboardMarkup(resize_keyboard=True,
                              one_time_keyboard=True,
                              row_width=3)
    button = KeyboardButton("🍷 0.5 litr")
    button2 = KeyboardButton("🍷 1 litr")
    button3 = KeyboardButton("🍷 1.5 litr")
    button4 = KeyboardButton("⬅️Back to home")
    button5 = KeyboardButton("🗑️ Savatga qo'shish")
    rkm.add(button, button2, button3,button4,button5)
    return rkm


def cola_capacity():

    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton("🍸 0.5 litr")
    button2 = KeyboardButton("🍸 1 litr")
    button3 = KeyboardButton("🍸 1.5 litr")
    button4 = KeyboardButton("⬅️Back to home")
    button5 = KeyboardButton("🗑️ Savatga qo'shish")
    rkm.add(button, button2, button3,button4,button5)
    return rkm

def fanta_capacity():

    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton("🍹  0.5 litr")
    button2 = KeyboardButton("🍹  1 litr")
    button3 = KeyboardButton("🍹  1.5 litr")
    button4 = KeyboardButton("⬅️Back to home")
    button5 = KeyboardButton("🗑️ Savatga qo'shish")
    rkm.add(button, button2, button3,button4, button5)
    return rkm


def fast_food_inner():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    button=KeyboardButton("🥙 Doner")
    button2=KeyboardButton("🌮 Hot-Dog")
    button4=KeyboardButton("🌯 Lavash")
    button5 = KeyboardButton("⏪ Back to home")
    button6 = KeyboardButton("🗑️ Savatga qo'shish")
    rkm.add(button, button2, button4, button5,button6)
    return rkm


def lavash_food():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    button=KeyboardButton("🌯 Lavash(Standart)")
    button2=KeyboardButton("🌯 Tandir Lavash")
    button3 = KeyboardButton("⬅ back to home")
    button4 = KeyboardButton("🗑️ Savatga qo'shish")
    rkm.add(button,button2, button3, button4)
    return rkm


def get_backet():

    rkm = ReplyKeyboardMarkup(resize_keyboard=True,
                              one_time_keyboard=True)
    button = KeyboardButton("⏪ Back to home")
    button2 = KeyboardButton("🗑️ Savatga qo'shish")
    rkm.add(button, button2)
    return rkm






