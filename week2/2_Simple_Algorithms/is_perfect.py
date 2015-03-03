n = input("Enter n: ")
n = int(n)

count = 1
sum_n = 0

while count < n:
    if n % count == 0:
        sum_n = sum_n + count
    count += 1
if sum_n == n:
    print(str(n) + " is perfect number - the sum of it's divisors is equal to it")
