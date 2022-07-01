s=input()
c=0
for i in set(s):
    if s.count(i)==1:
        c+=1
if c==len(s):
    print('True')
else:
    print('False')