s=input()
b=0
a=0
l=0
o=0
n=0
for i in s:
    if i=='b':
        b+=1
    if i=='a':
        a+=1
    if i=='l':
        l+=1
    if i=='o':
        o+=1
    if i=='n':
        n+=1
san=0
while b>0 and a>0 and l>0 and o>0 and n>0:
    b-=1
    a-=1
    l-=2
    if l<0:
        break
    o-=2
    if o<0:
        break
    n-=1
    san+=1
print(san)
        
        