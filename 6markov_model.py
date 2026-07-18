from collections import defaultdict, Counter
import random
import numpy as np

with open("../KelimeListesi/Turkce-Kelime-Listesi/turkce_kelime_listesi.txt", "r", encoding="utf-8") as dosya:
    satirlar = [satir.strip() for satir in dosya]

words = np.array(satirlar)

markov = defaultdict(Counter)

for a, b in zip(words[:-1], words[1:]):
    markov[a][b] += 1


def generate(start, length):

    result = [start]
    current = start

    for _ in range(length):

        if current not in markov:
            break

        next_words = markov[current]

        choices = list(next_words.keys())
        weights = list(next_words.values())

        current = random.choices(
            choices,
            weights=weights
        )[0]

        result.append(current)

    return " ".join(result)

print(generate("kedi",10))