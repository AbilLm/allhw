from aiogram import Router, F, types
from aiogram.filters import Command


start_router = Router()

@start_router.message(Command('start'))
async def start(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(url="https://www.wildberries.ru/catalog/knigi/hudozhestvennaya-literatura/komiksy-i-manga", text="Наш каталог"),
                types.InlineKeyboardButton(url='https://www.youtube.com/Wildberriesshop', text='Ютуб'),
            ],
            [
                types.InlineKeyboardButton(url="https://www.wildberries.ru/services/o-nas", text="О нас"),
                types.InlineKeyboardButton(callback_data="about", text="О нас прям в тг")
            ]


        ]


    )


    await message.answer(f"Привет, {message.from_user.username}, мы интернет-магазин WILDBERRIES", reply_markup=kb)

@start_router.callback_query(F.data == "about")
async def about_us(callback: types.CallbackQuery):
    await callback.message.answer("Wildberries - российский онлайн-ритейлер, один из крупнейших в стране. Он предоставляет широкий ассортимент товаров, включая одежду, обувь, электронику, косметику и другие товары. Компания была основана в 2004 году и быстро выросла, став популярным местом для онлайн-шопинга в России. Wildberries известен своей доставкой по всей стране, широким выбором брендов и активной маркетинговой деятельностью.")
