n=int(input())
line=input().split()
se=set()
for i in line:
    se.add(int(i))
print(sum(se)/len(se))
