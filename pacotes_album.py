#programa que calcula o número médio de pacotes necessários para completar um álbum com 681 figurinhas.

import numpy as np
import statistics as st
import matplotlib.pyplot as plt

num_pacotes = []
cartas = []

for i in range(1,1000):
    pacotes = 1
    cartas = np.random.choice(681,5)
    while len(np.unique(cartas))!=681:
        pacotes = pacotes + 1
        cartas = np.append(cartas,np.random.choice(681,5))
    num_pacotes = np.append(num_pacotes,pacotes)

mediana = st.median(num_pacotes)
media = st.mean(num_pacotes)

print(mediana)
print(media)

plt.hist(num_pacotes, bins='auto')
plt.title("Histograma")
plt.show()
