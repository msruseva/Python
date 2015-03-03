n = input("Enter n: ")
n = int(n)

n_list = []
count = 1

while count < n:
    if n % count == 0:
        n_list = n_list + [count]
    count += 1
print(n_list)
