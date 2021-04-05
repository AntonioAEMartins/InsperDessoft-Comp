print("Onças 30 Meses")
Oncas=[0]*30
Oncas[0]=15
Oncas[1]=18
i=0
while (i<29):
    Oncas[i+1]=Oncas[i]+4-1
    i=i+1
print(Oncas)

import matplotlib.pyplot as plt
import numpy as np

lista_x=np.arange(0,30)
plt.plot(Oncas,lista_x)
plt.xlabel("População de Onças")
plt.ylabel("∆População de Onças")
plt.grid(True)
plt.show()

