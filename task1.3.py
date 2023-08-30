lst=['0001','0011','0101','1011','1101','1111']
decimal=[]
for a in lst:
    i=0
    s=0
    a=int(a)
    while a!=0:
        r=a%10
        p=int(r*(2**i))
        s+=int(p)
        a=a//10
        i=i+1
    decimal.append(s)
print(decimal)
while len(decimal)!=2:
    decimal.sort()
    # print(decimal)
    r1=decimal[0]
    decimal.remove(r1)
    # print(decimal)
    r2=decimal[0]
    decimal.remove(r2)
    # print(decimal)
    r3=r1+r2
    decimal.append(r3)
    # print(decimal)
print(decimal)