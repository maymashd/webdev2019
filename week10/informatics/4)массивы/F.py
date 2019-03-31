n=input()
b=0
list=input().split()
for i in range(1,len(list)-1):
    if(int(list[i])>int(list[i-1]) and int(list[i])>int(list[i+1])):
        b+=1
print(b)