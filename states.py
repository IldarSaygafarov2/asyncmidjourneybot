from aiogram.dispatcher.filters.state import StatesGroup, State


class PromptStates(StatesGroup):
    PROMPT = State()
