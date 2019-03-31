n=int(input())
a=1
ok=False
while (a<=n):
    if (a==n):
        ok=True
    a=a*2
if ok==True:
    print("YES")
else:
    print("NO")