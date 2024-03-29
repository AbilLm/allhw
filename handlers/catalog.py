from aiogram import Router, F, types, Bot
from aiogram.filters import Command
from db.queries import get_catalog, init_db, get_object

get_catalog_router = Router()
catalog_router = Router()

@catalog_router.message(Command("catalog"))
async def show_catalog(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text='Книги'),
                types.KeyboardButton(text='Одежда')
            ],
            [
                types.KeyboardButton(text='Бытовая техника')
            ]


        ],
        realize_keybord=True



    )
    await message.answer("Выберите категорию", reply_markup=kb)

@catalog_router.message(F.text == "Книги")
async def show_book(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(url="https://www.wildberries.ru/catalog/knigi", text="Наши книги")
            ]
        ])

    await message.answer("У нас отличный выбор книг, по низкой цене.Заходи на сайт!", reply_markup=kb)

@catalog_router.message(F.text == "Одежда")
async def show_book(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(url="https://www.wildberries.ru/catalog/0/search.aspx?search=одежда", text="Каталог одежды")
            ]
        ])

    await message.answer("У нас большой выбор стильных, качественных вещей по низкой цене.Залетай!", reply_markup=kb)

@catalog_router.message(F.text == "Бытовая техника")
async def show_book(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(url="https://www.wildberries.ru/catalog/bytovaya-tehnika", text="Бытовая техника")
            ]
        ])

    await message.answer("Перед новым годом всегда есть скидка на быт.технику.Ты знаешь где покупать!", reply_markup=kb)

@get_catalog_router.message(Command('clothes', 'books', 'dish'))
async def show_my_products(message: types.Message):
   objects = get_object(1 if message.text=='clothes' else 2 if message.text=='books' else 3)
   for i in objects:
       await message.answer(
                              text=f'id{i[0]}\n'
                                   f"name{i[1]}\n"
                                   f"amount{i[2]}")

