import math
def prime(n):
    ok=True
    for i in range(2,int(n/2)):
        if n%i==0:
            prime=False
    return ok
n=int(input())
print(prime(n))