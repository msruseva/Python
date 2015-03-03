n = input("Enter n: ")
n = int(n)

i = 1
pro = 1

if n == 0:
    print(str(n) + "! = 1")
else:
    while i <= n:
        pro = pro * i
        i = i + 1
    print(str(n) + "! = " + str(pro))
    
