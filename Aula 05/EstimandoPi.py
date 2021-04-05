def Piwallis(n):
    i=0
    dividendo=0
    divisor=1
    produto=1
    while i < n:
        if i%2 ==0:
            dividendo+=2
        else:
            divisor+=2
        termo = dividendo/divisor
        produto*=termo
        i+=1
    return produto*2

