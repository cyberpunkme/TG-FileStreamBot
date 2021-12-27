# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from pyrogram import filters, emoji
from WebStreamer.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

@StreamBot.on_message(filters.command(['start', 'help']))
async def start(_, m: Message):
    await m.reply(f'👋𝐇𝐞𝐲 {m.from_user.mention(style="md")}, 𝘚𝘦𝘯𝘥 𝘮𝘦 𝘢 𝘧𝘪𝘭𝘦 𝘵𝘰 𝘨𝘦𝘵 𝘢𝘯 𝘥𝘪𝘳𝘦𝘤𝘵 𝘭𝘪𝘯𝘬.', quote=True)
