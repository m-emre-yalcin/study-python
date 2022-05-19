def unique_in_order(iterable):
    return [c for i, c in enumerate(iterable) if i + 1 == len(iterable) or c != iterable[i + 1] ]

print(unique_in_order([1,2,2,3,3]))