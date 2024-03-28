l1=list(map(int,input().split(",")))
evenlist=[]
oddlist=[]
for i in l1:
    if(i%2==0):
       evenlist.append(i)
    else:
        oddlist.append(i)
print(evenlist)
print(oddlist)

