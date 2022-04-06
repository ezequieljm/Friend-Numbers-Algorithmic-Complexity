from execution_time import execution_time

# Calculate the dividers of any number
# dividers_of :: Int -> [Int]
@execution_time.execution_time
def dividers_of(num):
    divs = []
    max = int(num / 2) + 1
    for possible_div in range(max, 1, -1):
        if num % possible_div == 0:
            divs.append(possible_div)
    divs.append(1)
    print(sum(divs))
    return divs

