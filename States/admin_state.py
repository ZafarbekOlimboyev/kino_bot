from aiogram.fsm.state import State,StatesGroup

class AdminState(StatesGroup):
    upload_movie = State()
    file_id = State()
    about = State()
    key = State()