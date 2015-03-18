# превръщаме число в списък от цифрите му
def to_digits(n):
    result = []
    while n != 0:
        digit = n % 10
        result = [digit] + result
        n = n // 10
    return result

# разглеждаме, случая в който в digits имаме само едноцифрени числа
def to_number(digits):
    result = 0
    for i in digits:
        result = result * 10 + i
    return result

def max_number(n):
    digits = to_digits(n)
    digits = sorted(digits, reverse = True)
    return to_number(digits)

def min_number(n):
    digits = to_digits(n)
    digits = sorted(digits)
    return to_number(digits)

n = input("Enter n: ")
n = int(n)

print(max_number(n))
print(min_number(n))
