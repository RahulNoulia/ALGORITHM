
"""
Problem 6

Sum square difference

The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""


sum_of_sq = 0
sq_of_sum = 0
for i in range(1, 101):
    sum_of_sq += pow(i, 2)
    sq_of_sum += i
print(pow(sq_of_sum, 2) - sum_of_sq)


# Answer : 25164150