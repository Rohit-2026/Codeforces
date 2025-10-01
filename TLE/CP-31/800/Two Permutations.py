for i in range(int(input())):
    n,a,b=map(int,input().split())
    if n==a and a==b:
        print("Yes")
    elif a+b>=n-1:
        print("No")
    else:
        print("Yes")    