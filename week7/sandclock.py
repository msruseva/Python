n = input("Enter number: ")
n = int(n)

star = n
point = 0

while star >= 0:
    print(point * "." + star * "*" + point * ".")
    point += 1
    star -= 2

star += 4
point -= 2

while star <= n:
    print (point * "." + star * "*" + point * ".")
    point -= 1
    star += 2
