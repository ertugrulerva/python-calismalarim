from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def anasayfa():
    return {"mesaj": "Harika! Python sunucusu su an tikir tikir calisiyor."}

@app.get("/api/kanal-verileri")
def veri_gonder():
    return {
        "kullanici": "Furkan",
        "son_video": "Seyit Onbasi ve Canakkale",
        "siradaki_video": "Kursad Destani",
        "durum": "Sistem aktif, Flutter'a veri gonderilmeye hazir!"
    }

# DİKKAT: Adresin sonuna süslü parantez içinde {isim} ekledik!
@app.get("/api/kanal-verileri/{isim}")
def veri_gonder(isim: str):
    
    # Gelen ismi küçük harfe çevirip kontrol ediyoruz
    if isim.lower() == "furkan":
        return {
            "kullanici": "Furkan",
            "son_video": "Seyit Onbasi ve Canakkale",
            "siradaki_video": "Kursad Destani"
        }
    elif isim.lower() == "pirireis":
        return {
            "kullanici": "Piri Reis",
            "son_video": "Kitab-ı Bahriye'nin Sırları",
            "siradaki_video": "Akdeniz'de Osmanlı Donanması"
        }
    elif isim.lower() == "lagari":
        return {
            "kullanici": "Lagari Hasan Celebi",
            "son_video": "İlk Roketli Uçuş Denemesi",
            "siradaki_video": "17. Yüzyıl Osmanlı Bilimi"
        }
    else:
        # Eğer tanımadığımız bir isim girilirse hata mesajı gönderiyoruz
        return {
            "hata": f"Sistemde '{isim}' adinda bir kayit bulunamadi!"
        }