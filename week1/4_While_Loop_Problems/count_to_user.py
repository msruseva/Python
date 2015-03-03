n = input("Enter number: ")
n = int(n)

counter = 0

while True:
    if counter == n:
        break
    else:
        counter = counter + 1
        print(counter)

while True:
    if counter == 1:
        print(counter)
        break
    else:
        print(counter)
        counter = counter - 1

