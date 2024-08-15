def is_palindrome(n):
    return str(n) == str(n)[::-1]
def largest_palindrome():
    l_p=0
    for i in range(100,1000):
        for j in range(100,1000):
            if is_palindrome(i*j):
                if i*j>l_p:
                    l_p=i*j
    return l_p
print(largest_palindrome())