from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""
 𝐇𝐞𝐲 {msg.from_user.mention}.
𝐓𝐡𝐢𝐬 𝐢𝐬 {me2}.
𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐨𝐫 𝐁𝐨𝐭...
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="🔷 Start Generating Session 🔷", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("🔷 Join This Group 🔷", url="https://t.me/RomeoBot_op"),
                ]
            ]
        ),
        disable_web_page_preview=True,
    )       
