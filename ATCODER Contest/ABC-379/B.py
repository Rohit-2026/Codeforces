n, k = map(int, input().split())
s = input()
c = 0
i = 0
while i <= n - k:
    if s[i:i+k] == 'O' * k:
        c += 1
        i += k
    else:
        i += 1  
print(c)
