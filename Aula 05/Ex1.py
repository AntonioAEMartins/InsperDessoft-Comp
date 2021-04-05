soma=0
zero=0
indicador=True
while indicador:
    pergunta_numero=int(input("Qual o Próximo Número da soma?"))
    if pergunta_numero>zero:
        soma+=pergunta_numero
        indicador=True
    if pergunta_numero<=zero:
        indicador=False
        print (soma)

#Nesse programa eu adicionei duas constantes, sendo a primeira Soma e a segunda Zero (que aidiconei porque estava dando problema de Sintax)
#assim iniciei um programa While, para realizar a soma de todos os Input colocados pelo usuario (que eram transformados em Int)
#E caso este digitasse 0 termina o calculo automaticamente