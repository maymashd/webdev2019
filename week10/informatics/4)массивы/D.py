n=input()
b=0
list=input().split()
for i in range(1,len(list)):
    if(list[i]>list[i-1]):
        b+=1
print(b)