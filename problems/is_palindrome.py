def is_polindrome(x):
    i = 0
    x = str(x)
    while i < len(x) // 2:
        if x[i] != x[-i - 1]:
            return False
        i+=1
    return True

print(is_polindrome(121))