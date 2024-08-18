#find the sum of all primes less than 20000000
import math
import time
t_sum = 2
n = 200000
#Brute force.u
start=time.time()
for i in range(3,n,2):
    prime_check=True
    for j in range(2, int(math.sqrt(i)) + 1):
        if(i %j ==0):
            prime_check=False
            break;
    if(prime_check):
        t_sum += i
print("Brute Force: " + str(t_sum))
print("Brute Force Time: " + str(time.time()-start))

#sieve of Eratosthenes
def solution_sieve(n):
    sieve = [True] * (n+1) #Marking all numbers are prime. 
    p=2 #Initial Prime Number
    while p*p <=n: #this will be false when pursuing number p is greater than sqrt(n)
        if sieve[p]:
            for i in range(p*p, n+1, p):
                sieve[i] = False
        p+=1
    return sum(i for i in range(2,n) if sieve[i])
start =time.time()
print("Sieve of Eratosthenes: " + str(solution_sieve(n)))
print("Sieve of Eratosthenes Time: " + str(time.time()-start))
