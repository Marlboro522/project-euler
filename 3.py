import math

def max_prime_factors(n):
    largest_prime = -1
    i = 2
    while i * i <= n:
        while n % i == 0:
            largest_prime = i
            n = n // i
        i = i + 1
    if n > 1:
        largest_prime = n
    return largest_prime
print(max_prime_factors(600851475143))