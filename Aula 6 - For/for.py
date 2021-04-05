#Hoje vamos estudar um pouco do For, que serve para criar repetições de listas
def soma_elementos(lista):
    soma=0
    i=0
    while i < len(lista):
        n=lista[i]
        soma+=n
        i+=1
    return soma

#acima temos um exemplo simples de uma função que percorre uma lista utilizando While
#nesta lista utilizamos o while para percorrer a lista enquanto i é menor que sua Len.

minha_lista=[] #Lista sem elementos
minha_lista.append("lembranca") #Adicionar elemento da lista
minha_lista.append("Ultima aula") #Não é possivel adicionar dois elementos ao mesmo tempo em uma lista
print (minha_lista)
minha_lista.append(["Ultima aula","Listas"]) #Adicionei uma lista dentro de minha_lista

#

numeros=[1,2,3,4,5,6]
i=0
while i<len(numeros):
    duas_numeros=numeros[i]*2
    i+=1
    print (duas_numeros)

#Acima adicionei uma lista chamada numeros com 6 elementos. E vou utilizar o While/Len
#para conseguir multiplicar todos os itens desta lista.

numeros=[1,2,3,4,5,6]
i=0
while i<len(numeros):
    numeros[i]*=2
    i+=1
    print (numeros) #Será impressa cada passada da lista, já que o print esta dentro do while

#Acima é outra maneira de se multiplicar todos os elementos de uma lista

"for" # Não é necessario utilizar condição.

for e in minha_lista: #para cada elemento de minha lista, imprima elemento
    print (e)

lista=[5,6,2,1,2,3]
i=0
while i<len(lista):
    print (lista[i])
    i+=1

for el in lista:
    print (el)

#O For se torna o jeito mais facil e eficiente de se imprimir ou interagir com uma lista
print("Percorrendo uma lista com for")

lista =["a",1,3.14,["x","y","z"]]

for e in lista:
    print (e)

nova_lista=[]
for el in nova_lista:
    if(el>=0):
        nova_lista.append(el)

print(nova_lista)

#acima estaria adicionado um elemento na lista utilizando o For

palavra= "Insper"
for e in palavra:
    print (e)

#Acima foi criada uma lista com a palavra "Insper" e o For ira percorrer cada letra da palavra
#E finalmente imprimirá elas individualmente

print("For como Range 1")
for i in range(5):
    print(i)
print("For como Range 2")
for i in range(1,5):
    print(i)
print("For como Range 3")
for i in range(0,5,2):
    print(i)

#Acima foi utilizado o For como Range, então o primeiro vai print todos os números de 0-4
#O segundo todos de 1 a 4, e o terceiro someno os numeros entre 0 e 4 pulando-os de 2 em 2