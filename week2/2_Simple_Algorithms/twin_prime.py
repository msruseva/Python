p = input("Enter p: ")
p = int(p)

q = p - 2
t = p + 2

def is_prime(n):
    start = 2
    is_prime = True

    while start < n:
        if n % start == 0:
            is_prime = False
            break
        start += 1
    return is_prime

if is_prime(p) == False:
    print(str(p) + " is not a prime")
elif is_prime(p) == True and is_prime(q) == True and is_prime(t) == True:
    print("Twin primes with " + str(p) + ":")
    print(str(q) + ", " + str(p))
    print(str(p) + ", " + str(t))
elif is_prime(p) == True and is_prime(q) == True and is_prime(t) == False:
    print(str(p) + " and " + str(q) + " are prime but: ")
    print(str(t) + " is not.")
elif is_prime(p) == True and is_prime(q) == False and is_prime(t) == False:
    print(str(p) + " is prime but:")
    print(str(q) + " is not.")
    print(str(t) + " is not.")
    

