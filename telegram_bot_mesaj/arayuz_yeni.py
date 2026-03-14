import tkinter as tk
import tkinter.messagebox as messagebox  # Açılır uyarı pencereleri için
import json  # JSON dosyasıyla işlem yapmak için
import os    # Dosyanın var olup olmadığını kontrol etmek için

# --- 1. İŞLEM MOTORU ---
def sozu_kaydet():
    girilen_metin = yazi_kutusu.get() 
    
    # KONTROL 1: Acaba kutu boş mu? Boşsa uyarı verip işlemi durduralım.
    if girilen_metin.strip() == "":
        messagebox.showwarning("Uyarı", "Lütfen boş bir söz eklemeyin!")
        return # return kodu burada keser, aşağıya inmesini engeller.

    # KONTROL 2: Eski sözleri kaybetmemek için önce dosyayı okumamız lazım.
    soz_listesi = [] # Önce boş bir liste hazırlıyoruz
    
    # Eğer sozler.json diye bir dosya zaten varsa, içindekileri bu listeye alalım
    if os.path.exists("sozler.json"):
        with open("sozler.json", "r", encoding="utf-8") as dosya:
            soz_listesi = json.load(dosya)

    # 3. YENİ SÖZÜ EKLE: Kutudan aldığımız metni, listenin sonuna ekliyoruz
    soz_listesi.append(girilen_metin)

    # 4. DOSYAYA YAZ: Güncellenmiş listeyi tekrar sozler.json dosyasına kaydediyoruz
    with open("sozler.json", "w", encoding="utf-8") as dosya:
        # indent=4 kısmı JSON dosyasının içindeki yazıların alt alta, düzenli durmasını sağlar
        json.dump(soz_listesi, dosya, ensure_ascii=False, indent=4)

    # 5. BAŞARI MESAJI VE TEMİZLİK
    messagebox.showinfo("Başarılı", "Harika! Yeni söz kalıcı olarak eklendi.")
    yazi_kutusu.delete(0, tk.END)

# --- 2. PENCERE VE TASARIM ---
pencere = tk.Tk()
pencere.title("Sürpriz Söz Ekleme Paneli")
pencere.geometry("400x300")

bilgi_yazisi = tk.Label(pencere, text="Eklemek istediğiniz güzel sözü aşağıya yazın:", font=("Arial", 11))
bilgi_yazisi.pack(pady=20)

yazi_kutusu = tk.Entry(pencere, width=45, font=("Arial", 10))
yazi_kutusu.pack(pady=10)

kaydet_butonu = tk.Button(pencere, text="Sözü Kaydet", command=sozu_kaydet, bg="green", fg="white", font=("Arial", 10, "bold"))
kaydet_butonu.pack(pady=10)

pencere.mainloop()