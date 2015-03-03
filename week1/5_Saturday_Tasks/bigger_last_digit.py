n = input("Enter n: ")
m = input("Enter m: ")

n = int(n)
m = int(m)

n_last_digit = n % 10
m_last_digit = m % 10

if n_last_digit > m_last_digit:
    print(n)
elif n_last_digit < m_last_digit:
    print(m)
elif n > m:
    print(n)
elif n < m:
    print(m)


