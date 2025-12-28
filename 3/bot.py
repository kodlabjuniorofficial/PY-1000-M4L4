import os
import sqlite3
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

load_dotenv()

# --- Önceki Aşamada Tamamlanan Fonksiyonlar ---
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

# --- [ÖĞRETMEN DEMOLARI] ---
# GÖREV: /rastgele komutu için bir asenkron fonksiyon yazın.
# get_random_movie() fonksiyonundan gelen veriyi kullanıcıya şık bir mesajla gönderin.
async def suggest_random(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # ADIM 1: get_random_movie() fonksiyonunu çağırarak veriyi bir değişkene alın.
    # ADIM 2: update.message.reply_text kullanarak film bilgilerini mesaj olarak gönderin.
    pass

# --- [ÖĞRENCİ GÖREVİ] ---
# GÖREV: /eniyi komutu için bir asenkron fonksiyon yazın.
# get_top_movie() fonksiyonunu kullanın ve sonucu kullanıcıya gönderin.
async def suggest_top(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # ADIM 1: get_top_movie() fonksiyonu ile en iyi filmi seçin.
    # ADIM 2: Kullanıcıya film adını ve puanını içeren bir tebrik mesajı gönderin.
    pass

if __name__ == '__main__':
    app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()

    # Öğretmen: Rastgele komutunu bağlar
    # app.add_handler(CommandHandler("rastgele", suggest_random))

    # Öğrenci: En iyi komutunu bağlar
    # app.add_handler(CommandHandler("eniyi", suggest_top))

    print("Bot başlatılıyor...")
    app.run_polling()
