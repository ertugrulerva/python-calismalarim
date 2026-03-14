import requests
import json
import random
import schedule
import time
import os

TOKEN = "BURAYA_KENDI_TOKEN_NUMARANIZI_YAZIN"
CHAT_ID = "BURAYA_HEDEF_ID_YAZIN"

def surpriz_mesaj_gonder():
    soz_listesi = []
    kullanilmis_listesi = []

    # 1. Ana dosyamızı (sozler.json) okuyoruz
    if os.path.exists("sozler.json"):
        with open("sozler.json", "r", encoding="utf-8") as dosya:
            soz_listesi = json.load(dosya)

    # 2. Kullanılmış sözler dosyamızı okuyoruz (Eğer daha önce oluşmadıysa boş kalacak)
    if os.path.exists("kullanilmis_sozler.json"):
        with open("kullanilmis_sozler.json", "r", encoding="utf-8") as dosya:
            kullanilmis_listesi = json.load(dosya)

    # 3. KONTROL: Ana listede hiç söz kalmadıysa ne olacak? (İşte senin mantığın burası)
    if len(soz_listesi) == 0:
        print("Ana listedeki tüm sözler bitti! Kullanılmış sözler geri yükleniyor...")
        
        # Eğer kullanılmış liste de boşsa, sistemde hiç söz yoktur demektir.
        if len(kullanilmis_listesi) == 0:
            print("Hata: Hiçbir dosyada söz yok. Lütfen arayüzden söz ekleyin.")
            return # İşlemi durdur
        
        # Masadaki (kullanılmış) kartları alıp tekrar elimizdeki desteye (ana listeye) koyuyoruz
        soz_listesi = kullanilmis_listesi.copy()
        kullanilmis_listesi = [] # Masayı (kullanılmış listeyi) tertemiz yapıyoruz

    # 4. Elimizdeki desteden rastgele bir söz seçiyoruz
    secilen_soz = random.choice(soz_listesi)

    # 5. YER DEĞİŞTİRME: Seçilen sözü ana listeden SİL, kullanılmış listesine EKLE
    soz_listesi.remove(secilen_soz)
    kullanilmis_listesi.append(secilen_soz)

    # 6. DOSYALARI GÜNCELLE: İki listeyi de son halleriyle dosyalarına kaydediyoruz
    with open("sozler.json", "w", encoding="utf-8") as dosya:
        json.dump(soz_listesi, dosya, ensure_ascii=False, indent=4)
        
    with open("kullanilmis_sozler.json", "w", encoding="utf-8") as dosya:
        json.dump(kullanilmis_listesi, dosya, ensure_ascii=False, indent=4)

    # 7. Mesajı Telegram'a Gönder
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    parametreler = {"chat_id": CHAT_ID, "text": secilen_soz}
    cevap = requests.post(url, data=parametreler)
    
    if cevap.status_code == 200:
        print(f"Mesaj başarıyla gönderildi: {secilen_soz}")
        print(f"Kalan yeni söz sayısı: {len(soz_listesi)}")
    else:
        print("Bir hata oldu:", cevap.text)

# --- ZAMANLAYICI AYARLARI ---
schedule.every(10).seconds.do(surpriz_mesaj_gonder)

print("Hafızalı Bot çalışmaya başladı! (Kapatmak için CTRL+C)")

while True:
    schedule.run_pending()
    time.sleep(1)
