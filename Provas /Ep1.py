#Classifica Caixa

def classifica_caixa(comprimento,peso):
    W=(-6.193*comprimento)+(7.312*peso)-110.597
    if W>0:
        return "Verdura"
    if W<0:
        return "Legume"


#Soma Entrada Usuário

soma=0
estado=True
while estado:
    pergunta=input("Que digitar mais um número?")
    if pergunta == "sim":
        numero=float(input("Qual número?"))
        soma +=numero
        estado = True
    if pergunta == "não":
        estado = False
        print ("{0:.2f}".format(soma))
        
#ProdutoFresco

soma=0
caixa_verduradas=0
caixa_legumes=0
estado=True
while estado:
    pergunta=input("Quer adicionar dados de mais uma caixa?")
    peso=float(input("Peso da caixa"))
    comprimento=float(input("Comprimento da caixa"))
    if pergunta =="sim":
        W=(-6.193*comprimento)+(7.312*peso)-110.597
        if W>0:
            caixa_verduras += peso
            estado=True
        if W<0:
            caixa_legumes +=peso
            estado=True
    if pergunta =="não":
        estado = False
        
    
