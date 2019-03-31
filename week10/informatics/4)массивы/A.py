list1=[]
n=int(input())
for i in range(0,n):
    a=int(input())
    list1.append(a)
for i in range(0,n):
    if (i%2==0):
        print(list1[i])
