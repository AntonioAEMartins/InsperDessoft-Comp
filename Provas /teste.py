soma=0
caixa_verduras=0
caixa_legumes=0
estado=True
while estado:
    pergunta=input("Quer adicionar dados de mais uma caixa?")
    
    if pergunta =="sim":
        peso=float(input("Peso da caixa"))
        comprimento=float(input("Comprimento da caixa"))
        W=(-6.193*comprimento)+(7.312*peso)-110.597
        if W>0:
            caixa_verduras += peso
            estado=True
            print ("verdura")
        if W<0:
            caixa_legumes +=peso
            estado=True
            print("legume")
    if pergunta == "não":
        estado = False
        if caixa_verduras >0:
            print ("Peso total das caixas de verduras : {0:.2f}Kg".format(caixa_verduras))
        if caixa_legumes >0:
            print("Peso total das caixas de legumes : {0:.2f}Kg".format(caixa_legumes))