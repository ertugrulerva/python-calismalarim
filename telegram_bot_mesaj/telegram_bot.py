import requests # İnternetteki sitelere (veya API'lere) bağlanmamızı sağlayan kütüphane

# Bilgilerimizi tanımlıyoruz (Buraya kendi bilgilerini tırnak içine yazmalısın)
TOKEN = "8191658705:AAEHDvO_yFAkvF0vB6RQoSGU3ATyAdHo9t0"
CHAT_ID = "8146950832"

# Göndereceğimiz ilk test mesajı
mesaj = "Merhaba! Ben Python üzerinden gönderilen ilk robot mesajıyım. 🤖"

# Telegram'ın mesaj gönderme kapısı (Adresi)
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

# Telegram'a göndereceğimiz paketi hazırlıyoruz (Kime gidecek, ne yazacak?)
parametreler = {
    "chat_id": CHAT_ID,
    "text": mesaj
}

# Ve postacıyı yola çıkarıyoruz! (Telegram'ın kapısına paketimizi bırakıyoruz)
cevap = requests.post(url, data=parametreler)

# İşlem başarılı mı diye kontrol ediyoruz (200 OK kodu, internet dünyasında "İşlem Başarılı" demektir)
if cevap.status_code == 200:
    print("Harika! Mesaj saniyeler içinde telefona ulaştı.")
else:
    print("Bir hata oldu:", cevap.text)