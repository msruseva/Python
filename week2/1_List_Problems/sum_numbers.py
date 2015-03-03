n = input("Enter n: ")
n = int(n)

count = 1
n_list = []
n_sum = 0

while count <= n:
    num = input("Enter num: ")
    num = int(num)
    n_list = n_list + [num]
    count = count + 1
for i in n_list:
    n_sum = n_sum + i
print("The sum is: " + str(n_sum))
