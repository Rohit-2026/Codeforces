for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    t=max(max(a)-a[0],a[-1]-min(a))    
    for i in range(n):
        t=max(t,a[i-1]-a[i])  
    print(t)        
