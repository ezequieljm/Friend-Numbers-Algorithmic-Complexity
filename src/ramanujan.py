import execution_time


# factor_everything_until :: Int -> [(Bool, Int)]
def factor_everything_until(n):
    sigma1_list = [(True, 1)] * (n + 1)
    for p in range(2, n + 1): 
        (is_prime,_) = sigma1_list[p]
        if is_prime:
            for j in range(p + p, n + 1, p): 
                exp = 1
                dividend = j
                while dividend % p == 0:
                    dividend = dividend // p
                    exp += 1
                tot = 0
                for exp in range(0, exp): tot += (p ** exp)
                (_, partial_sigma1) = sigma1_list[j]
                partial_sigma1 *= tot
                sigma1_list[j] = (False, partial_sigma1)
    return sigma1_list


#ramanujan :: Int -> [(Int, Int)]
@execution_time.execution_time
def ramanujan(limit):
    friends = []
    facts = factor_everything_until(limit)
    for a in range(0, limit + 1):
        (is_prime, sigma1a) = facts[a]
        if not is_prime:
            if (sigma1a - a) > limit: continue
            b = sigma1a - a
            if b < a:
                (_,sigma1b) = facts[b]
                if (sigma1b - b) == a: friends.append((a,b))
    return friends


# main :: IO ()
def main():
    value = input("Enter a value: ")
    print(ramanujan(int(value)))


# Control of module
if __name__ == "__main__":
    main()