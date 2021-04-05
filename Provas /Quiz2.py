faixa1=0
faixa2=0
faixa3=0
faixa4=0
faixa5=0
faixa6=0
faixa0=0
pergunta=True

while pergunta:
    idade= int(input("Idade de seu paciente"))
    if idade>=0 and idade <=11:
        faixa1+=1
        faixa0+=1
        pergunta = True
    if idade>=12 and idade<=17:
        faixa2+=1
        faixa0+=1
        pergunta = True
    if idade>=18 and idade <=25:
        faixa3+=1
        faixa0+=1
        pergunta= True
    if idade>=26 and idade<=35:
        faixa4+=1
        faixa0+=1
        pergunta = True
    if idade>=36 and idade <=59:
        faixa5+=1
        faixa0+=1
        pergunta = True
    if idade>=60:
        faixa6+=1
        faixa0+=1
        pergunta = True
    if idade <0:
        pergunta = False


print("0-11 anos: {0:.2f}%".format((faixa1/faixa0)*100))
print("12-17 anos: {0:.2f}%".format((faixa2/faixa0)*100))
print("18-25 anos: {0:.2f}%".format((faixa3/faixa0)*100))
print("26-35 anos: {0:.2f}%".format((faixa4/faixa0)*100))
print("36-59 anos: {0:.2f}%".format((faixa5/faixa0)*100))
print("Acima de 60 anos: {0:.2f}%".format((faixa6/faixa0)*100))



