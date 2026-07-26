import pickle
import numpy as np

# Modeli yükle
embeddings = np.load("skipgram_model.npz")

with open("skipgram.pkl", "rb") as f:
    data = pickle.load(f)

word_to_index = data["word_to_id"]
index_to_word = data["id_to_word"]

W = embeddings["W"]
W2 = embeddings["W2"]

print(embeddings)
print(word_to_index)

print(W.shape)
print(W2.shape)


query = W[word_to_index["kadın"]]

scores = (W @ query) / (
    np.linalg.norm(W, axis=1) * np.linalg.norm(query) # cosine sim
)

indices = np.argsort(scores)[::-1] 

for i in indices[:10]:
    print(index_to_word[i], scores[i])