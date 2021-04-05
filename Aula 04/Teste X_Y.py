def testa_x_y(x,y):
    if x>y:
        resultado=1
    if x==0:
        resultado=0
    else:
        resultado=-1
    return resultado

print(testa_x_y(5,10))


numero=int(input("Digite um número"))
if numero==0:
    print ("0 não é nem par, nem ímpar")
elif numero %2==0:
    print("{0} é par".format(numero))
else:
    print("{0} é ímpar".format(numero))


#Aqui criei uma equação que aceita Input do usuario, para dizer se o numero é Par, impar ou nenhum dos dois
#ELIF = Se não, Se
20

#Exercicio 10, porque não é possivel realizar a divisão ou porcentagem do zero.
#Exercicio 11: É mais eficiente utilizar o Else, porque já definimos anteriormente o que faz um número ser Par, ou Nenhum dos dois


def testa_maioridade(idade):
    if idade>=21:
        return "maior nos EUA e Brasil"
    elif idade>=18:
        return "Maior no Brasil"
    else:
        return "Menor de idade"

print(testa_maioridade(17))
print(testa_maioridade(20))
print(testa_maioridade(21))

esta_chovendo = True
faz_sol = True

hora = int(input("Que horas são:"))



msg=""
if hora <0 or hora > 24:
    msg="Hora invalida"
elif hora <12:
    msg="Bom-dia"
elif hora <18:
    msg="Boa-Tarde"
else:
    msg="Boa-noite"

print(msg)

#Elif não entra em todos os blocos, ele entra apenas em 1. Então nesse caso é precido colocar bom-dia, antes de boa-tarde
#Então nesse caos pra não termos boa noite + hora invalida, é necessario adicionar IF (primeiro) e depois ELIF