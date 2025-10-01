for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    t=a.count(1)
    t1=a.count(0)
    print(2**t1*t)