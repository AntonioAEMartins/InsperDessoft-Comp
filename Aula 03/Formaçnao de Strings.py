#O grande objetivo deste aquivo é explicar a formação de Strings, e como gerar numeros com casas decimais
#e gerar numeros sem casas decimais

#A diferença de Float para int é que Float vai aceitar numeros decimais dados pelo usuario, enquanto int apenas inteiros.
import Conversoes

distKm=float(input("Entre com a distancia(km):"))
distMi=Conversoes.km2mi(distKm)
print("{0:.0f}km->{1:.0f}mi".format(distKm,distMi))
print("{0:.1f}km->{1:.1f}mi".format(distKm,distMi))
print("{0:.2f}km->{1:.2f}mi".format(distKm,distMi))
print("{0:.0f}km->{1:.2f}mi".format(distKm,distMi))

#Concatenação é quando quer juntar textos atravez de formula
s1="Inp"
s2="er"

s=s1+s2
print(s)

#Multiplicação de Strings

s=3*s1+s2
print(s)
