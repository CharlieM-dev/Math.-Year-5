# Some natural number greater than 3 is denoted as 𝑎. Write the two previous and two next natural numbers for a

import random
import sys
a = random.randint(4, sys.maxsize)
previous_numbers = [a - 2, a - 1]
next_numbers = [a + 1, a + 2]
print(f'Your number is: {a}')
print(f'Previous numbers: {previous_numbers}')
print(f"Next numbers: {next_numbers}")
