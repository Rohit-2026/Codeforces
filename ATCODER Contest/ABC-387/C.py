def count_numbers_with_strict_msd(n):
    # Convert the number into a string for easy manipulation
    str_n = str(n)
    d = len(str_n)  # Number of digits in the given number
    count = 0
    
    # Count numbers with fewer digits than n
    for length in range(1, d):
        # For numbers of length 'length', MSD can be from 1 to 9
        for msd in range(1, 10):
            # For all remaining digits, they can be anything from 0 to (msd-1)
            count += (msd) ** (length - 1)
    
    # Count numbers with the same number of digits as n
    msd = int(str_n[0])
    for i in range(1, d):
        for m in range(1, msd):
            # For numbers with MSD = m, all subsequent digits can be anything from 0 to (m-1)
            count += (m) ** (d - 1 - i)
        
        if int(str_n[i]) < msd:
            break
        elif int(str_n[i]) > msd:
            break
        else:
            continue
    
    # Check if the number n itself satisfies the condition
    if all(int(str_n[i]) < msd for i in range(1, d)):
        count += 1
    
    return count


a,b=map(int,input().split())
print(count_numbers_with_strict_msd(b))  # Output will be the count of numbers
