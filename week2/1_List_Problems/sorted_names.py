n = input("Enter n: ")
n = int(n)

count = 1
name_list = []

while count <= n:
    name = input("Enter name: ")
    name_list += [name]
    count += 1
print(sorted(name_list))
