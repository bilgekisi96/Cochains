import re

# 1. Dosyayı oku
dosya_adi = "divanilugatiturk.txt"  # Dosya adınızı buraya yazın
with open(dosya_adi, "r", encoding="utf-8") as dosya:
    metin = dosya.read()

# 2. Metni cümlelere böl
# Cümle sonlarındaki (. ? !) işaretlerinden ve boşluklardan bölme yapar
cumleler = re.split(r"[.!?] \s*", metin)

# 3. Sonuçları listele
cumle_list = [f"{i} {cumle.strip()}" for i, cumle in enumerate(cumleler, 1) if cumle.strip()] 

print([k.replace("\n","") for k in cumle_list])
