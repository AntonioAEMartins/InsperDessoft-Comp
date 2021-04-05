a=int(input("Entre com a Base"))
b=int(input("Entre com a Altura"))
c=a*b
print(c)


import Conversoes

distKm=float(input("Entre com a distancia(km):"))
distMi=Conversoes.km2mi (distKm)
print("{}km->{}mi".format(distKm,distMi))
10

#é possivel escrever o codigo com 0,1 para representar a primeira operação e depois a segunda
#nesse caso 0=DistKM e 1=distMi

distKm=float(input("Entre com a distancia(km):"))
distMi=Conversoes.km2mi (distKm)
print("{0}km->{1}mi".format(distKm,distMi))
10

#É possivel colocar apenas com determinadas casas decimais, utilizando :2f (para suas casas decimais)

distKm=float(input("Entre com a distancia(km):"))
distMi=Conversoes.km2mi (distKm)
print("{0}km->{1:2f}mi".format(distKm,distMi))
10