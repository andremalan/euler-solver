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
print largest_prime_factor(600851475143)
#print generate_primes(10000)
