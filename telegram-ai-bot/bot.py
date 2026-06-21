import logging
import os

from dotenv import load_dotenv
from openai import OpenAI
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)
from ytmusicapi import YTMusic

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
CHAT_MODEL = os.environ.get("CHAT_MODEL", "gpt-4o-mini")
IMAGE_MODEL = os.environ.get("IMAGE_MODEL", "gpt-image-1")

client = OpenAI(api_key=OPENAI_API_KEY)
ytmusic = YTMusic()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Привет! Я ассистент.\n\n"
        "/music <название> — найти музыку (ссылки на YouTube Music)\n"
        "/image <описание> — нарисовать картинку\n"
        "Просто напиши сообщение — отвечу как чат-бот."
    )


async def music(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = " ".join(context.args)
    if not query:
        await update.message.reply_text("Напиши: /music название песни")
        return

    results = ytmusic.search(query, filter="songs", limit=5)
    if not results:
        await update.message.reply_text("Ничего не нашёл.")
        return

    lines = []
    for r in results:
        title = r.get("title", "?")
        artists = ", ".join(a["name"] for a in r.get("artists", []))
        video_id = r.get("videoId")
        link = f"https://music.youtube.com/watch?v={video_id}" if video_id else "(нет ссылки)"
        lines.append(f"{title} — {artists}\n{link}")

    await update.message.reply_text("\n\n".join(lines))


async def image(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    prompt = " ".join(context.args)
    if not prompt:
        await update.message.reply_text("Напиши: /image описание картинки")
        return

    await update.message.reply_text("Рисую...")
    result = client.images.generate(model=IMAGE_MODEL, prompt=prompt, size="1024x1024")
    await update.message.reply_photo(result.data[0].url)


async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_text = update.message.text
    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[{"role": "user", "content": user_text}],
    )
    await update.message.reply_text(response.choices[0].message.content)


def main() -> None:
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("music", music))
    app.add_handler(CommandHandler("image", image))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
    app.run_polling()


if __name__ == "__main__":
    main()
