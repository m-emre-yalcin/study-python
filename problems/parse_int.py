def parse_int(string):
    parts = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
        "twenty": 20,
        "thirty": 30,
        "forty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90,
        "hundred": 100,
        "thousand": 1000,
        "million": 1000000
    }
    string = string.replace(' and ', ' ').replace('-',' ').split(' ')
    result = parts[string[0]]
    max = 0
    l = len(string)
    i = 0

    for str in string:
        if max < parts[str]:
            max = parts[str]

    while i + 1 < l:
        if parts[string[i]] == max: # threashold for separating sections
            i+=1 # next
            sum = parts[string[i]]

            while i + 1 < l:
                if parts[string[i]] < parts[string[i + 1]]:
                    sum *= parts[string[i + 1]]
                else:
                    sum += parts[string[i + 1]]
                i+=1
            result += sum
            break
        elif parts[string[i]] < parts[string[i + 1]]:
            result *= parts[string[i + 1]]
        else:
            result += parts[string[i + 1]]

        i+=1
    return result

print(parse_int("two hundred"))
# print(parse_int("seven hundred eighty-three thousand nine hundred and nineteen")) # 783.919 = (7 * 1000 * (100 + 83)) + (9 * 100) + 19