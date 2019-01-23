def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    max_count = 0
    sel_char = ''
    char_count = 0

    if len(line) == 0:
        return 0

    for char in line:
        if char == sel_char:
            char_count += 1
        else:
            sel_char = char
            char_count = 1

        if char_count > max_count:
            max_count = char_count

    return max_count


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('aa') == 2, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
