primes = 0

for x in range(2, 2000):
    isPrime = True
    for i in range(2, x):
        if (x % i) == 0:
            isPrime = False
            break
        else:
            continue
    if isPrime == True:
        primes = primes + x

print(primes)
