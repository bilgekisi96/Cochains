chars = set("""aâbcçdefgğhıîijklmnoöprsştuûüvwxyzAÂBCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVXQWYZ0123456789.–^,!?„™ﬀﬂ~;:‘ä►£®±-✓()[]{}\"'/\xad><é%ù|©”—“&+ﬁÛ=«°'̂…*q■»_$•Î@#\\\n\t\x85‚'``’' """)

with open("../KelimeListesi/Turkce-Kelime-Listesi/turkce_kelime_listesi.txt",
          encoding="utf-8") as f:
    kelimeler = [satir.strip() for satir in f]

harf_yok = []

for kelime in kelimeler:
    for harf in kelime:
        if harf not in chars:
            harf_yok.append(harf)

print(set(harf_yok))