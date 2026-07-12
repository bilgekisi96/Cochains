with open("Turkcecumlelistesi/cumle.txt", "r", encoding="utf-8") as dosya:
    satirlar = [satir.strip() for satir in dosya]


print(satirlar)