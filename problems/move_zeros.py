def move_zeros(array):
    return [a for a in array if a > 0] + [a for a in array if a == 0]