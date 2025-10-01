import heapq
from collections import defaultdict

f = defaultdict(int)
min_heap = []

for _ in range(int(input())):
    q = list(map(int, input().split()))
    
    if q[0] == 1:
        # Increment the count of 0
        f[0] += 1
        heapq.heappush(min_heap, 0)  # Push the key 0 into the heap
    elif q[0] == 3:
        # Query the sum of counts for keys >= q[1]
        c = 0
        # Remove all elements from the heap that are less than q[1]
        while min_heap and min_heap[0] < q[1]:
            heapq.heappop(min_heap)
        
        # Now sum the counts for keys >= q[1]
        for key in list(f.keys()):
            if key >= q[1]:
                c += f[key]
        print(c)
    else:
        # Update all keys in the heap by adding q[1] and updating their counts
        new_entries = []
        for key in list(f.keys()):
            new_key = key + q[1]
            f[new_key] += f[key]
            new_entries.append(new_key)
            heapq.heappush(min_heap, new_key)  # Push the new keys into the heap
        
        # Ensure all old keys are removed if no longer relevant
        for key in list(f.keys()):
            del f[key]

