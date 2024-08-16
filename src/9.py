#pythagorean triplet
# a^2 + b^2 = c^2
#a <b <c
#a+b+c = 1000
# find abc
def pythagorean_triplet():
    for a in range(1,1000):
        for b in range(a,1000):
            c = 1000-a-b
            if a**2+b**2==c**2:
                print(a,b,c)
                return a*b*c
print(pythagorean_triplet())