for i in range(int(input())):
    n,k,x=map(int,input().split())
    if x>=(k*(1+k))//2 and x<=(k*(n+n-k+1))//2:
        print("YES")
    else:
        print("NO")    