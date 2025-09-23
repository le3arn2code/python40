def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def iterative_factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

rec_result = factorial(5)
iter_result = iterative_factorial(5)

print("Recursive factorial of 5:", rec_result)
print("Iterative factorial of 5:", iter_result)
