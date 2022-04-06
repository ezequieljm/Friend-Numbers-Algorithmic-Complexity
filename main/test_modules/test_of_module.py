from execution_time import execution_time

# Calculate the dividers of any number
# dividers_of :: Int -> [Int]
@execution_time.execution_time
def dividers_of(num):
    max_value = int(num / 2) + 1
    return [d for d in range(max_value, 1, -1) if num % d == 0]

# Calculate the sum of the divisors of any number
# sum_dividers_of :: Int -> Int
@execution_time.execution_time
def sum_dividers_of(num):
    half_of_value = int(num / 2) + 1
    result = 1
    for possible_div in range(half_of_value, 1, -1): 
        if num % possible_div == 0 : result += possible_div
    return result





