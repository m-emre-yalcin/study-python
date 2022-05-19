def first_non_repeating_letter(string):
    for i, s in enumerate(string):
        repeating = False

        for ii, c in enumerate(string):
            if i != ii and s.lower() == c.lower():
                repeating = True
                break

        if not repeating: return s
    return False

print(first_non_repeating_letter("huh stress"))