def reversed_int(x):
    n = str(x)[::-1]

    if n[-1] == '-':
        n = '-' + n[:-1]

    n = int(n)

    if pow(-2, 31) <= n <= pow(2, 31) - 1:
        return n

    return 0


print(reversed_int(4500))