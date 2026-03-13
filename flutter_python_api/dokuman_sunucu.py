from fastapi import FastAPI

# API'mize havalı bir başlık ve açıklama ekliyoruz
app = FastAPI(
    title="Tarih Kanalı API",
    description="Bu API, mobil uygulamamıza tarihi şahsiyetlerin verilerini gönderir.",
    version="1.0"
)

@app.get("/")
def anasayfa():
    """Burası sistemin çalıştığını kontrol ettiğimiz ana sayfadır."""
    return {"mesaj": "Sunucu aktif!"}

@app.get("/api/kanal-verileri/{isim}")
def veri_gonder(isim: str):
    """
    Kullanıcı adını girerek o kişiye ait video verilerini getirir.
    Geçerli isimler: **furkan**, **pirireis**, **lagari**
    """
    if isim.lower() == "furkan":
        return {"kullanici": "Furkan", "son_video": "Seyit Onbasi"}
    elif isim.lower() == "pirireis":
        return {"kullanici": "Piri Reis", "son_video": "Kitab-ı Bahriye"}
    else:
        return {"hata": "Kayit bulunamadi!"}