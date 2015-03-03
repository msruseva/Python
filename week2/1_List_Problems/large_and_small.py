n = input("Enter n: ")
n = int(n)

n_list = []
smaller = 0
bigger = 0

while n != 0:
    digit = n % 10
    n_list = n_list + [digit]
    n = n // 10
print(n_list)

smaller_list = sorted(n_list, reverse = True)
bigger_list = sorted(n_list)

for i in smaller_list:
    


