import execution_time

# sieve :: Int -> [Int]
def sieve(n):
    is_prime = [True for _ in range(n + 1)]
    is_prime[0], is_prime[1] = False, False

    for i in range(2, int(n ** 0.5)): 
        if (is_prime[i]):
            for j in range(i * i, n + 1, i): 
                is_prime[j] = False

    return [x for x in range(2, n + 1) if is_prime[x]]

# divisors :: Int -> [Int] -> [[Int]] -> ()
def dividers_of(num, primes, dividers):
    if dividers[num] == None:
        i = 0
        while num % primes[i] != 0: i += 1

        prime = primes[i]
        original = num // prime
        haux = dividers[original].copy()
        haux.append(original)
        length = len(haux) - 2

        div = haux[length] * prime
        while div != original and length > -1: 
            haux.append(div)
            length -= 1
            div = haux[length] * prime

        dividers[num] = haux

# amigos :: Int -> [(Int,Int)]
@execution_time.execution_time
def friends(limit):
    primes = sieve(limit)
    dividers = [None] * limit
    dividers[0] = []; dividers[1] = []; friends = []

    for x in primes: dividers[x] = [1]
    for n in range(2, limit):
        dividers_of(n, primes, dividers)
        sm1 = sum(dividers[n])
        if sm1 < n:
            if sum(dividers[sm1]) == n:
                friends.append((n,sm1))
    return friends

# The main function entry point
# main :: IO ()
def main():
    # input_us = input(f"Enter a value: ")
    # friends(int(input_us))
    print(sieve(1000))

# Control of module
if __name__ == "__main__":
    main()