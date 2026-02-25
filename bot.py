from pyrogram import Client, filters

api_id = 35790707
api_hash = "44753bcac8911c81028f009377368330"
bot_token = "8779345278:AAGUeRRmEx0C2MP2q4xDmNQUVlcyh_GRRR4"

CHANNEL_ID = -1003865059298

app = Client(
    "temramovies",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

@app.on_message(filters.text & ~filters.command)
async def search_movie(client, message):
    query = message.text.lower()
    found = False

    async for msg in client.search_messages(CHANNEL_ID, query, limit=5):
        if msg.video or msg.document:
            link = f"https://t.me/c/{str(CHANNEL_ID)[4:]}/{msg.id}"
            await message.reply(f"🎬 {msg.caption or 'Movie'}\n🔗 {link}")
            found = True

    if not found:
        await message.reply("❌ Movie not found")

app.run()
