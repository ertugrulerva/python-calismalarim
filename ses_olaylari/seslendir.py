from gtts import gTTS
import os # Oluşan dosyayı otomatik açmak için kullanacağız

# 1. Okunmasını istediğimiz metni yazıyoruz
metin = "Tarihte ilk roketli uçuş denemesini, on yedinci yüzyılda Lagari Hasan Çelebi gerçekleştirmiştir."

# 2. Sesi oluşturuyoruz (lang='tr' ile Türkçe okumasını söylüyoruz)
print("Ses hazırlanıyor, lütfen bekleyin...")
ses = gTTS(text=metin, lang='tr', slow=False)

# 3. MP3 dosyası olarak bilgisayarımıza kaydediyoruz
dosya_adi = "lagari_belgesel.mp3"
ses.save(dosya_adi)
print("Harika! MP3 dosyası başarıyla oluşturuldu.")

# 4. (Bonus) Oluşan dosyayı bilgisayarın varsayılan müzik çalarıyla anında oynat!
os.startfile(dosya_adi)