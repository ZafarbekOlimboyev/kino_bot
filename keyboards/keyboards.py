from aiogram.types import KeyboardButton,ReplyKeyboardMarkup,InlineKeyboardMarkup,InlineKeyboardButton
reg = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Ro'yxatdan o'tish")]
],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Ro'yxatdan o'tish tugmasini bosing"
)

phone = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Telefon raqamni yuborish",request_contact=True)]
],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='"Telefon raqamni yuborish" tugamsini bosing.'
)
menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Kino izlash"),KeyboardButton(text="ℹ️ Mualliflar haqida")]
],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Kerakli menuni tanlang"

)
orqaga = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Menu")]
],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Agar menuga qaytmoqchi bo'lsangiz 'Menu' tugmasini bosing"

)
menu_admin = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Kino izlash"),KeyboardButton(text="Yangi kino yuklash")],
    [KeyboardButton(text="Shaxsiy Ma'lumotlar"),KeyboardButton(text="ℹ️ Muallif haqida")]
],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Kerakli menuni tanlang"

)
yes_or_noo = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Ha",callback_data="Ha"),
        InlineKeyboardButton(text="Yo'q",callback_data="Yo'q")
    ]
])
