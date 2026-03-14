import tkinter as tk  # Arayüz kütüphanemizi 'tk' kısaltmasıyla içeri alıyoruz

# --- 1. İŞLEM MOTORU (Fonksiyonlar) ---
def sozu_kaydet():
    # Yazı kutusunun içindeki metni çekip alıyoruz
    girilen_metin = yazi_kutusu.get() 
    
    # Şimdilik sadece terminale yazdıralım (Test amaçlı)
    print("Butona tıklandı! Gelen yeni söz:", girilen_metin)
    
    # Yazdırdıktan sonra kutunun içini temizleyelim ki yeni söz yazılabilsin
    yazi_kutusu.delete(0, tk.END)

# 1. Ana penceremizi oluşturuyoruz
pencere = tk.Tk()

# 2. Pencerenin başlığını ve başlangıç boyutunu ayarlıyoruz
pencere.title("Sürpriz Söz Ekleme Paneli")
pencere.geometry("400x300") # Genişlik x Yükseklik (Piksel cinsinden)

# Eşya 1: Bilgi Yazısı (Label)
bilgi_yazisi = tk.Label(pencere, text="Eklemek istediğiniz güzel sözü aşağıya yazın:", font=("Arial", 11))
bilgi_yazisi.pack(pady=20) # pady=20: Üstten ve alttan 20 piksel boşluk bırak

# Eşya 2: Yazı Kutusu (Entry)
yazi_kutusu = tk.Entry(pencere, width=45, font=("Arial", 10))
yazi_kutusu.pack(pady=10)

# Eşya 3: Kaydet Butonu (Button)
kaydet_butonu = tk.Button(pencere, text="Sözü Kaydet", command=sozu_kaydet, bg="green", fg="white", font=("Arial", 10, "bold"))
kaydet_butonu.pack(pady=10)

# 3. Pencerenin ekranda açık kalmasını sağlayan motor
pencere.mainloop()