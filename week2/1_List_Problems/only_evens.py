n = input("Enter n: ")
n = int(n)

count = 1
evens = 0
num_list = []
evens_list = []

while count <= n:
    num = input("Enter num: ")
    num = int(num)
    num_list = num_list + [num]
    count = count + 1
for i in num_list:
    if i %2 == 0:
        evens = evens + 1
        evens_list = evens_list + [i]
print("Count of evens: " + str(evens))
print("Evens are: ")
for j in evens_list:
    print(j)
