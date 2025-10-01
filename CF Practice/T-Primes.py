import math

n = int(input())
a = list(map(int, input().split()))

def SOE(b):
    itroh = [1] * (b + 1)
    itroh[0] = itroh[1] = 0
    for i in range(2, int(math.sqrt(b)) + 1):
        if itroh[i]:
            for j in range(i * i, b + 1, i):
                itroh[j] = 0
    return [i for i in range(2, b + 1) if itroh[i]]

t = SOE(int(math.sqrt(max(a))) + 1) 

for i in range(n):
    if a[i] == 1:
        print("NO")
    else:
        sqrt_a_i = int(math.sqrt(a[i]))
        if sqrt_a_i * sqrt_a_i == a[i] and sqrt_a_i in t:
            print("YES")
        else:
            print("NO")
