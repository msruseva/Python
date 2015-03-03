n = input("Enter n: ")
n = int(n)

count = 0
i = 1

while i <= n:
    if n % i == 0:
        count = count + 1
        i = i + 1
    else:
        i = i + 1
if count > 2:
    print(str(n) + " is not prime.")
else:
    print(str(n) + " is prime.")
