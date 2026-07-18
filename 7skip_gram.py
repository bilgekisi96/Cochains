
with open("../KelimeListesi/Turkce-Kelime-Listesi/turkce_kelime_listesi.txt", "r", encoding="utf-8") as dosya:
    satirlar = [satir.strip() for satir in dosya]


satirlar = [k.lower() for k in satirlar]

words = [k.lower() for k in satirlar]

word_matrix = np.load("word_vectors.npy")

word_vectors = {kelime: vektor for kelime, vektor in zip(satirlar, word_matrix)}

word_to_id = word_vectors


vocab = list(set(words))

id_to_word = {
    i:w for w,i in word_to_id.items()
}


vocab_size = len(vocab)

print(word_to_id)



# Skip Gram

pairs = []

for i, word in enumerate(words):

    center = word_to_id[word]

    for j in range(
        max(0,i-1),
        min(len(words),i+2)
    ):

        if i != j:

            context = word_to_id[words[j]]

            pairs.append(
                (center, context)
            )


print(pairs)




#Embedding Matris

embedding_size = 10


W = np.random.randn(
    vocab_size,
    embedding_size
) * 0.01


W2 = np.random.randn(
    embedding_size,
    vocab_size
) * 0.01





#Forward

x = 0

hidden = W[x]

scores = hidden @ W2





#Softmax

def softmax(x):

    exp = np.exp(
        x - np.max(x)
    )

    return exp / exp.sum()








#Gradient Desent Eğitim döngüsü


lr = 0.05


for epoch in range(1000):

    loss = 0

    for center, target in pairs:

        hidden = W[center]

        scores = hidden @ W2

        probs = softmax(scores)


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


        dhidden = W2 @ grad


        # update

        W2 -= lr * dW2

        W[center] -= lr * dhidden


    if epoch % 100 == 0:
        print(epoch, loss)


#Embedding hazir

kedi_vector = W[word_to_id["kedi"]]

print(kedi_vector) #öğrenilmiş kelime vektörü


#Hangi kelime anlam olarak birbirine yakın cevabı ?


#Test Cosine

def cosine(a,b):

    return np.dot(a,b) / (
        np.linalg.norm(a)
        *
        np.linalg.norm(b)
    )


v1 = W[word_to_id["kedi"]]
v2 = W[word_to_id["köpek"]]

print(
    cosine(v1,v2)
)


#Metin üretiminde Hem markov hem Embedding kullanılacak 