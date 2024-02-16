from datetime import date
from aiogram import Router,F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from keyboards.keyboards import reg, phone, menu

reg_router = Router()
from DATA_BASE.database import database_user
from config import db_name
from States.statess import RegistrState

db = database_user(db_name)
@reg_router.message(RegistrState.regs)
async def start(msg: Message, state: FSMContext):
    user = db.get_user(msg.from_user.id)
    if user[4]:
        await msg.answer("Siz ro'yxatdan o'tkansiz!")
    elif msg.text == "Ro'yxatdan o'tish":
        await msg.answer('Keling unda ro\'yxatdan o\'tishni boshlaymiz. "Telefon raqamni yuborish" tugmasini bosing: ',reply_markup=phone)
        await state.set_state(RegistrState.regPhone)
    else:
        await msg.answer("Botni ishlatish uchun iltimos Ro'yxatdan o'tish tugmasini bosing.", reply_markup=reg)
        await state.set_state(RegistrState.regs)
@reg_router.message(RegistrState.regPhone)
async def reg_phone(msg: Message, state: FSMContext):
    try:
        regphone=msg.contact.phone_number
        db.update_user(msg.from_user.id,regphone)
        await msg.answer(text="Yaxshi endi botdan foydalanishingiz mumkun: ",reply_markup=menu)
        await state.set_state(RegistrState.menu)
    except:
        await msg.answer('"Telefon raqamni yuborish" tugmasini bosing: ',reply_markup=phone)

@reg_router.message()
async def unknown_command(msg: Message):
    await msg.answer(text="Xatolik\nIltimos botni qayta ishga tushuring. /start")
