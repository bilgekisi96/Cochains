import numpy as np

word_matrix = np.load("word_vectors.npy")

sentence_vectors = np.load("sentence_vectors.npy")

print(word_matrix.shape)

print(word_matrix[0])

print(sentence_vectors.shape)