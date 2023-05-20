from aiogram.dispatcher.filters.state import StatesGroup, State


class AddProductState(StatesGroup):
    title = State()
    description=State()
    price = State()
    categories= State()
    photo = State()


class DeleteProductState(StatesGroup):
    id = State()


class GetProductState(StatesGroup):
    id = State()









