from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from DATA_BASE import database
from States.admin_state import AdminState
from config import db_name
from functions.upload_movie import upload
from keyboards.keyboards import orqaga, menu, menu_admin,yes_or_noo

admin_co = Router()
@admin_co.message(F.text=="Yangi kino yuklash")
async def upload_kino(msg: Message, state: FSMContext):
    db = database.database_user(db_name)
    user = db.get_user(msg.from_user.id)
    if user[5] != 0:
        await msg.answer(text="Kino videosini yuboring",reply_markup=orqaga)
        await state.set_state(AdminState.file_id)
    else:
        await msg.answer(text="Xatolik buday menu yo'q",reply_markup=menu)
@admin_co.message(AdminState.file_id)
async def movie_id(msg: Message, state: FSMContext):
    try:
        file_id = msg.video.file_id
        await state.update_data(file_id=file_id)
        await msg.answer(text="Kino nomini kiriting: ")
        await state.set_state(AdminState.about)
    except:
        if msg.text == "Menu":
            await msg.answer(text="Menu",reply_markup=menu_admin)
            await state.clear()
        else:
            await msg.answer(text="Kino videosini yuboring")
@admin_co.message(AdminState.about)
async def movie_name(msg: Message, state: FSMContext):
    await state.update_data(name=msg.text)
    await msg.answer(text="Kino kodini kiriting")
    await state.set_state(AdminState.key)
@admin_co.message(AdminState.key)
async def key(msg: Message, state: FSMContext):
    dbm = database.database_movie(db_name)
    if msg.text.isdigit():
        if not dbm.get_movie(int(msg.text)):
            data =await state.get_data()
            file_id = data.get("file_id")
            name = data.get("name")
            keyy = int(msg.text)
            await state.update_data(keyy=keyy)
            await state.update_data(chat_idd=msg.chat.id)
            # yes_or_no(msg.bot.token,msg.chat.id,file_id,name=name,keyboard=yes_or_noo)
            await msg.bot.send_video(chat_id=msg.chat.id, video=file_id, caption=f"Kino nomi: {name}\nKod: {keyy}\n Saqlansinmi", reply_markup=yes_or_noo)
            await state.set_state(AdminState.upload_movie)
        else:
            await msg.answer(text="Kino kodini kiriting. Bu kodga boshqa kino biriktirilgan")
    else:
        await msg.answer(text="Kino kodini kiriting. Faqat raqamlardan iborat bo'lsin")
@admin_co.callback_query(AdminState.upload_movie)
async def upload_v(query: CallbackQuery, state: FSMContext):
    if query.data == "Ha":
        data = await state.get_data()
        file_id = data.get("file_id")
        name = data.get("name")
        keyy = data.get("keyy")
        chat_id = data.get("chat_idd")
        await upload(file_id,keyy,name)
        await query.answer(text="Kino muvoffaqiyatli yuklandi.")
        await state.clear()
        await query.answer(text="Menu")
        await query.bot.send_message(chat_id=chat_id,text="Menu",reply_markup=menu_admin)
    else:
        data = await state.get_data()
        chat_id = data.get("chat_idd")

        await state.clear()
        await query.bot.send_message(chat_id=chat_id,text="Menu", reply_markup=menu_admin)
