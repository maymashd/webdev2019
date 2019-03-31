import math
n=int(input())
a=1
while (a<=n):
    b=float(a)
    if b==float(int(math.sqrt(b))*int(math.sqrt(b))):
        print(a)
    a+=1