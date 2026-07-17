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


kelime_odunda = set()

corpus_kelime = set()

for satir in cumle_list_clean:
    corpus_kelime.update(satir.strip().split())


with open("../KelimeListesi/Turkce-Kelime-Listesi/turkce_kelime_listesi.txt",
          encoding="utf-8") as f:
    mevcut_kelime = set(line.strip() for line in f)

print(f"{len(mevcut_kelime)} mevcut kelime sayisidir")

# Sadece yeni kelimeler
yeni_kelimeler = corpus_kelime - mevcut_kelime

print(f"{len(yeni_kelimeler)} yeni kelime bulundu.")


with open("../KelimeListesi/Turkce-Kelime-Listesi/turkce_kelime_listesi.txt",
          "a",
          encoding="utf-8") as f:

    for kelime in sorted(yeni_kelimeler):
        f.write(kelime + "\n")

mevcut_kelime.update(yeni_kelimeler)

with open("../KelimeListesi/Turkce-Kelime-Listesi/turkce_kelime_listesi.txt",
          "w",
          encoding="utf-8") as f:

    for kelime in sorted(mevcut_kelime):
        f.write(kelime + "\n")



#sucvecz divanlugatiturk eklendi 255058 mevcut kelime 