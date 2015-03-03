n = input("Enter n: ")
n = int(n)

not_rev_n = n
rev_n = 0

while n != 0:
    digit = n % 10
    rev_n = rev_n * 10 + digit
    n = n // 10
    
if not_rev_n == rev_n:
    print(str(not_rev_n + " is palindrom.")
else:
    print(str(not_rev_n) + " is not palindrom.")
    
