import Conversoes

distkm = 50
distmi = Conversoes.km2mi(distkm)

print("em Km: {}".format(distkm))
print("em Mi: {}".format(distmi))
print("em Km: {}".format(Conversoes.converte_milhas_para_km(62)))

#Criei uma biblioteca=Conversoes que torna o arquivo python algo mais simples e localizado
#Então caso tenha problema com a formula vou no arquivo importado que tenha esta
#Abaixo utilizei a formula colocada no arquivo py citado

Carro1Mi=50
Carro2Km=10
DistanciaKm=Conversoes.converte_milhas_para_km(Carro1Mi)-Carro2Km
print("Distancia entre os Carros: {}".format(DistanciaKm))


#Agora aumentando o conhecimento, criei uma biblioteca=area para simplificar o calculo
#de areas como as de triangulos e circulos

import area

x=10
y=20
z=area.triangulo(x,y)
print("area",z)

raio=3
print("circulo de raio {} tem area{}".format(raio,area.circulo(raio)))


##Aula 03 ##

#A função input abre o terminal para o usuario escrever algo, como sua cor favorita ou algo de seu interesse

#Pedindo a cor favorita com Input
cor_favorita=input("Qual a sua cor favorita?")
#Imprime a cor favorita do usuário
print(cor_favorita)
print("Sua cor favorita é:".format

#Agora com a area de um quadrado

#variaveis não podem começar com numeros, podem começar com letrar e _(mas não pode estar sozinho)
#Tentar não utilizar texto com acento, porque pode dar problemas de compatibilidade internacional (idioma)
#Não usar nomes reservados


