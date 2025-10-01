N, W = map(int, input().split())
blocks = []

for i in range(N):
    x, y = map(int, input().split())
    blocks.append((y, x, i))  # Sort primarily by y, then x, and keep index

Q = int(input())
queries = []
for _ in range(Q):
    t, a = map(int, input().split())
    queries.append((t, a - 1))  # Convert 1-based to 0-based index

blocks.sort(reverse=True)  # Sort blocks by y descending, x ascending

col_stack = {i: 0 for i in range(1, W + 1)}  # Track landing heights
disappear_time = [-1] * N  # Store when each block disappears
row_count = {}  # Count blocks in each row

for y, x, i in blocks:
    land_y = col_stack[x] + 1  # Block falls to the next available row
    col_stack[x] = land_y  # Update column stack

    row_count[land_y] = row_count.get(land_y, 0) + 1
    if row_count[land_y] == W:  # If a row gets completely filled
        disappear_time[i] = land_y  # The row disappears at time land_y
        for col in range(1, W + 1):
            if col_stack[col] == land_y:
                col_stack[col] -= 1  # Drop all blocks in that row
        del row_count[land_y]  # Remove the row tracking

for t, a in queries:
    if disappear_time[a] == -1 or disappear_time[a] > t:
        print("Yes")
    else:
        print("No")
