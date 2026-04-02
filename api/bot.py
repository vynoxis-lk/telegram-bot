import os
import json
from telegram import Bot, Update

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)

async def handler(request):
    try:
        data = await request.json()
        update = Update.de_json(data, bot)

        # Simple command handling
        if update.message:
            text = update.message.text

            if text == "/start":
                await bot.send_message(
                    chat_id=update.message.chat_id,
                    text="Bot is working on Vercel 🚀"
                )

        return {
            "statusCode": 200,
            "body": json.dumps({"ok": True})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": str(e)
        }
