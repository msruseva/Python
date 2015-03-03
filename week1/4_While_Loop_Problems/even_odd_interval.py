a = input("Enter a: ")
b = input("Enter b: ")

a = int(a)
b = int(b)

while a >= b :
    if b%2 == 0:
        print(str(b) + " - " + " even")
        b = b + 1
    else:
        print(str(b) + " - " + " odd")
        b = b + 1

while a <= b :
    if a%2 == 0:
        print(str(a) + " - " + " even")
        a = a + 1
    else:
        print(str(a) + " - " + " odd")
        a = a + 1
