from collections import defaultdict
n=int(input())
s=input()
t=set(list(s))
i=0
j=0
y=defaultdict(int)
m=n
while j<n:
    y[s[j]]+=1  
    while len(y)==len(t):
        m=min(m,j-i+1)
        y[s[i]]-=1
        if y[s[i]]==0:
            del y[s[i]]
        i+=1
    j+=1        
print(m)    






