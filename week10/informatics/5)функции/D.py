def election(a,b,c):
    s=a+b+c
    if (s>=2):
        return 1
    else:
        return 0
a1=int(input())
b1=int(input())
c1=int(input())
print(election(a1,b1,c1))
