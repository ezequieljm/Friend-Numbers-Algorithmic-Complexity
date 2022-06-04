
# sieve :: Int -> [Int]
def sieve(n):
    is_prime = [True for _ in range(n + 1)]
    is_prime[0], is_prime[1] = False, False

    for i in range(2, int(n ** 0.5)): 
        if (is_prime[i]):
            for j in range(i * i, n + 1, i): 
                is_prime[j] = False

    return [x for x in range(2, n + 1) if is_prime[x]]


#sieve2 :: Int -> [Int]
sieve2 = (lambda prime, xs, inx, n: 
    [prime] + [x for x in xs if x % prime > 0] if inx > int(n ** 0.5) 
    else [prime] + sieve2(xs[inx + 1], [x for x in xs if x % prime > 0], inx + 1, n)
)

list1 = sorted(sieve2(2,[x for x in range(2, 22)], 0, 20))
list2 = sieve(20)
print(list1)
print(list2)

# list_difference = []

# for item in list1:
#   if item not in list2:
#     list_difference.append(item)

# print(list_difference)

# for item in list_difference:
#     for i in list1:
#         if item == i: print(f"{item} {i}")

# print([x for x in range(0,1001) if x % 5 == 0])
