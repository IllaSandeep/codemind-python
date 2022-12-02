s=input()
l=[]
s1=""
for i in s:
    if i.isalpha():
        l.append(i)
l.reverse()
x=0
for i in s:
    if i.isalpha():
        s1+=l[x]
        x+=1
    else:
        s1+=i
print(s1)