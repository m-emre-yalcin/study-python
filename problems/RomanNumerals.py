thresholds = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    '': 1000,
    '': 5000,
}


class RomanNumerals:
    def to_roman(self, val):
        if val < 1 and val > 4000: return ''
        
        roman = ''
        digits = str(val)
        roman_thresholds = list(thresholds.keys())
        roman_five_based_thresholds = list(filter(lambda key: str(thresholds[key]).startswith('5'), roman_thresholds))
        roman_one_based_thresholds = list(filter(lambda key: str(thresholds[key]).startswith('1'), roman_thresholds))

        for i, number in enumerate(digits):
            number = int(number)
            digit = len(digits) - i
            index = digit - 1
            base = number * (10 ** (digit - 1))
            mod = number % 5
            roman_number = roman_thresholds[index]
            th = thresholds[roman_number]

            print({ 'digit': digit, 'index': index, 'number': number, 'base': base, 'mod': mod, 'roman_number': roman_number, 'roman_one_based_thresholds': roman_one_based_thresholds[index], 'roman_five_based_thresholds': roman_five_based_thresholds[index], 'th': th})

            if number:
                if mod < 4: # 0, 1, 2, 3, 6, 7, 8
                    if number < 4:
                        for n in range(mod): roman+= roman_one_based_thresholds[index]
                    else:
                        roman+= roman_five_based_thresholds[index]
                        for n in range(mod): roman+= roman_one_based_thresholds[index]
                elif mod == 4: # 4, 9
                    if number == 4:
                        roman += roman_one_based_thresholds[index] + roman_five_based_thresholds[index]
                    elif number == 9:
                        roman += roman_one_based_thresholds[index] + roman_one_based_thresholds[digit]

        return roman
    def from_roman(self, roman_num):
        roman_num = roman_num.upper()
        roman_num_len = len(roman_num)
        integer = 0
        i = 0

        while i < roman_num_len:
            has_next = i + 1 < roman_num_len
            th = thresholds[roman_num[i]]
            next_th = has_next and thresholds[roman_num[i + 1]]

            if th < next_th:
                integer += next_th - th
                i = i + 1 # 2 step next
            else:
                integer += th

            i += 1
        return integer

print(RomanNumerals().to_roman(3999))
