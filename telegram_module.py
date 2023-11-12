from pyrogram import Client
from pyrogram import idle
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler
from pyrogram import filters
from pyrogram.types import BotCommand
from pyrogram.enums import ParseMode

async def search(char_id, words, user):
    client = Client('me_client_bot', 9006209, '57f2dfbe60fb31b1f7ef85ec937f36b5')

    await client.start()
    ans = []
    if (user):
        async for x in client.search_messages(id, query=words, from_user=user):
            ans.append({"id": x.id, "from_user": x.from_user, "text": x.text})
    else: 
        async for x in client.search_messages(id, query=words):
            ans.append({"id": x.id, "from_user": x.from_user, "text": x.text})
    await client.stop()

    return ans

async def get_messages(chat_id):
    client = Client('me_client_bot', 9006209, '57f2dfbe60fb31b1f7ef85ec937f36b5')

    await client.start()
    ans = []
    async for x in client.get_chat_history(chat_id):
        ans.append({"id": x.id, "from_user": x.from_user, "text": x.text})
    await client.stop()
    return ans
