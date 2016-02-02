def count_words(text, words):
    counter = 0
    for word in words:
        if text.lower().find(word) != -1:
            counter += 1

    return counter

count_words('How aresjfhdskfhskd you?', ['you', 'how', 'hello', 'are'])