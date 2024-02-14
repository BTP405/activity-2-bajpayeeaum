def getPrimeNumbers(n):
    if n < 2:
        return []
    primes = [2]
    for x in range(3, n + 1, 2):
        is_prime = True
        for p in primes:
            if x % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(x)
    return primes

while True:
    n = int(input("Enter a value for n (enter 0 to exit): "))
    if n == 0:
        print("Exiting the program.")
        break
    primes_up_to_n = getPrimeNumbers(n)
    primes_str = ', '.join(map(str, primes_up_to_n))
    print("Prime numbers up to", n, "are:", primes_str)

