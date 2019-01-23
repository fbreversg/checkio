def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    beg_index = text.find(begin)
    end_index = text.find(end)

    if beg_index == end_index:
        return text
    elif beg_index == -1:
        return text[0:end_index]
    elif end_index == -1:
        return text[beg_index+len(begin):]
    else:
        return text[beg_index+len(begin):end_index]


if __name__ == '__main__':
    print('Example:')
    print(between_markers('No [b]hi', '[b]', '[/b]'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
