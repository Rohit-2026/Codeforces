n,t,p=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
if arr[-p]>t:
    print(0)
else:
    print(t-arr[-p])    