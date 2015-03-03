n = input("Enter count of number: ")
n = int(n)

count = 1
numbers = []

while count <= n:
    number = input("Enter number: ")
    number = int(number)
    numbers = numbers + [number]
    count = count + 1
print(numbers)
