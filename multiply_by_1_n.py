def tich(n):
    if(n==1):
        return 1
    return n*(n-1)*tich((n-1)-1)

print("1/",tich(n))
