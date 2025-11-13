'''Exercise 1: Python Basics and Data Types'''
def is_prime(n):
    if n <= 1:
        return 'Not Prime'
    if n == 2:
        return 'Prime'
    if n % 2 == 0:
        return "Not Prime"

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return 'Not Prime'
    return 'Prime'

n = int(input("Enter a number: "))
print(is_prime(n))
