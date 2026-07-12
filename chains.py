import numpy as np

chars = "aâbcçdefgğhıîijklmnoöprsştuûüvxyzAÂBCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVXYZ0123456789.–^,!?;:-()[]{}\"'/%&+=*@#\\\n\t\x85‚'``’' "

chars = sorted(set(chars))

char_to_id = {c:i for i,c in enumerate(chars)}
id_to_char = {i:c for c,i in char_to_id.items()}

embedding_dim = 8

embedding_matrix = np.random.randn(len(chars), embedding_dim)


with open("../KelimeListesi/Turkce-Kelime-Listesi/turkce_kelime_listesi.txt", "r", encoding="utf-8") as dosya:
    satirlar = [satir.strip() for satir in dosya]

word_vector_space = []

for kelime in satirlar:

    vectors = []

    for harf in kelime:

        idx = char_to_id[harf]

        vectors.append(embedding_matrix[idx])

    print(np.array(vectors))

    word_matrix = np.array(vectors)

    word_vector = np.mean(word_matrix, axis=0)
    word_vector_space.append(word_vector)

word_vector_space_arr = np.array(word_vector_space)
print(word_vector_space_arr.shape)
np.save("word_vectors.npy", word_vector_space_arr)