import os
from pyrogram import Client, filters
from flask import Flask
import threading

api_id = int(os.environ.get("35790707"))
api_hash = os.environ.get("44753bcac8911c81028f009377368330")
bot_token = os.environ.get("8779345278:AAGUeRRmEx0C2MP2q4xDmNQUVlcyh_GRRR4")
CHANNEL_ID = int(os.environ.get("-1003865059298"))

bot = Client(
    "temramovies",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

@bot.on_message(filters.text & ~filters.command)
async def search_movie(client, message):
    query = message.text.lower()
    found = False

    async for msg in client.search_messages(CHANNEL_ID, query, limit=5):
        if msg.video or msg.document:
            link = f"https://t.me/c/{str(CHANNEL_ID)[4:]}/{msg.id}"
            await message.reply(
                f"🎬 {msg.caption or 'Movie'}\n🔗 {link}"
            )
            found = True

    if not found:
        await message.reply("❌ Movie not found")

# -------- Flask Web Server --------
app = Flask(__name__)

@app.route("/")
def home():
    return "Temramovies Bot is Running"

def run_flask():
    app.run(host="0.0.0.0", port=10000)

# -------- Start Both --------
if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    bot.run()
