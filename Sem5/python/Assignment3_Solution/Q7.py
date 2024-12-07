def alpha(char):
    if len(char)!=1 or not char.isalpha():
        return "Invalid input"
    return "vowel" if char.lower() in "aeiou" else "consonant"
print(alpha('d'))