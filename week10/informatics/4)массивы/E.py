n=input()
b=0
ok=False
list=input().split()
for i in range(1,len(list)):
    if(int(list[i])*int(list[i-1])>0):
        ok=True
if ok :
    print("YES")
else:
    print("NO")