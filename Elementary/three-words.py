def checkio(words):

    words = words.split()

    counter = 0
    result = False

    for word in words:
        if word.isalpha():
            counter +=1
            if counter >= 3:
                return True
        else:
            counter = 0

    return False




