import sqlite3

# --- [ÖĞRETMEN DEMOLARI] ---
# GÖREV: Veritabanına bağlanın, bir cursor oluşturun.
# 'top250' tablosundan RANDOM() ile 1 film seçin ve fetchone() ile döndürün.
def get_random_movie():
    # ADIM 1: sqlite3 ile 'top250.db' dosyasına bağlanın.
    # ADIM 2: SQL sorgusunu (ORDER BY RANDOM() LIMIT 1) çalıştırın.
    # ADIM 3: Veriyi fetchone() ile yakalayıp return edin.
    pass

# --- [ÖĞRENCİ GÖREVİ] ---
# GÖREV: Veritabanından puanı (rating) en yüksek olan 1 filmi seçin.
# İpucu: 'rating DESC' ve 'LIMIT 1' kullanın.
def get_top_movie():
    # ADIM 1: Veritabanı bağlantısını ve cursor nesnesini oluşturun.
    # ADIM 2: Rating sütununa göre azalan sırada sıralayıp ilk kaydı getiren sorguyu çalıştırın.
    # ADIM 3: Veriyi alın ve bağlantıyı kapatıp sonucu döndürün.
    pass
