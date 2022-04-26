a=int(input())
rev=0
while a!=0:
    h=a%10
    rev=rev*10+h
    a=a//10
print(rev)
