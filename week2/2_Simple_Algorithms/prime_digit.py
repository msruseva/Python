n = input("Enter n: ")
n = int(n)

digits = []

while n != 0:
    digit = n % 10
    digits = digit + [digit]
    n = n // 10

has_prime_digit = False

for digit in digits:
    if digit in [2,3,5,7]:
        has_prime_digit = True
        break

if has_prime_digit:
    print("At least one prime digit found")
else:
    print("No prime digits found")


