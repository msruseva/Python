n = input("Enter n: ")
n = int(n)

count = 1
min_list = []
min_num = 0

while count <= n:
    num = input("Enter num: ")
    num = int(num)
    min_list += [num]
    count += 1
for i in min_list:
    if i < min_num:
        min_num = i
print("Min is: " + str(min_num))
