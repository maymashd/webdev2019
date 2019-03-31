def binpow(a,n):
    if (n==0):
        return 1
    elif n==1:
        return a
    elif n%2==0:
        return binpow(a,n/2)*binpow(a,n/2)
    elif n%2==1:
        return binpow(a,int(n/2))*binpow(a,int(n/2))*a
a=int(input())
n=int(input())
print(binpow(a,n))