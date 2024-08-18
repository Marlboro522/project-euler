import math
def find_divisors(number: int) -> int:
    divisors = 2
    for i in range(2, int(number/2) + 1):
        if (number % i == 0):
            divisors += 1
            # print(i)
    return divisors
print(find_divisors(20))
# print(find_divisors(76576500))

def traingle_number(number: int) -> int:
    return int((number * (number + 1)) / 2)
i=1
while True:
    number = traingle_number(i)
    print(number)
    if find_divisors(number) > 500:
        print(number)
        break
    i += 1


