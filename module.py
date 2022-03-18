#Prob1 Modules
import math

def sqrt(x):
    """
    Returns the square root of x.
    """
    return math.sqrt(x)
def factorial(n):
    """
    Returns the factorial of n.
    """
    return math.factorial(n)
def ebob(a,b):
    """
    Returns the greatest common divisor of a and b.
    """
    return math.gcd(a,b)
def ekok(a,b):
    """
    Returns the least common multiple of a and b.
    """
    return math.lcm(a,b)
def isPrime(n):
    """
    Returns True if n is prime, False otherwise.
    """
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def circleArea(r):
    """
    Returns the area of a circle with radius r.
    """
    return math.pi * (r * 2)

def add(a,b):
    """
    Returns the sum of a and b.
    """
    return a + b
def sub(a,b):
    """
    Returns the difference of a and b.
    """
    return a - b
def mul(a,b):
    """
    Returns the product of a and b.
    """
    return a * b
def div(a,b):
    """
    Returns the quotient of a and b.
    """
    return a / b
def log(a,b):
    """
    Returns the logarithm of a to the base b.
    """
    return math.log(a,b)