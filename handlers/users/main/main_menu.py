from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards.default.default_button import menyu_inner, burger_default_button, fast_food_inner, lavash_food
from keyboards.inline.inline_burger_button import inline_drink
from loader import dp, bot


@dp.message_handler(Text(equals = "🍽️ Menyu"))
async def get_menyu(message:types.Message):
    await message.answer(text="Bizning mahsulotlar ",
                         reply_markup=menyu_inner())



@dp.message_handler(Text(equals="🚁 Buyurtma haqida"))
async def get_buyurtma(message: types.Message):
    await message.answer(text="<b><em>Bepul yetkazib berish xizmati 2 kmgacha va soat 09:00 dan 23:00 gacha davom etadi.\n\n"
                              " Undan keyin yetkazib berish xizmati 🚕 Taxi tomonidan amalga oshiriladi va alohida to'lanadi.\n\n"

            "🚕 Taxi yetkazib berish xizmatining narxi bizlarga bog'liq emas!\n\n"

           " Sizning buyurtmangiz taxminan 45 minut ichida yetkazib beriladi</em></b>\n\n",

                         parse_mode="HTML",
                         reply_markup=burger_default_button())




@dp.message_handler(Text(equals="☎ Kontaktlar"))
async def get_contact(message: types.Message):
    await message.answer(text=f"<b><em>📞 Buyurtma va boshqa savollar bo'yicha javob olish uchun +998992990005 "
                              f"yoki +998919210005 murojaat qiling, barchasiga javob beramiz !!!!</em></b>",
                         parse_mode="HTML",
                         reply_markup=burger_default_button())



@dp.message_handler(Text(equals="🔎 Kafe lokatsiya"))
async def location(message: types.Message):
    await bot.send_location(chat_id=message.chat.id,
                            latitude=38.8611918,
                            longitude=65.7847269,reply_markup=burger_default_button())







@dp.message_handler(Text(equals="🥙 Doner"))
async def doner_func(message: types.Message):
    await message.answer_photo(photo="https://media.istockphoto.com/id/851493796/photo/close-up-of-kebab-sandwich.jpg?s=612x612&w=0&k=20&c=gSQ8R-L2J1i0RCPJFXB-vYdWaB4wUcL8I8UAzpjSWVw=",
                               caption=f"<b><em>Tarkibi : </em></b> <b> Go'sht, bulochka, salat mix, oq sous, qizil sous\n\n"
                                       f"Narxi: 26 000 so'm </b>",
                               parse_mode="html")


@dp.message_handler(Text(equals="🌮 Hot-Dog"))
async def hot_dog_func(message: types.Message):
    await message.answer_photo(photo="https://zira.uz/wp-content/uploads/2020/09/khot-dog-2.jpg",
                               caption=f"<b><em>Tarkibi : </em></b> <b> Bulochka, 1-Kanada sherin sosiska, Chimchi, Svikla, Svejiy salat\n\n"
                                       f"Narxi: 17 000 so'm </b>",
                               parse_mode="html")




@dp.message_handler(Text(equals="⬅ back to home"))
async def lavash_big(message: types.Message):
    await message.answer(text="Bekor qilindi !",
                         reply_markup=fast_food_inner())


@dp.message_handler(Text(equals='🌯 Lavash'))
async def lavash_big(message: types.Message):
    await message.answer(text="Lavashlar",
                         reply_markup=lavash_food())


@dp.message_handler(Text(equals="🌯 Lavash(Standart)"))
async def lavash_standart_func(message:types.Message):
    await message.answer_photo(photo="https://i.ytimg.com/vi/L-w8IwloI78/maxresdefault.jpg",
                               caption=f"<b><em>🌯 Lavash</em></b> \n"

                                "<b>Tarkibi : Lavash noni, Go'sht, Salat ayzberg, Pomidor, Qizil SousFirmenniy sous    \n\n"
                                f"Narxi: 25 000 so'm </b>",
                               parse_mode="html")


@dp.message_handler(Text(equals="🌯 Tandir Lavash"))
async def lavash_tandir_func(message:types.Message):
    await message.answer_photo(photo="https://pasta.uz/upload/products/OL%20x%20Pasta%20Tandir%20lavash.jpg",
                               caption=f"<b><em>🌯 Tandir Lavash</em></b> \n"

                                "<b>Tarkibi : Lavash noni, Pomidor, Chesnok, Pishloq Mazzarella, Go'sht,"
                                "Qizil sous, Firmenniy sous     \n\n"
                                f"Narxi: 25 000 so'm </b>",
                               parse_mode="html")


@dp.message_handler(Text(equals="🌯 Fast-Food"))
async def fast_food_func(message:types.Message):
    await message.answer(text="Fast-Food mahsulotlari",
                         reply_markup=fast_food_inner())

