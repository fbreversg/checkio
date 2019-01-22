import string


def to_encrypt(text, delta):

    ciphered = []
    for char in text:
        if char == ' ':
            next_sym = char
        elif ord(char) - 97 + delta < 25:
            next_sym = string.ascii_lowercase[ord(char) - 97 + delta]
        else:
            next_sym = string.ascii_lowercase[ord(char) - 97 + delta - 26]

        ciphered.append(next_sym)

    return "".join(ciphered)


if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('simple text', 16))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")
