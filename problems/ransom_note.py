# Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.
def ransom_note(ransom_note, magazine):
    while len(ransom_note):
        try:
            j = magazine.index(ransom_note[0])
            magazine = magazine.replace(magazine[j], '', 1)
            ransom_note = ransom_note.replace(ransom_note[0], '', 1)
        except Exception as e: # not found
            print(e)
            return False
    return True

print(ransom_note("aa", "aba"))