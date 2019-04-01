n=int(input())
list1=list()
list2=list()
list3=list()
cnt=2000000

for i in range(0,n):
    s=input()
    a=float(input())
    list1.append(s)
    list2.append(a)

b=min(list2)

for i in range(0,len(list2)):
    if (cnt>list2[i] and list2[i]!=b):
        cnt=list2[i]
for i in range(0,len(list2)):
    if (cnt==list2[i]):
        list3.append(list1[i])

list3.sort()

for i in list3:
    print(i)
