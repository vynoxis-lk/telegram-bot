import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")

app = Application.builder().token(BOT_TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Bot is working 🚀")

app.add_handler(CommandHandler("start", start))

async def handler(request):
    data = await request.json()
    update = Update.de_json(data, app.bot)

    await app.initialize()
    await app.process_update(update)

    return {"statusCode": 200, "body": "ok"}
