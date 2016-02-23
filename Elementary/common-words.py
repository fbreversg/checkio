def checkio(first, second):
    return ','.join(sorted(list(set(first.split(',')) & set(second.split(',')))))


