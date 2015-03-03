def is_prime(n):
    start = 2
    is_prime = True
    while start < n:
        if n % start == 0:
            is_prime = False
            break
        start += 1
        
    return is_prime

p = input("Enter p: ")
p = int(p)

q = p - 2
r = p + 2

if is_prime(p) and is_prime(q) and is_prime(r):
    print("Twin primes with " + str(p) + ":\n"
          + str(q) + "\n"
          + str(r))
elif is_prime(p) and not is_prime(q) and not is_prime(r):
    print(str(p) + " is prime \n"
          + str(q) + " is not \n"
          + str(r) + " is not")
elif is_prime(p) and not is_prime(q) and is_prime(r):
    print("Twin primes with " + str(p) + ": \n"
          + str(r))
elif is_prime(p) and is_prime(q) and not is_prime(r):
    print("Twin primes with " + str(p) + ": \n"
          + str(q))
else:
    print(str(p) + " is not prime.")
