def f(n,ok):
    a=0
    if ok==True:
        a=5
    if (n-a<=60):
        return 0
    elif n-a>60 and n-a<=80:
        return 1
    else:
        return 1
n=int(input())
ok=bool(input())
print(f(n,ok))