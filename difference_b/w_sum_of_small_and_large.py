s=input()
x=s.split(" ")
s=s2=0
for i in x:
    mi=ord(min(i))
    s=s+mi
    ma=ord(max(i))
    s2=s2+ma
print(s2-s)