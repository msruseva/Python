def divisors(n):
    count = 1
    result = []
    while count < n:
        if n % count == 0:
            result = result + [count]
        count += 1
    return result

def sum_ints(numbers):
    sum_numbers = 0
    count = 0
    while count < len(numbers):
        sum_numbers = sum_numbers + numbers[count]
        count += 1
    return sum_numbers

def is_perfect(n):
    if sum_ints(divisors(n)) == n:
        return True
    else:
        return False


n = input("Enter n: ")
n = int(n)

count = 0
count_numbers = 1
while count <= n:
    if is_perfect(count_numbers) == True:
        count += 1
        print (count_numbers)
    count_numbers += 1

