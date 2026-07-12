with open("Turkcecumlelistesi/cumle.txt", "r", encoding="utf-8") as dosya:
    satirlar = [satir.strip() for satir in dosya]

sayi = 0
sayili_satirlar = []
for c in satirlar:
    ekli = str(sayi)+ " " + c 
    sayi += 1
    sayili_satirlar.append(ekli)

print(sayili_satirlar)

with open('sentenceid.txt', 'w') as file:
    file.write('\n'.join(sayili_satirlar))