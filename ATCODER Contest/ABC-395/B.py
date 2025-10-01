n=int(input())
a=[[''] * n for i in range(n)]
for i in range(1,n+1):
    j=n+1-i
    if i<=j:
        if i%2==1:
            c='#' 
        else:
            c='.'
        for r in range(i-1,j):
            for s in range(i-1,j):
                a[r][s]=c
for r in a:
    print(''.join(r))
