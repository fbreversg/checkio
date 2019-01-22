import re


def repeat_inside(line):
    """
        first the longest repeating substring
    """
    pattern = ''
    for i in range(len(line)):
        for j in range(len(line) - i):
            test = line[i:i + j + 1]
            for k in range(2, len(line) // len(test) + 1):
                ls = test * k
                if ls in line and len(ls) > len(pattern):
                    pattern = ls
    return pattern


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert repeat_inside('aaaaa') == 'aaaaa', "First"
    assert repeat_inside('aabbff') == 'aa', "Second"
    assert repeat_inside('aababcc') == 'abab', "Third"
    assert repeat_inside('abc') == '', "Forth"
    assert repeat_inside('abcabcabab') == 'abcabc', "Fifth"
    print('"Run" is good. How is "Check"?')
