a = input("Enter a: ")
a = int(a)
b = input("Enter b: ")
b = int(b)

if a > b:
    print("a(" + str(a) + ") is bigger than b(" + str(b) + ")!")
elif a < b:
    print("b(" + str(b) + ") is bigger than b(" + str(a) + ")!")
else:
    print("a(" + str(a) + ") is equal to b(" + str(b) + ")")
