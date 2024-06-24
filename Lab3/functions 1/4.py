def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(x):
    primes = [i for i in x if is_prime(i)]
    print(' '.join(map(str, primes)))

filter_prime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
