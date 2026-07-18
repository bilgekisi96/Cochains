import numpy as np




with open("../KelimeListesi/Turkce-Kelime-Listesi/turkce_kelime_listesi.txt", "r", encoding="utf-8") as dosya:
    satirlar = [satir.strip() for satir in dosya]

word_matrix = np.load("word_vectors.npy")

word_vectors = {kelime: vektor for kelime, vektor in zip(satirlar, word_matrix)}




def cosine(v1, v2):
    return np.dot(v1, v2) / (
        np.linalg.norm(v1) *
        np.linalg.norm(v2)
    )


def nearest_words(word, embeddings, topk=5):

    target = embeddings[word]

    scores = []

    for other_word, vector in embeddings.items():

        if other_word == word:
            continue

        sim = cosine(target, vector)

        scores.append((other_word, sim))

    scores.sort(key=lambda x: x[1], reverse=True)

    return scores[:topk]


for word, score in nearest_words("araba", word_vectors):
    print(word, score)