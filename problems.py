import math

# What is the largest prime factor of the number 600851475143 ?
def problem3():
    return largest_prime_factor(600851475143)

# Find the largest palindrome made from the product of two 3-digit numbers.
def problem4():
    return largest_palindrome_product()

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def problem5():
    total = 1
    primes = generate_primes(20) 
    for prime in primes:
        i = 1
        while True:
            if pow(prime, i) > 20:
                total = total * pow(prime,i-1)
                break
            else:
                i+=1
    return total

#problem 4

def problem7():
    #too slow, 12 seconds instead of 1
    primes= generate_primes(104800)
    print len(primes) 
    return primes[10000]

def problem8():
    #pure guess
    return 9*9*8*7*9
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
    numbers = []
    for i in range(0, n, 1):
        numbers.append(True)
    numbers[1] = False
    for i in range(0, n, 2):
        numbers[i] = False
    while primes[-1] < n:
        try:
            primes.append(numbers.index(True))
            for j in range(primes[-1], n, primes[-1]):
                numbers[j] = False
        except ValueError:
            return primes
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




