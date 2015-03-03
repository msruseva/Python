def last(fib_n):
    return fib_n[len(fib_n) - 1]

def before_last(fib_n):
    return fib_n[len(fib_n) - 2]

# ф-я, която връща списък с първите n елемента от ред. на Фибоначи
def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    result = [1, 1]
    while len(result) < n:
        nex_fib = last(result) + before_last(result)
        result = result + [next_fib]
    return result    
    
# ф-я, която взима едно цяло число и върща броя на неговите цифри
def count_digit(n):
    result = 0
    while n != 0:
        result += 1
        n = n // 10
    return result

# ф-я, която взима списък от цели числа, които може да са с повече от една цифра
# и връща цяло число, което е конкатенация от числата в списъка
def to_number(numbers):
    result = 0
    for number in numbers:
        multiplier = 10 ** count_digits(number)
        result = result * multiplier + number
    return result

def fin_number(n):
    return to_number(fib(n))
