import numpy as np

chars = "abcçdefgğhıijklmnoöprsştuüvyzABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ0123456789.,!?;:-()[]{}\"'/%&+=*@#\n\t "

chars = sorted(set(chars))

char_to_id = {c:i for i,c in enumerate(chars)}
id_to_char = {i:c for c,i in char_to_id.items()}

embedding_dim = 8

embedding_matrix = np.random.randn(len(chars), embedding_dim)

kelime = "MER"

vectors = []

for harf in kelime:

    idx = char_to_id[harf]

    vectors.append(embedding_matrix[idx])

print(np.array(vectors))