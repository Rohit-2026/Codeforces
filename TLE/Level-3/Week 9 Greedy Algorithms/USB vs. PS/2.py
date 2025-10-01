a,b,c=map(int,input().split())
n=int(input())
u=[]
p=[]
cost=0
count=0
for i in range(n):
    t,q=map(str,input().split())
    if q=="USB":
        u.append(int(t))
    else:
        p.append(int(t))
u.sort()
p.sort()
if a<=len(u):
    cost+=sum(u[0:a])
    u=u[a:]
    count+=a
else:
    cost+=sum(u)
    count+=len(u)
    u=[]
if b<=len(p):
    cost+=sum(p[0:b])
    p=p[b:]
    count+=b 
else:
    cost+=sum(p)
    count+=len(p)
    p=[]
u=u+p 
u.sort()   
if len(u)>=c:
    cost+=sum(u[0:c])
    count+=c        
else:
    cost+=sum(u)
    count+=len(u)
print(count,cost)                     

