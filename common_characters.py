s1=input().lower()
s2=input().lower()
s=''
flag=0
l=list(set(s1)&set(s2))
for i in l:
    if i==' ':
        continue
    s=s+i
    flag=1
x=sorted(s)
if flag==0:
    print('-1')
else:
    for i in x:
        print(i,end='')