import random
variante=random.randint(1,20)
nescolhido=int(input("Escolha um número"))
if nescolhido < 1 or nescolhido > 20:
    print ("Erro, escolha um número de 1-20")

#Aqui defini a variante utilizado da biblioteca Random e da função Randint que gera um nuero aleatorio, inteiro, dentre os do Range escolhido
#Logo apos adicionei um If, para dizer ao usuario se o numero escolhid é valido ou não
condicao= True
nvezes=1
while condicao and nvezes<5:
    if nescolhido<variante:
     print("Muito Baixo")
     condicao=True
     nescolhido=int(input("Escolha um número"))
     nvezes+=1
    if nescolhido>variante:
     print("Muito Alto")
     condicao=True
     nescolhido=int(input("Escolha um número"))
     nvezes+=1
    if nescolhido == variante:
        print("Acertou")
        condicao=False
if nvezes>= 5:
    print("Que Pena, você Perdeu!")
print("Este é o Número aleatorio:{}".format(variante))
print("Este é o Número que você escolheu:{}".format(nescolhido))


#Aqui defini as igualdades do sistema, então adicionei quando o Nescolhido era mais alto, baixo ou igual. E ao final da equação mostrei ao usuario
#o n digitado e o Nescolhido, para ele saber que o sistema está funcionando

tem_duvidas= True
if tem_duvidas:
    resposta_do_aluno=input("Você tem duvidas?")

    if resposta_do_aluno == "sim":
        print("Pratique mais")
        tem_duvidas= True
    else:
        print("Até a próxima")
        tem_duvidas= False

#Criei agora outra função que3
# pergunta se o aluno tem duvidas. Caso ele as tenha será respondido com estude mais.

tem_duvidas= True
nvezes=1

while tem_duvidas and nvezes <5:
    resposta_do_aluno=input("Você tem duvidas?")

    if resposta_do_aluno == "sim":
        print("Estude mais")
        tem_duvidas= True
        nvezes += 1
    else:
        print("Parabens")
        tem_duvidas= False
    if nvezes >= 5:
        print("Até a próxima")

#Agora modifiquei um pouco a equação das duvidas, adicionando um ciclo finito que rodará até o aluno ter 5 Duvidas.
