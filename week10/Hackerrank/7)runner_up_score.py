n=input()
list=input().split()
b=max(list)
a=-999999
for i in range(0,len(list)):
    if int(list[i])!=b and int(list[i])>a:
        a=int(list[i])
print(a)