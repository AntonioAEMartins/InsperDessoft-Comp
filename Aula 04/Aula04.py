#Desvios COndicionais (if) = Quando o Python desvia o programa, pulando uma parte, ou sendo redirecionado
print("Começo o programa")

if True:
    print("Entrou no primeiro if")

if False:
    print("Entrou no segundo if")

print("Saindo do programa")

#Aqui vamos aplicar uma condição não conectada a nenhuma base de dados, então ela sempre será verdadeira (True)
print("Começou Idade")

idade=int(input("Qual sua idade?"))
if idade < 18 and idade>0:
    print("Menor de Idade")

if idade >= 18:
    print("Maior de idade")
    print("Agora vocie pode dirigir")

if idade <=0 and idade>150:
    print("Idade invalida")

print("Saindo do Programa")

#Aqui realizei um programa que pergunta a idade do usuario com a linha 15, introduzindo um Input
#E depois adicionei duas condições, com escrituras identadas. Depois fomos limitando o programa
#para idades humanas, então adicionamos o AND para colocar mais limitacões a idades minimas e criei mais uma clausula
#Para idade mínima

#######

menor = 1<2 #Operação lógica
print(menor) #recebe o valor de verdadeiro
print((1<2)) #recebe o valor de verdaeiro

#Aqui ocorre a operacionalização do valor de menor, então nesse caso é verdade que 1 é menor que 2, então menor é verdadeiro
#Ao Print Menor ou 1<2 vamos ter o mesmo resultado

nota=int(input("Sua media:"))
limiar = 5

aprovado = nota >= limiar #operação logica
print("Aprovado".format(aprovado))

igual =1==2 #== corresponde a igualdade
print("4.{}".format(igual))

diferente=1!=2
print("5.{}".format(diferente))

contem_i = "i" in "Insper"
print("6.{}".format(contem_i))
#Python diferencia Maiuscula de minuscula, assim não percebe que em Insper existe i

