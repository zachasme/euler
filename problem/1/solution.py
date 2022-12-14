import sys

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

threes = set(range(3, int(sys.argv[1]), 3))
fives = set(range(5, int(sys.argv[1]), 5))

print(sum(threes | fives))  # 233168
