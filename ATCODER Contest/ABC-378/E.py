n, m = map(int, input().split())
arr = list(map(int, input().split()))
mod_sums = []

for x in arr:
    t=[x%m]
    for i in mod_sums:
        t.append((i+x%m)%m)
    mod_sums+=t    
    print(mod_sums)
total=sum(mod_sums)
print(total)
