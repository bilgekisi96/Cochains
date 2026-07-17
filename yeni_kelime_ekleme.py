kelime_odunda = set()
with open("Turkcecumlelistesi/cumle.txt", encoding="utf-8") as f:
    corpus_kelime = set()

    for satir in f:
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