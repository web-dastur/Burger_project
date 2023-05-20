
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def inline_drink():
    ikm = InlineKeyboardMarkup(row_width=1)
    button = InlineKeyboardButton("🍸 Pepsi", callback_data="pepsi")
    button2 = InlineKeyboardButton("🍹 Fanta", callback_data="fanta")
    button3 = InlineKeyboardButton("🍷 Coca-cola", callback_data="cola")
    button4 = InlineKeyboardButton("⬅ Back to home",callback_data="back_to_home")
    ikm.add(button, button2, button3,button4)
    return ikm




def next_back_inline():
    ikm=InlineKeyboardMarkup()

    btn= InlineKeyboardButton(text=f"Keyingi burger :  ➡️ 🍔️",callback_data="next")
    ikm.add(btn)
    return ikm



