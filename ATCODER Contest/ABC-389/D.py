import math

r = int(input())
r2 = r * r
counts = []

# Calculate valid cell counts for each row
for i in range(-r, r + 1):
    t = r2 - (i + 0.5) ** 2
    if t >= 0:
        max_j = int(math.sqrt(t))
        counts.append(2 * max_j + 1)  # Count cells in this row

# Total count
print(sum(counts))
