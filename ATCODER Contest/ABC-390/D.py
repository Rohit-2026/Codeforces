def calculate_distinct_xors(a):
    n = len(a)
    unique_xors = set()
    
    # Iterate over all subsets using bitmasking
    for mask in range(1 << n):
        group_sum = 0
        remaining_xor = 0
        for i in range(n):
            if mask & (1 << i):  # If the i-th bit is set in mask, it's in the subset
                group_sum += a[i]
            else:
                remaining_xor ^= a[i]  # Otherwise, XOR the element with the remaining XOR
        # Add the result to the set
        unique_xors.add(group_sum ^ remaining_xor)
    
    return len(unique_xors)

# Input
n = int(input())
a = list(map(int, input().split()))
print(calculate_distinct_xors(a))
