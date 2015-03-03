def is_prime(n):
    start = 2
    is_prime = True
    while start < n:
        if n % start == 0:
            is_prime = False
            break
        start += 1
        
    return is_prime

def to_digits(n):
    result = []
    while n != 0:
        digit = n % 10
        result = [digit] + result
        n = n // 10
    return result

n = input("Enter n: ")
n = int(n)

not_prime = "Ne"

for i in to_digits(n):
    if is_prime(i):
        not_prime = "Da"
        break
    
print(not_prime)
