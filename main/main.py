from sys import argv
from test_modules import test_of_module

# The main function entry point
def main(*args, **kwargs):
    test_of_module.divs_range(100000)
    #primes = test_of_module.get_lazy_prime()
    #test_of_module.primes_ultil(100000, primes)





# Control of module
if __name__ == "__main__":
    main()