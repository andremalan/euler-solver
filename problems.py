import math

def problem3():
  print "What is the largest prime factor of the number 600851475143 ?"
  print largest_prime_factor(600851475143)

def problem4():
  print "Find the largest palindrome made from the product of two 3-digit numbers."
  print largest_palindrome_product()




#problem 4


def largest_palindrome_product():
  #dumb way
  palindromes = []
  for i in range(0,899):
    for j in range(0,899):
      product = (999-i) * (999-j)
      if is_palindrome(product): 
        palindromes.append(product)
  palindromes.sort()
  return palindromes.pop()

def is_palindrome(n):
  first = ((n % 1000000) / 100000) == (n % 10)
  second = ((n % 100000) /  10000) == ((n % 100)/10)
  third = ((n % 10000) /  1000) == ((n % 1000)/100)
  return first and second and third
      




def generate_primes(n):
  #function too slow
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


#print largest_prime_factor(13195)
#print generate_primes(10000)



