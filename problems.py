import math

# What is the largest prime factor of the number 600851475143 ?
def problem3():
    return largest_prime_factor(600851475143)

# Find the largest palindrome made from the product of two 3-digit numbers.
def problem4():
    return largest_palindrome_product()





#problem 4


#dumb way
def largest_palindrome_product():

    palindromes = []
    for i in range(0,899):
        for j in range(0,899):
            product = (999-i) * (999-j)
            if is_palindrome(product): 
                palindromes.append(product)
    palindromes.sort()
    return palindromes.pop()

#has to be a better way to do this in Python
def is_palindrome(n):
    first = ((n % 1000000) / 100000) == (n % 10)
    second = ((n % 100000) /  10000) == ((n % 100)/10)
    third = ((n % 10000) /  1000) == ((n % 1000)/100)
    return first and second and third
  




#function too slow
def generate_primes(n):
    primes = [2]
    for number in range(3,n):
        is_prime = True 
        for p in primes:
            if number % p == 0:
                is_prime = False
        if is_prime:
            primes.append(number)
    return primes


#problem 3
def largest_prime_factor(n):
    primes= generate_primes(10000)
    primes.sort(reverse=True)
    for p in primes:
        if n % p == 0:
            return p
    return "no prime"

def prime_factors(n):
    factors = []
    primes= generate_primes(n)
    for p in primes:
        if n % p == 0:
            factors.append(p)
    return factors 




