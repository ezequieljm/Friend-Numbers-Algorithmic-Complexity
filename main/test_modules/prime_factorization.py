#from math import sqrt
from execution_time import execution_time

########################################################################################################
#
########################################################################################################

# prime_seive0 :: Int -> ([Int], [Int])
#@execution_time.execution_time
def prime_seive0(limit):
    is_prime = [True for _ in range(limit + 1)]
    is_prime[0], is_prime[1] = False, False

    for i in range(2, int(limit ** 0.5) + 1):
        for j in range(2 * i, limit + 1, i):
            is_prime[j] = False

    return ([p for p in range(2, limit + 1) if is_prime[p]], [c for c in range(1, limit + 1) if not is_prime[c]])

# prime_seive1 :: Int -> [Int]
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
def sum_dividers_by_prime_factorization(num, primes):
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
    return val

# Calculate all dividers of numbers into a range without primes
# sum_dividers_by_factorization_in_range :: Int -> [[Int]]
#@execution_time.execution_time
def dividers_by_factorization_in_range(prime_list, compose_list):
    return {str(x) : sum_dividers_by_prime_factorization(x, prime_list) for x in compose_list}


# Friend numbers
# friend_numbers :: Int -> IO ()
@execution_time.execution_time
def friend_numbers(limit):
    (primes, composes) = prime_seive0(limit)
    dic = {}
    result = []

    for n in composes:
        nstr = str(n)
        if nstr not in dic:
            dic[nstr] = sum_dividers_by_prime_factorization(n,primes)

        sm1 = dic[nstr]

        if sm1 < n:
            k = str(sm1)
            if k not in dic:
                dic[k] = sum_dividers_by_prime_factorization(sm1, primes)
            
            sm2 = dic[k]

            if sm2 == n:
                result.append((n,sm2))

    return result
    




