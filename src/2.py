# sum of even numbers in a fibonacci sequence less thatn 4000000
def fibon_sum():
    a, b = 0, 1
    sum = 0
    while b < 4000000:
        if b % 2 == 0:
            sum += b
        a, b = b, a+b
    print(sum)
fibon_sum()