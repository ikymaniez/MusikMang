from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAEJRPhgc4wyE8q8DZtwCSzEJn0O5j6l1AACjwIAAkq0mVcKDooD9TgcSx4E")
    await message.reply_text(
        f"""**Yuhuuuu Guys saya {bn} 🎵

Saya bisa memutar musik di panggilan suara grup Anda. Dikembangkan Oleh [Toni](https://t.me/BluueBlueSky).

Tambahkan [Melodi Music](https://t.me/MelodiMusicPlayer) dan [Melodi Assistant](https://t.me/MelodiAssistanBot) ke grup Anda, dan nikmati mendengar musik dengan bebas!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Penjelasan Printah", url="https://telegra.ph/text-04-11-2")
                  ],[
                    InlineKeyboardButton(
                        "🐝 Pemilik", url="https://t.me/BluueBlueSky"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/CandaAnda"
                    )
                 ],[ 
                    InlineKeyboardButton(
                        "⚡Follow instagram⚡", url="www.instagram.com/antoniprananda"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Melodi Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/CandaAnda")
                ]
            ]
        )
   )


