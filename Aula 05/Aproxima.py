def aproxima_raiz(n):
    i=1
    while i**2 < n:
        i+=1
    dif1=abs(n-1**2)
    dif2=abs(n-(i-1)**2)
    if dif1<dif2:
        return i
    else:
        return i-1
print(aproxima_raiz(49))
