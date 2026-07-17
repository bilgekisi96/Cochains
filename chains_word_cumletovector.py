import numpy as np 

with open("../KelimeListesi/Turkce-Kelime-Listesi/turkce_kelime_listesi.txt", "r", encoding="utf-8") as dosya:
    satirlar = [satir.strip() for satir in dosya]

word_to_id = {kelime: i for i, kelime in enumerate(satirlar)}



with open("Turkcecumlelistesi/cumle.txt", "r", encoding="utf-8") as dosya:
    satirlar = [satir.strip().split() for satir in dosya]


liste_word = []
for k in satirlar:
    liste_word.append([word_to_id[j] for j in k])
        
word_vectors = np.load("word_vectors.npy")

print(word_vectors[liste_word[0]])

print(liste_word[0])

sentence_vectors = []

for ids in liste_word:   # sentence_tokens = [[78,132284,...],[9878,...],...]
    matrix = word_vectors[ids]
    sentence_vector = np.mean(matrix, axis=0)
    sentence_vectors.append(sentence_vector)

sentence_vectors = np.array(sentence_vectors)

np.save("sentence_vectors.npy", sentence_vectors)