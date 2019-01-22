def checkio(number):
    solution = ''

    while True:
        if not is_divisible_by_prime(number):
            return 0

        for divisor in range(9, 2, -1):
            if is_divisible(number, divisor):
                number = number // divisor
                solution += str(divisor)
                break

        if number < 10:
            solution += str(number)
            break

    return int(solution[::-1])


def is_divisible_by_prime(number):
    primes = [2, 3, 5, 7]
    for prime in primes:
        if number % prime == 0:
            return True
    return False


def is_divisible(number, by):
    return number // by and number % by == 0


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"
