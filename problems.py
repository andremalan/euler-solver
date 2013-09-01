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
    string_input = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

    list_input = list(string_input)
    candidates =[]
    nums = map((lambda x: int(x)), list_input)
    for i, n in enumerate(nums):
        if n > 7 and i+4 < len(nums):
            sum = nums[i] + nums[i+1] + nums[i+2] + nums[i+3] + nums[i+4]
            if sum > 35: #arbitrary high bar
                candidates.append(nums[i] *  nums[i+1] * nums[i+2] * nums[i+3] * nums[i+4])
    candidates.sort()
    print len(candidates)
    return candidates[-1] 
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




