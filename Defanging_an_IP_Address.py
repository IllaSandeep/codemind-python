s=(input())
for i in range (0,len(s)):
    if(ord(s[i])==46):
        print("[.]",end='')
    else:
        print(s[i],end='')