lista_numeros=[1,2,3,4,5,6,7,8]
soma=0 #Soma precisa estar forá do For
for e in lista_numeros:
    if e % 2 != 0:
        soma+= e
        print (e)
print (soma)


def soma_impares (lista):
    soma=0
    for e in lista:
        if e % 2 !=0:
            soma+=e