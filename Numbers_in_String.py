n=input()
a=[]
for i in n:
    if i.isdigit():
        a.append(int(i))
print(sum(a))