import sys
t = []
k = [4, 8, 15, 16, 23, 42]
p = {}
l1 = []
l2 = []
for i in range(len(k)):
    for j in range(i+1, len(k)):
        p[k[i]*k[j]] = [k[i], k[j]]
print("?", 1, 2)
sys.stdout.flush()
n = int(input())
t.append(n)
print("?", 2, 3)
sys.stdout.flush()
n = int(input())
t.append(n)
l1 += p[t[0]]
l1 += p[t[1]]
for i in range(3):
    if l1.count(l1[i]) == 2:
        e = l1[i]
        l1.remove(e)
        l1.remove(e)
        break
l1 = [l1[0], e, l1[1]]
t = []
print("?", 3, 4)
sys.stdout.flush()
n = int(input())
t.append(n)
print("?", 4, 5)
sys.stdout.flush()
n = int(input())
t.append(n)
l2 += p[t[0]]
l2 += p[t[1]]
for i in range(3):
    if l2.count(l2[i]) == 2:
        e = l2[i]
        l2.remove(e)
        l2.remove(e)
        break
l2 = [l2[0], e, l2[1]]
l1 = l1 + l2[1:]
for i in k:
    if i not in l1:
        l1.append(i)
        break
print("!", *l1)