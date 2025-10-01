for o in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = []
    for x in a:
        d.append([int(c) for c in str(x)[::-1]])
    m = max(len(x) for x in d)
    c = 0
    r = 0
    for i in range(m):
        s = r
        for x in d:
            if i < len(x):
                s += x[i]
        if s > 9:
            r = s // 10
            c += r
        else:
            r = 0
    print(c)
