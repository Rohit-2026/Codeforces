q=3*10**5
p=[True]*(q+1)
p[0]=p[1]=False
for i in range(2,int(q**0.5)+1):
    if p[i]:
        for j in range(i*i,q+1,i):
            p[j] = False
primes=[x for x in range(q+1) if p[x]]
for i in range(int(input())):
    n,k=input().split()
    n=int(n)
    s=input()
    t=[]
    for i in range(n):
        if s[i]!=k:
            t.append(i+1)     
    if not t:
        print(0)
    elif len(t)==1:
        print(1)
        if t[0]==n:
            print(n-2)
        elif t[0]==1:
            print(2)
        else:
            print(t[0]-1)
    else:
        for i in range(n-1,-n//2,-1):
            if i not in t and i in primes:
                print(1)
                print(i)
                break
        else:
            print(2)
            print(n,n-1)
        

