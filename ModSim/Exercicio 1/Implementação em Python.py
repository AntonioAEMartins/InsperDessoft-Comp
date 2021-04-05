print("Hello World")
lista=[0]*10
print(lista)

#Criei uma lista com 10 caracteres = 0, em que o primeiro elemento se encontra na posição 0

lista[4]=7
lista[9]=15

print(lista)

#Agora alterei o quinto e decimo termo desta lista, para 7 e 15 respectivamente

lista[9]=lista[9]*2
print(lista)

#Agora multipliquei o decimo termo da lista por 2

print("Lista de Fibonacci")
lista=[0]*10
print(lista)
lista[0]=1
lista[1]=1
lista[2]=2
lista[3]=3
lista[4]=5
lista[5]=8
lista[6]=13
lista[7]=21
lista[8]=34
lista[9]=55

print(lista)

#Acima criei uma lista simples de Python, utilizando a sequência de Fibonacci de forma manual

i=1
#adicionei uma variavel que servirá de índice para o loop
while (i<1):
    print("Ola, sou a impressão", i)
    i=i+1

print("Fibonacci Aut")
Fibonacci=[0]*100
Fibonacci[0]=1
Fibonacci[1]=1
i=0
while (i<98):
    Fibonacci[i+2]=Fibonacci[i+1]+Fibonacci[i]
    i=i+1
print(Fibonacci)
#Acima está a equação automatica de Fibonacci


import matplotlib.pyplot as plt
import numpy as np

lista_x=np.arange(0,100)

#Foi criada a lista horizontal X que vai de 0 a 1000
plt.plot(lista_x, Fibonacci)  
plt.xlabel("Índice da sequência")
plt.ylabel("Valores da sequência")
plt.grid(True)
plt.show()

print("Onças 30 Meses")
Oncas=[0]*30
Oncas[0]=15
Oncas[1]=18
i=0
while (i<30):
    Oncas[i+1]=Oncas[i]+4-1
    i=i+1
print(Oncas)

