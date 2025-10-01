t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = input().strip()
    b = input().strip()

    pre1 = []
    cnt0 = 0
    cost = 0
    for i in range(n):
        if a[i] == '1':
            cost += cnt0
            pre1.append(cost)
        else:
            cnt0 += 1

    suff2 = []
    cnt0 = 0
    cost = 0
    for i in range(n-1, -1, -1):
        if b[i] == '1':
            cost += cnt0
            suff2.append(cost)
        else:
            cnt0 += 1

    n1 = len(pre1)
    n2 = len(suff2)
    if n1 + n2 < n + 1:
        print(-1)
        continue

    ans = 10**18
    for i in range(n):
        if n1 >= i+1 and n2 >= n-i:
            v = pre1[i] + suff2[n-i-1]
            if v < ans:
                ans = v
    print(ans)
