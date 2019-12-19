""" Problem 187: Semiprimes

A composite is a number containing at least two prime factors.
For example, 15 = 3 × 5; 9 = 3 × 3; 12 = 2 × 2 × 3.

There are ten composites below thirty containing precisely two,
not necessarily distinct, prime factors:
4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

How many composite integers, n < 10^8, have precisely two,
not necessarily distinct, prime factors?"""

import itertools
import time


def erat2():
    D = {}
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q * q] = q
            yield q
        else:
            x = p + q
            while x in D or not (x & 1):
                x += p
            D[x] = p


t = time.time()
max_num = 10 ** 8

primes = [0] * max_num
for i, j in enumerate(erat2()):
    primes[i] = j
    if j > max_num:
        print(i)
        break


p_facts = [0] * max_num
print("PROBLEM 187")
print("calculating...")
total_two_composites = 0

number = 2
while True:
    finished = False
    continueFlag = True
    orig_number = number
    prime_factors = 0
    index = 0
    # print(f"Zerlegung von {orig_number}")

    while continueFlag:
        if number % primes[index] != 0:
            index += 1

        else:
            number = int(number / primes[index])
            prime_factors += 1
            total_prime_factors = prime_factors + p_facts[number]
            if total_prime_factors > 2:
                continueFlag = False
                finished = False
            elif total_prime_factors == 2:
                continueFlag = False
                finished = True
                total_two_composites += 1
                # print(f"{orig_number} is a composite integer")
            elif number == 1:
                continueFlag = False
                finished = True

    p_facts[orig_number] = total_prime_factors

    number = orig_number + 1
    if number == max_num:
        break


print(
    f"There are {total_two_composites} composites containing precisely two prime factors."
)

elapsed = time.time() - t
print(f"{elapsed} seconds")
