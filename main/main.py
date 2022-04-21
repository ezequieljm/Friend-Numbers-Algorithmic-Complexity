from sys import argv
from test_modules import test_of_module, prime_factorization

# The main function entry point
def main(*args, **kwargs):
    # if args[0] == 0:
    #     print("Sum of dividers by normal method")
    #     test_of_module.sum_dividers_by_range(args[1])
    # else:
    #     print("Sum of dividers by prime factor decomposition method")

    #     # Calculations with primes numbers are slower, since sigma1 of the prime number is always to one
    #     # primes = prime_factorization.prime_seive1(args[1])
    #     # prime_factorization.dividers_by_factorization_in_range(args[1],primes)

    #     # Calculations without primes numbers, this vertion is more fast
    #     # (primes, compose) = prime_factorization.prime_seive0(args[1])
    #     # prime_factorization.dividers_by_factorization_in_range(primes, compose)

    prime_factorization.friend_numbers(args[0])
    #(p,c) = prime_factorization.prime_seive0(args[0])
    #print(prime_factorization.dividers_by_factorization_in_range(p,c))


    

# Control of module
if __name__ == "__main__":
    main(int(argv[1]))