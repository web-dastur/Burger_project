import random
from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove


from keyboards.default.default_button import pepsi_capacity, fanta_capacity, cola_capacity, burger_default_button, \
    menyu_inner, get_backet
from keyboards.inline.inline_burger_button import inline_drink, next_back_inline
from loader import dp, bot


@dp.message_handler(Text(equals="⬅️Back to home"))
async def pepsi_05(message:types.Message):
    await message.answer(text="Bekor qilindi !",
                         reply_markup=burger_default_button())


@dp.message_handler(Text(equals = "🍹 Ichimliklar"))
async def get_menyu(message:types.Message):
    await message.answer(text="Bizning ichimliklar ",
                         reply_markup=inline_drink())


@dp.message_handler(Text(equals="⏪ Back to home"))
async def lavash_big(message:types.Message):
    await message.answer(text="Bekor qilindi !",
                         reply_markup=menyu_inner())



BURGER_URL=["https://iqtidor.uz//files/fotki/hamburger-fries.jpg",
          "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Cheeseburger.jpg/1200px-Cheeseburger.jpg",
          "https://domesticallyblissful.com/wp-content/uploads/2018/06/Grilled-Brown-Sugar-Glazed-Pineapple-Veggie-Burgers.jpg"]


BURGERS=dict(zip(BURGER_URL, ["\n🍔 Gamburger\n\n Tarkibi : Bulochka, Kotlet, Piyoz, Pomidor, Tuzlangan bodring, Salat bargiFirmenniy sous !\n\nNarxi : 22.000 so'm\n" ,

                              "\n🍔 Chizburger\n\n Tarkibi : Bulochka, Kotlet, Pishloq Hochland, Piyoz, Pomidor, Tuzlangan bodring, Salat bargi  Firmenniy sous, Pishloqli sous!\n\nNarxi : 25.000 so'm\n",

                        "\n🍔 Ananas Burger\n\n Tarkibi : Bulochka,Kotlet, Qo'ziqorinli ragu, Ananas, Salat bargi, Pomidor, Tuzlangan bodring, Pishloqli sous, Kotlet sousi!\n\nNarxi : 40.000 so'm\n"
                              ]))




#
@dp.message_handler(Text(equals="⬅️Back to home"))
async def pepsi_05(message:types.Message):
    await message.answer(text="Bekor qilindi !",
                         reply_markup=burger_default_button())

@dp.message_handler(Text(equals='🍔 Burger'))
async def burger_big(message:types.Message):
    global random_photo
    random_photo = random.choice(list(BURGERS.keys()))
    await message.answer(text="Burgerlar",
                         reply_markup=get_backet())
    await bot.send_photo(chat_id=message.chat.id,
                         photo=random_photo,
                         caption=BURGERS[random_photo],
                         reply_markup=next_back_inline())



@dp.callback_query_handler()
async def call_back_func(callback:types.CallbackQuery):
    if callback.data=="pepsi":
        await callback.message.answer(text="Pepsi turlari",
                                      reply_markup=pepsi_capacity())

    elif callback.data=="fanta":
        await callback.message.answer(text="Fanta turlari",
                                      reply_markup=fanta_capacity())


    elif callback.data=="cola":
        await callback.message.answer(text="Cola turlari",
                                      reply_markup=cola_capacity())

    elif callback.data=="back_to_home":
        await callback.message.answer(text="Bekor qilindi",
                                      reply_markup=menyu_inner())


    elif "next" == callback.data:
        global random_photo
        random_photo = random.choice(list(filter(lambda x: x != random_photo, list(BURGERS.keys()))))
        await callback.message.edit_media(types.InputMedia(media=random_photo,
                                                           type="photo",
                                                           caption=BURGERS[random_photo]
                                                           ), reply_markup=next_back_inline())
        await callback.answer()









@dp.message_handler(Text(equals="🍷 0.5 litr"))
async def pepsi_05(message:types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://devel.prom.uz/upload/products/60/98/60988e6c799e5067b5232a3b98fe6397.jpg",
                         caption="<em><b>Miqdori : 0.5 litr\n"
                                 "Narxi : 7000 ming so'm </b></em>\n",
                         reply_markup=pepsi_capacity(),)


@dp.message_handler(Text(equals="🍷 1 litr"))
async def pepsi_05(message:types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://1119001045.rsc.cdn77.org/wa-data/public/shop/products/87/30/3087/images/2239/Napitok_Gazirovannyy_Pepsi_10_l.650@2x.jpg",
                         caption="<em><b>Miqdori : 1 litr\n"
                                 "Narxi : 10.000 ming so'm </b></em>\n",
                         reply_markup=pepsi_capacity(),
                         )


@dp.message_handler(Text(equals="🍷 1.5 litr"))
async def pepsi_05(message:types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://catalog.milliykatalogi.uz/s3/med/be3c33ed-463a-91b9-d15c-523a24e507ba.jpg",
                         caption="<em><b>Miqdori : 1.5 litr\n"
                                 "Narxi : 12.000 ming so'm </b></em>\n",
                         reply_markup=pepsi_capacity(),
                         )



@dp.message_handler(Text(equals="🍹  0.5 litr"))
async def pepsi_05(message:types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://sambazar.uz/upload-file/2021/01/17/20136/750x750-3baeea84-3e36-42d2-914d-d274a03ea14f.png",
                         caption="<em><b>Miqdori : 0.5 litr\n"
                                 "Narxi : 7000 ming so'm </b></em>\n",
                         reply_markup=fanta_capacity(),)


@dp.message_handler(Text(equals="🍹  1 litr"))
async def pepsi_05(message:types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://bozor.com/media/filer_public/40/7b/407be902-11c3-453d-8506-fc1c9d5d7ff0/fanta-1.jpg",
                         caption="<em><b>Miqdori : 1 litr\n"
                                 "Narxi : 10.000 ming so'm </b></em>\n",
                         reply_markup=fanta_capacity(),
                         )


@dp.message_handler(Text(equals="🍹  1.5 litr"))
async def pepsi_05(message:types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://web.lebazar.uz/resources/product/2020/3/14/medium_1586858421530Fanta15.jpg",
                         caption="<em><b>Miqdori : 1.5 litr\n"
                                 "Narxi : 12.000 ming so'm </b></em>\n",
                         reply_markup=fanta_capacity(),
                         )








@dp.message_handler(Text(equals="🍸 0.5 litr"))
async def pepsi_05(message:types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://i.siteapi.org/6AW0nvO_NnPc87NC7VKA2yyQgW0=/fit-in/1024x768/center/top/a99ebf267115222.s.siteapi.org/img/79d36ef16a5b5e5f6627c6ca9fa73843b33b02cf.jpg",
                         caption="<em><b>Miqdori : 0.5 litr\n"
                                 "Narxi : 7000 ming so'm </b></em>\n",
                         reply_markup=cola_capacity(),)


@dp.message_handler(Text(equals="🍸 1 litr"))
async def pepsi_05(message:types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://images.uzum.uz/cd8ki8v0tgqvlm58tiug/original.jpg",
                         caption="<em><b>Miqdori : 1 litr\n"
                                 "Narxi : 10.000 ming so'm </b></em>\n",
                         reply_markup=cola_capacity(),
                         )


@dp.message_handler(Text(equals="🍸 1.5 litr"))
async def pepsi_05(message:types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://babymarket.uz/wp-content/uploads/2020/07/coca-cola-15-l.jpg",
                         caption="<em><b>Miqdori : 1.5 litr\n"
                                 "Narxi : 12.000 ming so'm </b></em>\n",
                         reply_markup=cola_capacity(),
                         )









