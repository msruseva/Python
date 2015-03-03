from random import randint

def generate_random_list(n, start, end):
    result = []
    while n >= 1:
        result = result + [randint(start, end)]
        n -= 1
    return result
