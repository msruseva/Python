def count_zero_neighbours(numbers):
    count = 0
    for n in numbers:
        if numbers[n] + numbers[n+1] == 0:
            count += 1
    return count

print(count_zero_neighbours([1, 2, -2, 0, 0, 5, -5]))

def count_zero_pairs(numbers):
    count = 0
    index = 0
    n = len(numbers)
    for x_index in range(0, n):
        for y_index in range(x_index, n):
            x = numbers[x_index]
            y = numbers[y_index]
            if x + y == 0:
                count += 1
    return count

print(count_zero_pairs([0, 2, -2, 5, 10]))

def is_prime(n):
    start = 2
    is_prime = True
    while start < n:
        if n % start == 0:
            is_prime = False
            break
        start += 1
    return is_prime
        

def prime_pair(numbers):
    n = len(numbers)
    for x in numbers:
        for y in numbers:
            if is_prime(x + y):
                return True
    return False

print(prime_pair([1, 2, 3, 4, 5]))
