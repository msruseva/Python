a = input("Enter a - lower bound of the interval: ")
a = int(a)
b = input("Enter b - upper bound of the interval: ")
b = int(b)
n = input("Enter number: ")
n = int(n)

if n == a:
    print("The number is equal to the lower bound of the interval.")
elif n == b:
    print("The number is equal to the upper bound of the interval.")
elif a<n and n<b:
    print("The number is in the interval.")
elif n < a:
    print("The number is outside the interval, n<a.")
else:
    print("The number is outside the interval, n>b.")
