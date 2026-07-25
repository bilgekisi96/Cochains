import cupy as cp

class SkipGram:

    def __init__(self, words,word_to_id, vocab_size,id_to_word):
        self.words = words
        self.word_to_id = word_to_id
        self.id_to_word = id_to_word
        self.vocab_size = vocab_size

        self.W = None
        self.W2 = None
        self.hidden = None
        self.scores = None
        self.pairs = None

    # Skip Gram
    def pairsf(self):
        self.pairs = []

        for i, word in enumerate(self.words):

            center = self.word_to_id[word]

            for j in range(
                max(0,i-1),
                min(len(self.words),i+2)
            ):

                if i != j:

                    context = self.word_to_id[self.words[j]]

                    self.pairs.append(
                        (center, context)
                    )

        print("su anda pairs")
        print(self.pairs[-1])
        # time.sleep(10) # Kaldırıldı veya yorum satırı yapıldı

    def embedding_matris(self):
        #Embedding Matris

        embedding_size = 8


        self.W = cp.random.randn(
            self.vocab_size,
            embedding_size
        ) * 0.01


        self.W2 = cp.random.randn(
            embedding_size,
            self.vocab_size
        ) * 0.01




    def forward(self):
        #Forward

        x = 0

        self.hidden = self.W[x]

        self.scores = self.hidden @ self.W2
        print("forward is ok")


    #Softmax
    def softmax(self,x):
        exp = cp.exp(
            x - cp.max(x)
        )
        return exp / exp.sum()

    def gradient(self):
        #Gradient Desent Eğitim döngüsü

        lr = 0.05
        start = time.time()
        #epochs = 1000 çok uzun zaman sürer diye 
        epochs = 5
        for epoch in range(epochs):

            loss = 0

            for center, target in self.pairs:

                hidden = self.W[center]

                scores = hidden @ self.W2

                probs = self.softmax(scores)

                loss -= cp.log(
                    probs[target]
                )

                # gradient

                grad = probs.copy()

                grad[target] -= 1

                dW2 = cp.outer(
                    hidden,
                    grad
                )

                dhidden = self.W2 @ grad

                # update

                self.W2 -= lr * dW2

                self.W[center] -= lr * dhidden

            if epoch % 10 == 0:
                percent = (epoch + 1) / epochs * 100

                elapsed = time.time() - start

                eta = elapsed / (epoch + 1) * (epochs - epoch - 1)

                print(
                    f"Epoch {epoch+1}/{epochs} "
                    f"({percent:.1f}%) | "
                    f"Loss: {loss/len(self.pairs):.4f} | "
                    f"Geçen: {elapsed:.1f}s | "
                    f"Kalan: {eta:.1f}s"
                )

            if epoch % 100 == 0:
                print(epoch, loss)


        #Embedding hazir

        kedi_vector = self.W[self.word_to_id["kedi"]]

        print(kedi_vector) #öğrenilmiş kelime vektörü

        # CuPy dizilerini NumPy'a dönüştürerek kaydet
        cp.savez(
            "skipgram_model.npz",
            W=self.W.get(), # .get() ile CPU'ya aktar
            W2=self.W2.get() # .get() ile CPU'ya aktar
        )
        model = {
            "W": self.W.get(),
            "W2": self.W2.get(),
            "word_to_id": self.word_to_id,
            "id_to_word": self.id_to_word,
        }

        with open("skipgram.pkl", "wb") as f:
            pickle.dump(model, f)



# Existing code logic, updated to use CuPy
with open("kitaptan_kelimeler.txt", "r", encoding="utf-8") as dosya:
    satirlar = [satir.strip() for satir in dosya]

satirlar = [k.lower() for k in satirlar]

words = [k.lower() for k in satirlar]

# word_matrix'i yükledikten sonra CuPy dizisine dönüştür
word_matrix_np = np.load("word_vectors_mantiksal.npy")
word_matrix = cp.asarray(word_matrix_np) # CuPy'ye dönüştür

word_vectors = {kelime: vektor for kelime, vektor in zip(satirlar, word_matrix.get())} # Eğer CPU'da işlem gerekiyorsa .get() kullan

word_to_id = word_vectors

vocab = sorted(set(words))

word_to_id = {
    w: i
    for i, w in enumerate(vocab)
}

id_to_word = {
    i: w
    for w, i in word_to_id.items()
}

vocab_size = len(vocab)
words = words[:10000] #sadece ilk 10000 kelimeye bak dedim epoch eğitim kolay olması için

skip_gram = SkipGram(words,word_to_id,vocab_size,id_to_word)

skip_gram.pairsf()
skip_gram.embedding_matris()
skip_gram.forward()
skip_gram.gradient()

print("Test Cosine")

# #Test Cosine

def cosine(a,b):
    # Cosine benzerliği için CuPy dizilerini NumPy'a dönüştürerek işlem yap
    a_np = a.get() if isinstance(a, cp.ndarray) else a
    b_np = b.get() if isinstance(b, cp.ndarray) else b
    return np.dot(a_np,b_np) / (
        np.linalg.norm(a_np)
        *
        np.linalg.norm(b_np)
    )


v1 = skip_gram.W[skip_gram.word_to_id["kedi"]]
v2 = skip_gram.W[skip_gram.word_to_id["köpek"]]

print(
    cosine(v1,v2)
)

# Bu kod gpu kullanımı ve işlem hızını arttırmak için düzenlendi ...
#Metin üretiminde Hem markov hem Embedding kullanılacak