import requests
import json
import random
import schedule
import time

TOKEN = "BURAYA_KENDI_TOKEN_NUMARANIZI_YAZIN"
CHAT_ID = "BURAYA_HEDEF_ID_YAZIN"

def surpriz_mesaj_gonder():
    # 1. JSON dosyasını aç ve içindeki sözleri oku
    try:
        with open("sozler.json", "r", encoding="utf-8") as dosya:
            soz_listesi = json.load(dosya)
    except FileNotFoundError:
        print("Hata: sozler.json dosyası bulunamadı!")
        return # Dosya yoksa işlemi iptal et

    # 2. Listeden rastgele bir söz seç
    secilen_soz = random.choice(soz_listesi)

    # 3. Telegram'a gönder
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    parametreler = {"chat_id": CHAT_ID, "text": secilen_soz}
    
    cevap = requests.post(url, data=parametreler)
    
    if cevap.status_code == 200:
        print(f"Mesaj başarıyla gönderildi: {secilen_soz}")
    else:
        print("Bir hata oldu:", cevap.text)

# --- ZAMANLAYICI AYARLARI ---
# Test edebilmen için şu an 'her 10 saniyede bir' çalışacak şekilde ayarladık.
# Sistemi görünce burayı schedule.every(1).hours.do(surpriz_mesaj_gonder) yapacağız.
schedule.every(10).seconds.do(surpriz_mesaj_gonder)

print("Bot çalışmaya başladı! Gözler Telegram'da olsun... (Kapatmak için CTRL+C)")

# Botun kapanmadan sürekli arka planda saati kontrol etmesini sağlayan sonsuz döngü
while True:
    schedule.run_pending()
    time.sleep(1) # İşlemciyi yormamak için saniyede bir kontrol et
