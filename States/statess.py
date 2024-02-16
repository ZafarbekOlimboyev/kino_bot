from aiogram.fsm.state import State,StatesGroup

class RegistrState(StatesGroup):
    regPhone = State()
    find_kino = State()
    menu = State()
    regs = State()
    admin_mode = State()