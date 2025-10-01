for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    if sum(a)<=0:
        print(abs(sum(a)))
    else:
        print(-(sum(a)))    