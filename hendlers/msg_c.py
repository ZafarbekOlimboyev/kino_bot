from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from States.statess import RegistrState
from config import db_name
from functions.send_kino import send_video,get_id
from keyboards.keyboards import orqaga, menu
from DATA_BASE.database import database_movie

msg_co = Router()

@msg_co.message(F.text == "Kino izlash")
async def kino(msg: Message, state: FSMContext):
    await msg.answer(text="Kino kodini kiriting: ",reply_markup=orqaga)
    await state.set_state(RegistrState.find_kino)

@msg_co.message(RegistrState.find_kino)
async def example(msg: Message, state: FSMContext):
    if msg.text.isdigit():
        file_id = get_id(int(msg.text))
        if file_id:
            # send_video(token=msg.bot.token,chat_id=msg.chat.id,file_id=file_id[1],name=file_id[3])
            await msg.bot.send_video(chat_id=msg.chat.id, video=file_id[1], caption=file_id[3])
        else:
            await msg.answer(text="Bunday kodli kino topilmadi.")
    elif msg.text == "Menu":
        await state.set_state(RegistrState.menu)
    else:
        await msg.answer(text="Iltimos faqat codni kiriting faqat raqamlardan iborat bo'lsin!",reply_markup=orqaga)
@msg_co.message(F.text == "ℹ️ Muallif haqida")
async def info(msg: Message):
    infoo = 'Bot yaratuvchisi:\n\t🐍 Python Developer:  <a href="https://t.me/un_knowndev">Zafarbek Olimboyev</a>'
    await msg.answer(text=infoo,parse_mode=ParseMode.HTML)