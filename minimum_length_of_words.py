a=list(map(str,input().split()))
l=[]
for i in a:
    c=0
    for j in i:
        c+=1
    l.append(c)
    c=0
print(min(l))