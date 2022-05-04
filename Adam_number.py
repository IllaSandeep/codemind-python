n = int(input())
sq_n=n*n
rev=0
while n:
    rev=rev*10+n%10
    n//=10
rev_sq=rev*rev
p=0
while rev_sq:
    p=p*10+rev_sq%10
    rev_sq//=10
if sq_n==p:
    print(True)
else:
    print(False)