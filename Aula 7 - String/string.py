lista1=[1,2,3,4]
print (lista1)
lista2=[9,8,7,6]
lista1.append(5)
print (lista1)
#acima foi adicionado um elemento com o .append

string1="abcd"
string2="efgh"
Soma_Strings="abcd"+"efgh"
soma_strings= string1+string2
print (Soma_Strings)
print(soma_strings)
#acima é realizada a soma de uma String, na qual não é póssivel utilizar .append

encontrar=string1.find("c")
print (encontrar)
#A string devolve a posição em uma lista que certo caracter está

string3="abcba"
substituir=string3.replace("b","d")
print(substituir)
#A string3 terá a repetição b substituida com d

apaga_espaço="    uma frase 1        \n".strip()
print (apaga_espaço)
#Acima com o .strip() apagaremos todos os espaços do inicio/fim da string


