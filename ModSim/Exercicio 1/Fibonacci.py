print("Fibonacci Aut")
Fibonacci=[0]*100
Fibonacci[0]=1
Fibonacci[1]=1
i=0

while (i<98):
    Fibonacci[i+2]=Fibonacci[i+1]+Fibonacci[i]
    i=i+1
print(Fibonacci)

import matplotlib.pyplot as plt
import numpy as np

lista_x=np.arange(0,100)

#Foi criada a lista horizontal X que vai de 0 a 1000
plt.plot(lista_x, Fibonacci)  
plt.xlabel("Índice da sequência")
plt.ylabel("Valores da sequência")
plt.grid(True)
plt.show()