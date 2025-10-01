n=int(input())
a=list(map(int,input().split()))
d={}
for i in range(n):
    if a[i] in d:
        d[a[i]].append(i+1)
    else:
        d[a[i]]=[i+1]
print(d)
s_d= dict(sorted(d.items(), key=lambda item: len(item[1]),reverse=True)) 
print(s_d)
for i in s_d:
    f=0
    for j in range(1,len(s_d[i])-1):
        if s_d[i][j]-s_d[i][j-1]!=s_d[i][j+1]-s_d[i][j]:
            f==1
            break
    if f==0:
        print(len(s_d[i]))
        break
else:
    print(1)       

