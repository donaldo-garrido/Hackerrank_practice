# Challenge: String Validators

# TASK:

# You are given a string S.
# Your task is to find out if the string contains: 
# alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

if __name__ == '__main__':
    s = input()

    # all alphanumeric? str.isalnum()
    # all alphabetical? str.isalpha()
    # all digits? str.isdigit()
    # all lowercase? str.islower()
    # all uppercase? str.isupper()

    # Lists to check all categories
    alphanumeric = []
    alphabetical = []
    digits = []
    lowercase = []
    uppercase = []

    # Check character per character
    for character in s:
        alphanumeric.append(character.isalnum())
        alphabetical.append(character.isalpha())
        digits.append(character.isdigit())
        lowercase.append(character.islower())
        uppercase.append(character.isupper())

    # If any of the characters is in the category
    # print True. Otherwise, print False.
    if True in alphanumeric:
        print(True)
    else:
        print(False)

    if True in alphabetical:
        print(True)
    else:
        print(False)

    if True in digits:
        print(True)
    else:
        print(False)

    if True in lowercase:
        print(True)
    else:
        print(False)

    if True in uppercase:
        print(True)
    else:
        print(False)