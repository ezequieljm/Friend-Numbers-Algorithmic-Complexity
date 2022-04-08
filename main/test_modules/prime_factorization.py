from math import sqrt
from execution_time import execution_time

########################################################################################################
#
########################################################################################################

# prime_seive :: Int -> [Int]
# @execution_time.execution_time
def prime_seive1(n):
    is_prime = [True for _ in range(n + 1)]
    is_prime[0], is_prime[1] = False, False

    for i in range(2, int(n ** 0.5) + 1):
        for j in range(2 * i, n + 1, i):
            is_prime[j] = False

    return [x for x in range(1, n + 1) if is_prime[x]]


# primes_factors :: Int -> [Int] -> [Int]
# @execution_time.execution_time
def primes_factors(num, primes):
    prime_factors = []
    # while not num in primes:
    while num > 1:
        for i in primes:
            if num % i == 0:
                num //= i
                prime_factors.append(i)
                break
    prime_factors.append(num)

    return prime_factors

# dividers_by_prime_factorization :: Int -> Int
# @execution_time.execution_time
def dividers_by_prime_factorization(num, primes):
    facts = primes_factors(num, primes)
    d = dict()
    for i in facts:
        d[str(i)] = d.get(str(i),0) + 1

    facts2 = set()
    facts3 = set()

    for i in d.keys():
        facts1 = set()
        for j in range(d[i] + 1):
            facts1.add(int(i) ** j)

        for f2 in facts2:
            for f1 in facts1:
                facts3.add(f2 * f1)

        for f in facts1:
            facts2.add(f)

    result = set([i for i in facts3])
    for f3 in facts3:
        result.add(num // f3)
    val = sum(result - {num})
    print(f"{num} : {val}")
    return  val

# Calculate all dividers of numbers into a range
# sum_dividers_by_factorization_in_range :: Int -> [[Int]]
@execution_time.execution_time
def dividers_by_factorization_in_range(limit, prime_list):
    return {str(x) : dividers_by_prime_factorization(x, prime_list) for x in range(2, limit + 1)}

########################################################################################################
#
########################################################################################################

# prime_seive0 :: Int -> [Int]
@execution_time.execution_time
def prime_seive0(n):
    num = int(sqrt(n))
    l = [0] * (num + 1)
    primes_until_of = []

    for i in range(2, num + 1):
        if l[i] == 0:
            primes_until_of.append(i)
        for j in range(i * 2,num + 1,i):
            l[j] = 1

    return primes_until_of

# Function calculate lazy prime numbers
def get_lazy_prime():
    current_prime = 2
    yield current_prime
    n = 0
    while True:
        n += 1
        temp = 2*n + 1 # all prime number greatter that 2 is odd
        count_divs = 2
        for x in range(2, int(temp / 2) + 1):
            if temp % x == 0:
                count_divs += 1
                break
        if count_divs == 2:
            current_prime = temp
            yield current_prime


#@execution_time.execution_time
def primes_ultil(value, gen):
    init = next(gen)
    while init <= value:
        print(init)
        init = next(gen)

# prime_factorization_of :: Int -> Int -> [Int] -> [Int]
#@execution_time.execution_time
def prime_factorization_of(num, prime, prime_list):
    prime_factors_of = []
    while num > 1:
        new_prime = next(prime)
        prime_list.append(new_prime)

        for p in prime_list:
            while num > 1 and num % p == 0:
                prime_factors_of.append(p)
                num //= p
            if num == 1:
                break
    return prime_factors_of