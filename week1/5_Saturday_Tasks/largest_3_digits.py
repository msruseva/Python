n = input("Enter n: ")
n = int(n)


digit_l = n % 10
digit_m = n // 10 % 10
digit_f = n // 100 % 10

largest = 0
middle = 0
lowest = 0

if digit_l >= digit_m and digit_l >= digit_f and digit_m >= digit_f:
    largest = digit_l
    middle = digit_m
    lowest = digit_f
elif digit_l >= digit_m and digit_l >= digit_f and digit_m <= digit_f:
    largest = digit_l
    middle = digit_f
    lowest = digit_m
elif digit_m >= digit_l and digit_m >= digit_f and digit_l >= digit_f:
    largest = digit_m
    middle = digit_l
    lowest = digit_f
elif digit_m >= digit_l and digit_m >= digit_f and digit_l <= digit_f:
    largest = digit_m
    middle = digit_f
    lowest = digit_l
elif digit_f >= digit_l and digit_f >= digit_m and digit_m >= digit_l:
    largest = digit_f
    middle = digit_m
    lowest = digit_l
elif digit_f >= digit_l and digit_f >= digit_m and digit_m <= digit_l:
    largest = digit_f
    middle = digit_l
    lowest = digit_m
else:
    print("else")

print(str(largest) + str(middle) + str(lowest))
print(str(lowest) + str(middle) + str(largest))

