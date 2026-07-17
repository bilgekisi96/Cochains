with open("../KelimeListesi/Turkce-Kelime-Listesi/turkce_kelime_listesi.txt",
          encoding="utf-8") as f:
    mevcut_kelime = set(line.strip() for line in f)

print(f"{len(mevcut_kelime)} mevcut kelime sayisidir")
