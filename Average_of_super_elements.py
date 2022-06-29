n=int(input())
a=list(map(int,input().split()))
s=0
c=0
for i in sorted(set(a),key=a.index):
    if a.count(i)==i:
        s=s+a[i]
        c+=1
if c==0:
    print('-1')
else:
    avg=(s/c)-1
    print('%.2f'%avg)