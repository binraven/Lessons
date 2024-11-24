import asyncio
import conf_bot
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

bot = Bot(token=conf_bot.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=["start"])
async def start_message(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.")

@dp.message_handler(text="Calories")
async def set_age(message):
    await message.answer("Введите свой возраст:")
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