n = input("Enter n: ")
n = int(n)

reverse_n = 0

while n != 0:
    digit = n % 10
    reverse_n = reverse_n * 10 + digit
    n = n // 10
print(reverse_n)
    
    
