n=int(input())
s='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
st='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'
while n:
    i=n%26
    if i==0:
        st+='Z'
        n=(n//26)-1
    else:
        st+=s[i-1]
        n=(n//26)
l=len(st)
for i in range(l-1,-1,-1):
    print(st[i],end='')