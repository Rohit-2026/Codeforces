# Input parsing
N, M = map(int, input().split())
L = []
R = []

for _ in range(N):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

# Total number of pairs (l, r) such that 1 <= l <= r <= M
total_pairs = M * (M + 1) // 2

# Now count how many invalid pairs (l, r) exist that completely contain [L_i, R_i]
invalid_pairs = 0

for i in range(N):
    Li = L[i]
    Ri = R[i]
    # For each Li, Ri, count how many pairs (l, r) such that l <= Li and r >= Ri
    # l ranges from 1 to Li, and for each l, r ranges from Ri to M
    invalid_pairs += Li * (M - Ri + 1)

# The result is total pairs minus invalid pairs
valid_pairs = total_pairs - invalid_pairs
print(valid_pairs)
