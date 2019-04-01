s=input()
d=""
for i in s:
    if i.islower()==True:
        d+=i.upper()
    else:
        d+=i.lower()
print(d)