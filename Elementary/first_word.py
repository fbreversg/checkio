import re


def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    p = re.compile(r'[A-Za-z\']+')
    return re.findall(p, text)[0]



if __name__ == '__main__':
    print("Example:")
    print(first_word(" a word "))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")
