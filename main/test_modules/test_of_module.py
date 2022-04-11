from execution_time import execution_time

# Calculate the dividers of any number VERTION 0
# dividers_of :: Int -> [Int]
@execution_time.execution_time
def dividers_of(num):
    max_value = int(num / 2) + 1
    return [d for d in range(max_value, 2, -1) if num % d == 0]
    # return [d for d in range(2, num) if num % d == 0]

# Calculate the sum of the divisors of any number VERTION 0
# sum_dividers_of :: Int -> Int
# @execution_time.execution_time
def sum_dividers_of(num):
    half_of_value = int(num / 2) + 1
    result = 1
    for possible_div in range(half_of_value, 1, -1): 
        if num % possible_div == 0 : result += possible_div
    print(f"{num} : {result}")
    return result

# Calculate all dividers of numbers into a range
# dividers_by_range :: Int -> [[Int]]
@execution_time.execution_time
def sum_dividers_by_range(limit):
    return {str(x) : sum_dividers_of(x) for x in range(1, limit + 1)}