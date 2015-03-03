def square(x):
    return x ** 2

def factoriel(x):
    if x == 0:
        return 1
    else:
        result = 1
        while x != 0:
            result = result * x
            x -= 1
        return result

def count_elements(items):
    count = 0
    for x in items:
        count += 1
    return count

def member(x, xs):
    for i in xs:
        if x == i:
            return True
    return False

def grades_that_pass(students, grades, limit):
    result = []
    count = 0
    while count < len(grades):
        if grades[count] >= limit:
            result = result + [students[count]]
        count += 1
    print (result)
