import os
import sqlite3
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

load_dotenv()

# --- VERİTABANI FONKSİYONLARI ---
def get_random_movie():
    conn = sqlite3.connect('top250.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, year, rating FROM top250 ORDER BY RANDOM() LIMIT 1")
    movie = cursor.fetchone()
    conn.close()
    return movie

def get_top_movie():
    conn = sqlite3.connect('top250.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, year, rating FROM top250 ORDER BY rating DESC LIMIT 1")
    movie = cursor.fetchone()
    conn.close()
    return movie

# --- BOT KOMUTLARI ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎬 Sinema Gurmesi Botuna Hoş Geldin!\n\n/rastgele - Sana film öneririm\n/eniyi - Listenin şampiyonunu söylerim")

async def suggest_random(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = get_random_movie()
    await update.message.reply_text(f"🎲 Rastgele Öneri: {data[0]} ({data[1]}) - ⭐ Puan: {data[2]}")

async def suggest_top(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = get_top_movie()
    await update.message.reply_text(f"🏆 Listenin En İyisi: {data[0]} ({data[1]}) - ⭐ Puan: {data[2]}")

# --- ANA PROGRAM ---
if __name__ == '__main__':
    token = os.getenv("BOT_TOKEN")
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("rastgele", suggest_random))
    app.add_handler(CommandHandler("eniyi", suggest_top))

    print("🎬 Bot başarıyla başlatıldı!")
    app.run_polling()
