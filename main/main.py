from sys import argv
from test_modules import test_of_module

# The main function entry point
def main(*args, **kwargs):
    #print(f"""Dividers of {args[0]} are:\n{test_of_module.dividers_of(args[0])}""")
    print(f"""Sum of the divisors of {args[0]} = {test_of_module.sum_dividers_of(args[0])}""")

# Control of module
if __name__ == "__main__":
    main(int(argv[1]))