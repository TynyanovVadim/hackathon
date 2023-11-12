from pyrogram import Client
from pyrogram import idle
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler
from pyrogram import filters
from pyrogram.types import BotCommand
import asyncio
from pyrogram.enums import ParseMode

chat_id = None
group_id = -1001646666955

async def command_start(app: Client, message: Message):
    global chat_id
    chat_id = message.chat.id
    await app.send_message(message.chat.id, 'Выберите действие из меню\n<b>/get_mes_id \'message_id\'</b>: взять сообщение из сообщества по id и вывести его в чат\n<b>/get_his_id \'кол-во сообщений\'</b>: взять указанное\
кол-во сообщений и вывести их в чат\n<b>/search_mes_query \'query\' \'limit\'</b>: найти некоторое кол-во сообщений(limit) с запросом(query) и вывести их в чат', ParseMode.HTML)
    
    
async def get_mes(app: Client, message: Message):
    split_list = message.text.split()
    if len(split_list) == 2:
        id = int(split_list[1].strip())
        mes = await app.get_messages(group_id, id)
        await app.send_message(chat_id, mes.text)
    else:
        await app.send_message(chat_id, 'Данные введены неверно')

async def history(client: Client, message: Message):
    split_list = message.text.split()
    if len(split_list) == 2:
        count = int(split_list[1].strip())
        async for message in client.get_chat_history(group_id, count):
            DATE = str(message.date)
            TEXT = str(message.text)
            await client.send_message(chat_id, DATE + ':\n\n' + TEXT)
    else:
        await client.send_message(chat_id, 'Данные введены неверно')

async def search(client: Client, message: Message):
    split_list = message.text.split()
    if len(split_list) == 3:
        query = split_list[1].strip()
        limit = int(split_list[2])
        async for message in client.search_messages(group_id, query, limit=limit):
            await client.send_message(chat_id, message.text)
    

async def send(client, message: Message):
    await message.reply('\'^\'')

bot_commands = [
    BotCommand(
        command = 'start',
        description = 'Starting'
    ),
    BotCommand(
        command='get_mes_id',
        description='get message'
    ),
    BotCommand(
        command='get_his_id',
        description='get history'
    ),
    BotCommand(
        command='search_mes_query',
        description='search'
    )
]

async def start():
    client = Client('me_client_bot', 9006209, '57f2dfbe60fb31b1f7ef85ec937f36b5')

    app = Client(

    "bot_name_here",

    api_id = 9006209,

    api_hash='57f2dfbe60fb31b1f7ef85ec937f36b5',

    bot_token='6447479053:AAHfM6ugYCJ9dN1xuplm2NxGgMA4klIDq-4'

    )

    app.add_handler(MessageHandler(command_start, filters.command(commands='start')))


    client.add_handler(MessageHandler(get_mes, filters.command(commands='get_mes_id')))


    client.add_handler(MessageHandler(history, filters.command(commands='get_his_id')))

    client.add_handler(MessageHandler(search, filters.command(commands='search_mes_query')))

    await client.start()
    await app.start()
    await app.set_bot_commands(bot_commands)
    await idle()
    await app.stop()
    await client.stop()

if __name__ == '__main__':
    asyncio.run(start())