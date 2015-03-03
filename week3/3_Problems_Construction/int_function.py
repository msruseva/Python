n = input("Enter n: ")
n = int(n)

def reverse_int(n):
    reverse_n = 0
    while n != 0 :
        digit = n % 10
        reverse_n = reverse_n * 10 + digit
        n = n // 10
    return reverse_n

def sum_digit(n):
    sum_n = 0
    while n != 0:
        digit = n % 10
        sum_n = digit + sum_n
        n = n // 10
    return sum_n

def product_digits(n):
    prod_n = 1
    while n != 0:
        digit = n % 10
        prod_n = digit * prod_n
        n = n // 10
    return prod_n

print("Reverse number is: " + str(reverse_int(n)))
print("Sum of the digits in the number is: " + str(sum_digit(n)))
print("Product of the digits in the number is: " + str(product_digits(n)))
