def f(a,b):
    if a>=8 or b>=8:
        return 2
    elif a<=2 or b<=2:
        return 0
    else:
        return 1
a=int(input())
b=int(input())
print(f(a,b))