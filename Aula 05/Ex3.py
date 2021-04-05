def prod3(lista):
    maior= lista[0]*lista[1]*lista[2]
    i=0
    while i<len(lista)-3:
        valor=lista[i]*lista[i+1]*lista[i+2]
        if valor > maior:
            maior = valor
        i+=1
    return maior

L1=[4,2,3]
print(prod3(L1))