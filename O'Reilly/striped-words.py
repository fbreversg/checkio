import re

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"

def checkio(text):

    text = text.upper()
    words = re.split("[^A-Z0-9]+", text)

    count = 0
    valid = True
    for word in words:

        if len(word) > 1 and word.isalpha():
            valid = True
            for i in range(0, len(word)-1):
                if word[i] in VOWELS and word[i+1] in VOWELS:
                    valid = False
                    break

                if word[i] in CONSONANTS and word[i+1] in CONSONANTS:
                    valid = False
                    break

            if valid:
                count += 1

    return count


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
