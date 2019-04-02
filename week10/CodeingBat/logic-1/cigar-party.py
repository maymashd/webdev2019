def f(n,ok):
    if (ok):
        if n>=40:
            return True
        else:
            return False
    else:
        if n>=40 and n<=60:
            return True
        else:
            return False
n=input()
ok=input()
print(f(n,ok))