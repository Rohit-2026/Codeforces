for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    t=[]
    for i in a:
        t.append(n-i+1)
    print(*t)   
