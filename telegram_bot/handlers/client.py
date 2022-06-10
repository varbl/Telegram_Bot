from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from data_base import sqlite_db

async def command_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, 'Вітаю', reply_markup=kb_client)
		await message.delete()
	except: 
		await message.reply('Спілкування з ботом через ОП, напишіть йому:\nhttps://t.me/yakitoriya_mk_bot')

async def open_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'Пн-Нд з 10:00 до 19:00')

async def place_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'проспект Центральний, 93В')

#@dp.message_handler(commands=['Меню'])
async def menu_command(message : types.Message):
	await sqlite_db.sql_read(message)


def register_handlers_client(dp : Dispatcher):
	dp.register_message_handler(command_start, commands=['start','help'])
	dp.register_message_handler(open_command, commands=['Режим_роботи'])
	dp.register_message_handler(place_command, commands=['Адреса'])
	dp.register_message_handler(menu_command, commands=['Меню'])