print("Modelo Populacional Geométrico de Onças")

Oncas=[0]*50
Oncas[0]=25
Oncas[1]=25.05
i=0
while (i<49):
    Oncas[i+1]=Oncas[i]+(0.1*Oncas[i])-(0.05*Oncas[i])
    i=i+1
    
print(Oncas)

import matplotlib.pyplot as plt
import numpy as np
lista_x=np.arange(0,50)
plt.plot(lista_x,Oncas)
plt.xlabel("Quantidade de Meses")
plt.ylabel("Número de Oncas")
plt.grid(True)
plt.show()