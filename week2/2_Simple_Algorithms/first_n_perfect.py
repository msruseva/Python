n = input("Enter n: ")
n = int(n)

count = 1
sum_n = 0
br_n = 0
num = 1

while br_n != n:
    while count < num:
        if num % count == 0:
            sum_n = sum_n + count
        count += 1
    if sum_n == num:
        br_n += 1
        print(str(num))
    num += 1
    sum_n = 0
    count = 1
