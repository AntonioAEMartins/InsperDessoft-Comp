nivel=0
if input("Q1:") == "sim":
    nivel +=1
if input("Q2:") == "sim":
    nivel +=1
if input("Q3:") == "sim":
    nivel +=1
if input("Q4:") == "sim":
    nivel +=1
if input("Q5:") == "sim":
    nivel +=1
print(nivel)

if nivel == 1:
    print("Iniciant")
if nivel ==2:
    print("Experiente")
if nivel ==3:
    print("Expert")
if nivel ==4:
    print("Pro")
if  nivel ==5:
    print("Chuw")



def raizes(a,b,c):
    delta=b**2-4*a*c
    raiz1=(-b+delta**(1/2))/(2*1)
    return raiz1
print (raizes(1,2,1))

