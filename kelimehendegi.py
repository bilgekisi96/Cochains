with open("../KelimeListesi/Turkce-Kelime-Listesi/turkce_kelime_listesi.txt", "r", encoding="utf-8") as dosya:
    satirlar = [satir.strip() for satir in dosya]

print(satirlar)