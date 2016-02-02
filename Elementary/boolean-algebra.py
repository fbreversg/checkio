OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):

    if operation == "conjunction":
        return x and y
    if operation == "disjunction":
        return x or y
    if operation == "implication":
        return not x or y
    if operation == "exclusive":
        return (x or y) and not (x and y)
    if operation == "equivalence":
        if x == y:
            return True
        else:
            return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"
