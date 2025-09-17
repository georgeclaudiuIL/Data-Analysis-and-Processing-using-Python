from django.test import TestCase

# Create your tests here.

def factorial_recursiv(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursiv(n-1)

print(factorial_recursiv(5))
