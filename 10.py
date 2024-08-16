#find the sum of all primes less than 20000000
import math
sum = 2

#Brute force.u
for i in range(3,2000000,2):
    prime_check=True
    for j in range(2, int(math.sqrt(i)) + 1):
        if(i %j ==0):
            prime_check=False
            break;
    if(prime_check):
        sum += i
print(sum)

#sieve of Eratosthenes
