s=input()
t="hello"
i=0
j=0
k=""
while j<len(s) and i<len(t):
    if t[i]==s[j]:
        k+=s[j]
        i+=1
        j+=1
    else:
        j+=1         
if k=="hello":
    print("YES")
else:
    print("NO")                