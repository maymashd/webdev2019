def xor(x,y):
    if ( (x==1 and y==0) or (x==0 or y==1) ):
        return True
    else :
        return False
a=int(input())
b=int(input())
print(xor(a,b))