from execution_time import execution_time

# Calculate the dividers of any number VERTION 0
# dividers_of :: Int -> [Int]
# @execution_time.execution_time
def dividers_of(num):
    max_value = int(num / 2) + 1
    return [d for d in range(max_value, 1, -1) if num % d == 0]

# Calculate the sum of the divisors of any number VERTION 1
# sum_dividers_of :: Int -> Int
# @execution_time.execution_time
def sum_dividers_of(num):
    half_of_value = int(num / 2) + 1
    result = 1
    for possible_div in range(half_of_value, 1, -1): 
        if num % possible_div == 0 : result += possible_div
    return result

@execution_time.execution_time
def divs_range(limit):
    for x in range(1, limit):
        #print(f"{x}: {sum_dividers_of(x)}")
        #sum_dividers_of(x)
        dividers_of(x)



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


@execution_time.execution_time
def primes_ultil(value, gen):
    init = next(gen)
    while init <= value:
        print(init)
        init = next(gen)



# prime_factorization_of :: Int -> Int -> [Int] -> [Int]
@execution_time.execution_time
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

# primes = get_lazy_prime()
# print(prime_factorization_of(191543369, primes, []))

@execution_time.execution_time
def test_time(n):
    prime = get_lazy_prime()
    ls = []
    for i in range(1, n):
        ls.append(next(prime))
    return ls
