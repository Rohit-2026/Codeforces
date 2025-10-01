#below Function is something i created using chatgpt way before this contest seive standard i just changed it a little.
def s(l):
    p=[1]*(l+1)
    p[0]=0 
    p[1]=0
    for i in range(2, int(l**0.5) + 1):
        if p[i]:
            for j in range(i * i, l + 1, i):
                p[j] = 0
    return [i for i in range(l + 1) if p[i]]
n=int(input())
c=0
p=s(int(n**(1/8)) + 1)
c+= sum(1 for x in p if x**8 <= n)
p= s(int(n**0.5) + 1)
for i in range(len(p)):
    for j in range(i + 1, len(p)):
        if p[i]**2 * p[j]**2 > n:
            break
        c += 1
print(c)
