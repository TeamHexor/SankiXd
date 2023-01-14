
import asyncio
import os
from telethon import events, Button
from telethon.tl.custom import button
from DEADLYSPAM import BOT0, BOT1, BOT2, BOT3, BOT4, BOT5, BOT6, BOT7, BOT8, BOT9, ALIVE_PIC, OWNER_ID, OWNER_NAME

DEADLY_IMG = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/226a73b069a28a0183ed3.mp4"


Deadly_Button = [
        [
        Button.url("Cʜᴀɴɴᴇʟ", "https://t.me/Its_Sanki"),
        Button.url("Sᴜᴘᴘᴏʀᴛ", "https://t.me/Its_Sanki")
        ],
        [
        Button.url("• Rᴇᴘᴏ •", "https://t.me/Himu_Xd")
        ]
        ]
        

#USERS 


@BOT0.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT1.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT2.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT3.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT4.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT5.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT6.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT7.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT8.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT9.on(events.NewMessage(incoming=True, pattern='/start'))
async def start(e):
    if e.chat_id is e.sender_id:
        name = e.sender.first_name
        user_id = e.sender_id
        mention = f"[{name}](tg://user?id={user_id})"
        myOwner = f"[{OWNER_NAME}](tg://user?id={OWNER_ID})"
        creator = f"[Hexor'Xd](tg://user?id={5555647537})"
        DEADLY_ON = f"""
ʜᴇʏ {mention},
ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴀᴄᴄᴇss sᴜᴘᴘᴏʀᴛ ,ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ʀᴇᴘᴏ!
    """
        await e.client.send_file(e.chat_id, DEADLY_IMG, caption=DEADLY_ON, buttons=Deadly_Button)
