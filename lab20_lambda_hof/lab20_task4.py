from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use reduce with a lambda function to sum the numbers
total_sum = reduce(lambda x, y: x + y, numbers)

print("Sum of Numbers:", total_sum)
