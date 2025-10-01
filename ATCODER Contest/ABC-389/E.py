def minCostToEqualArrays(arr, brr, k):
    n = len(arr)
    arr_sorted_indices = {val: idx for idx, val in enumerate(sorted(arr))}
    brr_sorted_indices = {val: idx for idx, val in enumerate(sorted(brr))}
    arr_sequence = [arr_sorted_indices[val] for val in arr]
    brr_sequence = [brr_sorted_indices[val] for val in brr]
    arr.sort()
    brr.sort()
    diff_sum = sum(abs(arr[i] - brr[i]) for i in range(n))
    print(arr_sequence)
    print(brr_sequence)
    print(diff_sum)
    if arr_sequence == brr_sequence:
        return diff_sum + k
    else:
        return diff_sum

# Example Usage
arr1, brr1, k1 = [-7, 9, 5], [7, -2, -5], 2
print(minCostToEqualArrays(arr1, brr1, k1))  # Output: 13

arr2, brr2, k2 = [2, 1], [2, 1], 0
print(minCostToEqualArrays(arr2, brr2, k2))  # Output: 0
