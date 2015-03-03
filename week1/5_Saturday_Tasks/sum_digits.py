n = input("Enter n: ")
n = int(n)

sum_d = 0
  
while n != 0:
    digit = n % 10
    n = n // 10
    sum_d = sum_d + digit
    
print(sum_d)
