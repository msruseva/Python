def divisors(n):
    count = 1
    result = []
    while count < n:
        if n % count == 0:
            result = result + [count]
        count += 1
    return result
