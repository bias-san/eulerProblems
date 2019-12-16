""" Problem 3: Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


num = 600851475143
i = 2

while True:
    if num % i == 0:
        num = num / i
        print(i)
        if num == 1:
            break
    i += 1
