a = input("Enter a: ")
b = input("Enter b: ")

a = int(a)
b = int(b)

if a > b:
    while b <= a:
        print(b)
        b = b + 1
else:
    while a <= b:
        print(a)
        a = a + 1

