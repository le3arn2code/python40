# Using a loop
squares_loop = []
for x in range(10):
    squares_loop.append(x**2)

# Using list comprehension
squares_comp = [x**2 for x in range(10)]

print("Squares with loop:", squares_loop)
print("Squares with comprehension:", squares_comp)
