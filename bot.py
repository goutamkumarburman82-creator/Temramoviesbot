import os
import threading
from flask import Flask
from pyrogram import Client, filters

# ---------- ENV ----------
api_id = int(os.environ.get("35790707"))
api_hash = os.environ.get("44753bcac8911c81028f009377368330")
bot_token = os.environ.get("8779345278:AAGUeRRmEx0C2MP2q4xDmNQUVlcyh_GRRR4")
CHANNEL_ID = int(os.environ.get("-1003865059298"))

# ---------- PYROGRAM ----------
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

# ---------- FLASK ----------
app = Flask(__name__)

@app.route("/")
def home():
    return "Temramovies Bot Running"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# ---------- START ----------
if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    bot.run()
