
import numpy as np
import time
import pickle

class SkipGram:

    def __init__(self, words,word_to_id, vocab_size): 
        self.words = words                           
        self.word_to_id = word_to_id
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
        time.sleep(10)

    def embedding_matris(self):
        #Embedding Matris

        embedding_size = 8


        self.W = np.random.randn(
            self.vocab_size,
            embedding_size
        ) * 0.01


        self.W2 = np.random.randn(
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
        exp = np.exp(
            x - np.max(x)
        )
        return exp / exp.sum()

    def gradient(self):
        #Gradient Desent Eğitim döngüsü

        lr = 0.05
        start = time.time()
        epochs = 1000

        for epoch in range(epochs):

            loss = 0

            for center, target in self.pairs:

                hidden = self.W[center]

                scores = hidden @ self.W2

                probs = self.softmax(scores)

                loss -= np.log(
                    probs[target]
                )

                # gradient

                grad = probs.copy()

                grad[target] -= 1

                dW2 = np.outer(
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
        
        np.savez(
            "skipgram_model.npz",
            W=self.W,
            W2=self.W2
        )
        model = {
            "W": self.W,
            "W2": self.W2,
            "word_to_id": self.word_to_id,
            "id_to_word": self.id_to_word,
        }

        with open("skipgram.pkl", "wb") as f:
            pickle.dump(model, f)

        #Hangi kelime anlam olarak birbirine yakın cevabı ?




with open("../KelimeListesi/Kitaptan_Kelimeler/kitaptan_kelimeler.txt", "r", encoding="utf-8") as dosya:
    satirlar = [satir.strip() for satir in dosya]

satirlar = [k.lower() for k in satirlar]

words = [k.lower() for k in satirlar]

word_matrix = np.load("word_vectors_mantiksal.npy")

word_vectors = {kelime: vektor for kelime, vektor in zip(satirlar, word_matrix)}

word_to_id = word_vectors

vocab = set(words)

word_to_id = {
    w: i
    for i, w in enumerate(vocab)
}

id_to_word = {
    i: w
    for w, i in word_to_id.items()
}

#id_to_word = {i:w for w,i in word_to_id.items()}

vocab_size = len(vocab)

skip_gram = SkipGram(words,word_to_id,vocab_size)

skip_gram.pairsf()
skip_gram.embedding_matris()
skip_gram.forward()
skip_gram.gradient()

print("Test Cosine")

# #Test Cosine

def cosine(a,b):

    return np.dot(a,b) / (
        np.linalg.norm(a)
        *
        np.linalg.norm(b)
    )


v1 = skip_gram.W[skip_gram.word_to_id["kedi"]]
v2 = skip_gram.W[skip_gram.word_to_id["köpek"]]

print(
    cosine(v1,v2)
)



#Metin üretiminde Hem markov hem Embedding kullanılacak 