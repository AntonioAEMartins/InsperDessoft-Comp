import math #Sempre que fomos utilizar uma biblioteca há a necessidade de importar a biblioteca, diferentes bibliotecas vão ter diferentes performances

print("Resultados")
print(1+1/2+1/2**2+1/2**3)
print (1+1/2+1/(2**2)+1/(2**3))
print
print ((3*4+5)/(1+2*3))
print((3**2+4**2)**(1/2)) #Raiz quadrada sem biblioteca
print(math.sqrt(3**2+4**2)) #Raiz Quadrada da biblioteca math
print(0.4321/2)

x=5 
#armazenei a informação de que X=5, entnao sempre que adicionar X a uma conta ele adicionará o número 5
#Não adicionei print antes do X, porque não quero exibir na tela
print(x)


y="hoje faz sol"
print(y)
#armazenei um valor de texto na letra Y, coloquei entre "porque é texto"

x=3
y=4
z=x*y
print("O retângulo de lado {0} e {1} tem area {2}".format(x,y,z))
#armazene um valor novo para X, Y e depois coloquei uma formula para Z, Print indica
#que X,Y,Z são respectivamente valores do lado de um retângulo


soma=1
soma = soma + 1/2**1
soma = soma + 1/2**2
soma = soma + 1/2**3
soma = soma + 1/2**4
print(soma)

a=1
b=a
a=3

print("a:",a,"b",b)
#Armazenei os valores de A,B e depois atualizei o valor de A

A=5
B=7
A=A+5
print("a vale{0},b vale {1}".format(A,B))
B-=3
C=1*B
C+=2
print("c vale {0}".format(C))

import math
resultado= math.cos(0)
print(resultado)
#Importei a biblioteca de Math, depois armazenei um resultado e Imprimi ele


def converte_milhas_para_km(distancia_mi):
    distancia_km = 1.60934*distancia_mi
    return distancia_km
#Def vai definiar algo, armazenei então a distancia em milhas (parametro Zero)
#Gravo esse vlor aleatorio dentro de ua variavel (1.60934), e embaixo escrevo return, para ter o retorno de meus calculos
#Reecuo (identação) de 4 espaços abaixo de def é sempre obrigatorio
print("milhas:{0},km:{1}".format(4,converte_milhas_para_km(4)))
#Agora pedi para o Calculo Print formatar 
