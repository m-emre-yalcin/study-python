def valid_parentheses(string, opened=0):
    if not opened and string == '':
        return True
    for i, s in enumerate(string):
        if s == '(':
            opened += 1
            return valid_parentheses(string[i+1:], opened)
        elif s == ')':
            if not opened: return False
            opened -= 1

    return not opened and len(string) >= 0 and len(string) <= 100

print(valid_parentheses("hi(()())(")) # returns True or False regarding its validity