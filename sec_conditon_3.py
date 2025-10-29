# Check whether a character is a vowel or consonant.

chr = input("Enter a character:")
vowel = "aeiou"

for item in chr:
    if item in vowel:
        print("Character is Vowel")
    else:
        print("Character is Not Vowel")


