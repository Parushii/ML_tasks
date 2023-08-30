l=[
    [1,2,3,4,6],
    [5,7,8,9,15],
    [12,14,16,18],
    [10,11,12,13,16,17,18,20]
    ]
i=0
l3=[] #list of list of consecutive numbers
consecutive_list=[]
res=l.copy()
a=[]
for i in range(len(l)):
    consecutive_list=[]
    a=[]
    j=0
    while j<=len(l[i])-2:
        if  l[i][j]==l[i][j+1]-1 and l[i][j]==l[i][j-1]+1:
            consecutive_list.append(l[i][j-1])
            consecutive_list.append(l[i][j])
            consecutive_list.append(l[i][j+1])
            j=j+2
        else:
            j=j+1
    l3.append(consecutive_list)
print(l3)
i=0
for i in range(len(res)):
    j=0
    for j in range(len(l3[i])):
        res[i].remove(l3[i][j])
        # print(l3[i][j])
print(res)
