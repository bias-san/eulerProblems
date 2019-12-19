""" Problem 187: Semiprimes

A composite is a number containing at least two prime factors.
For example, 15 = 3 × 5; 9 = 3 × 3; 12 = 2 × 2 × 3.

There are ten composites below thirty containing precisely two,
not necessarily distinct, prime factors:
4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

How many composite integers, n < 10^8, have precisely two,
not necessarily distinct, prime factors?"""

import time

arr = [0] * 1000

t = time.time()
max_num = 100000
print("PROBLEM 187")
print("calculating...")
total_two_composites = 0
set_of_tested_nums = set()

number = 2
while True:
    finished = False
    continueFlag = True
    orig_number = number
    prime_factors = 0
    divisor = 2
    # print(f"Zerlegung von {orig_number}")
    while continueFlag:
        if number % divisor != 0:
            if divisor == 2:
                divisor += 1
            else:
                divisor += 2
        else:
            number = int(number / divisor)
            prime_factors += 1
            if (prime_factors == 2 and number != 1) or (
                number in set_of_tested_nums
            ):
                continueFlag = False
                finished = False

            if number == 1:
                finished = True
                continueFlag = False

    if finished and prime_factors == 2:
        # print(f"{orig_number} is a composite integer")
        total_two_composites += 1
    if prime_factors > 1:
        set_of_tested_nums.add(orig_number)
    number = orig_number + 1
    if number == max_num:
        break


print(
    f"There are {total_two_composites} composites containing precisely two prime factors."
)

elapsed = time.time() - t
print(f"{elapsed} seconds")
