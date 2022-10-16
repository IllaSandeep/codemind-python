s=input()
v='aeiouAEIOU'
s1=""
for i in range(len(s)):
    if(len(s1)==0):
        if s[i] in v:
            s1+='V'
        else:
            s1+='C'
    elif s1[len(s1)-1]=='C':
        if s[i] in v:
            s1+='V'
    elif s1[len(s1)-1]=='V':
        if s[i] not in v:
            s1+='C'
print(s1)