def f(a,ok):
    if a>=1 and a<=10:
        return True
    elif ok:
        return True
    else:
        return False
a=int(input())
b=bool(input())
print(f(a,b))