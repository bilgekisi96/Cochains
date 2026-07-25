import re

# 1. Dosyayı oku
dosya_adi = "sucvecz.txt"  # Dosya adınızı buraya yazın
with open(dosya_adi, "r", encoding="utf-8") as dosya:
    metin = dosya.read()

# 2. Metni cümlelere böl
# Cümle sonlarındaki (. ? !) işaretlerinden ve boşluklardan bölme yapar
cumleler = re.split(r"[.!?] \s*", metin)

# 3. Sonuçları listele
cumle_list = [f"{i} {cumle.strip()}" for i, cumle in enumerate(cumleler, 1) if cumle.strip()] 

cumle_list_clean = [k.replace("\n","") for k in cumle_list]

kitap_tan_kelime = [satir.strip().split() for satir in cumle_list_clean]

kitap_tan_kelime = [j for k in kitap_tan_kelime for j in k]
print(kitap_tan_kelime)

with open("../KelimeListesi/Kitaptan_Kelimeler/kitaptan_kelimeler.txt",
           "a",
           encoding="utf-8") as f:

     for kelime in kitap_tan_kelime:
         f.write(kelime + "\n")