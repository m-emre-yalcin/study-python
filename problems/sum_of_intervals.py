def sum_of_intervals(intervals):
    N = set()
    
    for start, end in intervals:
        for n in range(start, end):
            N.add(n)

    return len(N)

print(sum_of_intervals([
   (1, 4), (7, 10), (3, 5)
]))