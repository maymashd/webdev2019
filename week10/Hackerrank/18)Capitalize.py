n=input().split()
list =list()
for i in range(0,len(n)):
    list.append(n[i][0].upper()+n[i][1:])
for i in list:
    print(i)


