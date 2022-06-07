def valid_paranthesis(s):
    model = { "(": ")", "[": "]", "{": "}" }

    def validate(s, tier=0):
        if tier < 0 or tier == len(s) or tier - 1 > len(s) or s == "":
            return s
        if s[tier] in model:
            tier+=1
            return validate(s, tier)
        elif s[tier - 1] in model and model[s[tier - 1]] == s[tier]:
            s = s[:tier - 1] + s[tier + 1:]
            tier=tier-1
            return validate(s, tier)
        else:
            return False

    return len(str(validate(s))) == 0
    

print(valid_paranthesis("["))