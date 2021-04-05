# Vamos iniciar nossas variáveis: alpha e S
alpha=0.2
S=200

# Em seguida, vamos criar uma lista que será preenchida pela equação a diferenças
# (O código a seguir cria uma lista com 40 elementos com dados da população, todos nulos)
P=[0]*40

# Vamos agora a redefinir o primeiro elemento da lista por o valor de P(0)=5
P[0]=5

# Por fim, vamos executar um loop para preencher toda a lista P[], que é nossa série temporal
# (Note que a lista deve ser percorrida até o penúltimo item, e note também que o primeiro elemento já está preenchido)
t=0
while(t<39):
    P[t+1]=P[t]+alpha*P[t]-alpha*(P[t]**2/S)
    t=t+1  

print(P)