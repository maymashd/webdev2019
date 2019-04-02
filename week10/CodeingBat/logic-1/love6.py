def f(a,b):
    if a==6 or b==6:
        return True
    elif a-b==6 or b-a==6 or a+b==6:
        return True
    else:
        return False
a=int(input())
b=int(input())
print(f(a,b))