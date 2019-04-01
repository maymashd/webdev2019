n=int(input())
list1=list()
list2=list()
for i in range(0,n):
    list1.append(input().split())
    cnt=0
    for j in range(1,len(list1[i])):
        cnt+=float(list1[i][j])
    list2.append(cnt/(len(list1[i])-1))
name=input()

for i in range(0,n):
        if list1[i][0]==name:
            print(list2[i])
