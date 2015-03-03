a = input("Enter a: ")
a = int(a)
b = input("Enter b: ")
b = int(b)

oper = input("Enter operation between those: +, -, *, /")

if oper == "+":
    print ("The result is:\n" + str(a+b))
elif oper == "-":
    print ("The result is:\n" + str(a-b))
elif oper == "*":
    print ("The result is:\n" + str(a*b))
elif oper == "/":
    print ("The result is:\n" + str(a/b))
else:
    print("Another operation.")
