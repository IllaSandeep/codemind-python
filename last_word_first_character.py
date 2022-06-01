s=list(map(str,input().split()))
c=0
x=len(s)
for i in s:
    c+=1
    if c==x:
        print(i[:3:3])