thresholds = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    '_': 1000,
    '_': 5000,
    '_': 5000,
}


class RomanNumerals:
    def to_roman(self, val):
        if val < 1 or val > 4000: return ''
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
    def from_roman(roman_num):
        roman_num = roman_num.upper()
        roman_num_len = len(roman_num)
        integer = 0

        ending = {
            'IX': 9,
            'IV': 4,
            'VI': 6
        }

        for i, r in enumerate(roman_num):
            has_next = i + 1 < roman_num_len
            curr_n = thresholds[roman_num[i]]
            next_n = has_next and thresholds[roman_num[i + 1]]

            if has_next and (roman_num[i] + roman_num[i+1]) in ending and roman_num.endswith(roman_num[i] + roman_num[i+1]):
                integer += ending[roman_num[i] + roman_num[i+1]]
                break
            elif curr_n < next_n:
                integer += next_n - curr_n
            else:
                integer += curr_n
        return integer

print(RomanNumerals().to_roman(1429)) # MCDXXIX
