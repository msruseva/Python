n = input("Enter n:")
n = int(n)

counter = 0
sum_n = 0

while counter <= n:
    if counter%2 == 0:
        sum_n = sum_n + counter
        counter = counter + 1
    else:
        counter = counter + 1
print(sum_n)     
