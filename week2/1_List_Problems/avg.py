n = input("Enter n:")
n = int(n)

count = 1
avg_list = []
sum_n = 0
avg_sum = 0

while count <= n:
    num = input("Enter num: ")
    num = int(num)
    avg_list += [num]
    count += 1
for i in avg_list:
    sum_n = sum_n + i

avg_sum = sum_n / n
print("Avg is: " + str(avg_sum))
