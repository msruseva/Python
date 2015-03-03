n = input("Enter n: ")
n = int(n)

count = 1
max_list = []
max_num = 0

while count <= n:
    num = input("Enter num: ")
    num = int(num)
    max_list += [num]
    count += 1
for i in max_list:
    if i > max_num:
        max_num = i
print("Max is " + str(max_num))
        
    
