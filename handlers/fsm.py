from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext



hw3_router = Router()




class Form(StatesGroup):
    name = State()
    age = State()
    gender = State()
    email = State()

@hw3_router.message(Command('start_quest'))
async def start(message: types.Message, state: FSMContext):
    await state.set_state(Form.name)
    await message.answer('Как вас зовут?')

@hw3_router.message(Form.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(f'Здраствуйте, {message.text}')
    await state.set_state(Form.age)
    await message.answer("Сколько вам лет?")

@hw3_router.message(Form.age)
async def pr_age(message: types.Message, state: FSMContext):
    if int(message.text) < 10:
        await message.answer('Вы слишком маленький :)')
        await state.clear()
    else:
        await message.answer('Хорошо.')
    await state.set_state(Form.gender)
    await message.answer('Какой у вас пол?(женщина или мужчина)')

@hw3_router.message(Form.gender)
async def pr_gender(message: types.Message, state: FSMContext):
    await state.update_data(gender=message.text)
    await state.set_state(Form.email)
    await message.answer('Укажите вашу почту')

@hw3_router.message(Form.email)
async def pr_email(message: types.Message, state: FSMContext):
    i = message.text
    if '@' not in i:
        await message.answer('Пожалуйста введите корректный адрес эл.почты')
        return
    await state.update_data(email=i)
    await message.answer('Мы закончили!')
    await state.finish()




