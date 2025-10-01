for i in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    if k==1 and a!=sorted(a):
        print("NO")
    else:
        print("YES")    


