import string

def check_pangram(text):

    for letter in string.ascii_uppercase:
        if letter not in text.upper():
            return False
    return True


