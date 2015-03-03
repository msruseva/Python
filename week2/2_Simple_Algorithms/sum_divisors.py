n = input("Enter n: ")
n = int(n)

count = 1
n_sum = 0

while count < n:
    if n % count == 0:
        n_sum = n_sum + count
    count += 1
print(n_sum)
