n=int(input())
a=list(map(int,input().split()))
i=0
j=n // 2
k=0
while i<n//2 and j<n:
    if a[i]*2<=a[j]:
        k+=1
        i+=1
        j+=1
    else:
        j+=1
print(k)