from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router
from keyboards.keyboards import menu, reg,menu_admin
from DATA_BASE.database import database_user
from config import db_name
from aiogram.fsm.context import FSMContext
from States.statess import RegistrState


cmd_co = Router()
@cmd_co.message(Command("start"))
async def cmd_start(msg: Message, state: FSMContext):
    db = database_user(db_name)
    user = db.get_user(msg.from_user.id)
    if user is None:
        db.add_new_user(msg.from_user.id, msg.from_user.last_name, msg.from_user.first_name)
        await msg.answer(text=f"Assalomu Alaykum {msg.from_user.full_name}!\nBotni ishlatish uchun iltimos Ro'yxatdan o'tish tugmasini bosing.", reply_markup=reg)
        await state.set_state(RegistrState.regs)
    elif user[4] is None:
        await msg.answer(text=f"Assalomu Alaykum {msg.from_user.full_name}!\nBotni ishlatish uchun iltimos Ro'yxatdan o'tish tugmasini bosing.", reply_markup=reg)
        await state.set_state(RegistrState.regs)
    elif user[5] == 1:
        await msg.answer(text=f'Assalomu Alaykum {user[2]}!', reply_markup=menu_admin)
    else:
        await msg.answer(text=f"Assalomu Alaykum {user[2]}! ",reply_markup=menu)