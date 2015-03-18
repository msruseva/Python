n = input("Enter number n: ")
n = int(n)

digits_list = []
num = 0

while n != 0:
    digit = n % 10
    digits_list = [digit] + digits_list
    n = n // 10
    
print("List of digits is: " + str(digits_list))

for digit in digits_list:
    num = num * 10 + digit
    
print("Number is: "+ str(num))
