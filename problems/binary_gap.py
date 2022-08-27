def binary_gap(N):
    dividing = N
    remaining = 0
    binary = ''

    while dividing > 0:
        quotient = int(dividing/2)
        remaining = dividing - quotient * 2
        binary += str(remaining)  # 1 or 0
        dividing = quotient

    binary = binary[::-1]  # reverse
    gaps = [0] * len(binary)

    print("binary:", binary)

    for i, bit in enumerate(binary):
        if bit == '1':  # start
            for bit in binary[i + 1:]:
                if bit == '0':
                    gaps[i] += 1  # gap
                if bit == '1':
                    break  # end

            try:
                if gaps[i] and binary[i + 1 + gaps[i]] is not '1':  # enclosing
                    print("index:", i + gaps[i])
                    gaps[i] = 0  # end
            except:
                gaps[i] = 0  # end
    return max(gaps)


print(binary_gap(156))
