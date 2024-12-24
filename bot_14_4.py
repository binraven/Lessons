import asyncio
import conf_bot
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, InputFile
import crud_functions

bot = Bot(token=conf_bot.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


kb = ReplyKeyboardMarkup(resize_keyboard=True)
btn_raschet = KeyboardButton(text="Рассчитать")
btn_info = KeyboardButton(text="Информация")
btn_buy = KeyboardButton(text="Купить") # - Задание 14.3
kb.row(btn_raschet, btn_info)
kb.row(btn_buy) # - Задание 14.3


kb_inline = InlineKeyboardMarkup()
btn_inline_raschet = InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="calories")
btn_inline_formula = InlineKeyboardButton(text="Формулы расчёта", callback_data="formulas")
kb_inline.row(btn_inline_raschet, btn_inline_formula)
#//////////////////////////// Start - Задание 14.3 ///////////////////////////////////////////
kb_inl_buy = InlineKeyboardMarkup(
    inline_keyboard=[
        [KeyboardButton(text="Продукт 1", callback_data="product_buying")],
        [KeyboardButton(text="Продукт 2", callback_data="product_buying")],
        [KeyboardButton(text="Продукт 3", callback_data="product_buying")],
        [KeyboardButton(text="Продукт 4", callback_data="product_buying")]
    ]
)
#///////////////////////////// End - Задание 14.3 ///////////////////////////////////////////



class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()



@dp.message_handler(text="Рассчитать")
async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup=kb_inline)

@dp.callback_query_handler(text="formulas")
async def get_formulas(call):
    await call.message.answer("для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5")
    await call.answer()


@dp.message_handler(commands=["start"])
async def start_message(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=kb)

#//////////////////////////// Start - Задание 14.3 ///////////////////////////////////////////
@dp.message_handler(text="Купить")
async def get_buying_list(message):
    prod = crud_functions.get_all_products()
    for i in prod:
        await bot.send_photo(message.chat.id, caption=f"Название: {i[1]} | Описание: {i[2]} | Цена: {i[3]}"
                             , photo=InputFile('file/prod.png'))
    await message.answer("Выберите продукт для покупки:", reply_markup=kb_inl_buy)

@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()
#///////////////////////////// End - Задание 14.3 ///////////////////////////////////////////





@dp.callback_query_handler(text="calories")
async def set_age(call):
    await call.message.answer("Введите свой возраст:", reply_markup=types.ReplyKeyboardRemove())
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    await message.answer(f"Ваш возраст {data['age']}")
    await message.answer("Введите свой рост:")
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    data = await state.get_data()
    await message.answer(f"Ваш рост {data['growth']}")
    await message.answer("Введите свой вес:")
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    await message.answer(f"Ваши парметры: \n Возраст: {data['age']}"
                         f"\n Рост: {data['growth']}"
                         f"\n Вес: {data['weight']}")
    await message.answer(f"Рассчет калорий: "
                         f"{10 * float(data['weight']) +6.25*float(data['growth']) - 5*float(data['age']) + 5}")
    await state.finish()





if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)