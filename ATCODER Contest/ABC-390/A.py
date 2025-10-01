a=list(map(int,input().split()))
t=[]
for i in range(5):
    if a[i]!=i+1:
        t.append(i)
if len(t)>2 or not t:
    print("No")
else:
    if abs(t[0]-t[1])==1:
        print("Yes")
    else:
        print("No")                