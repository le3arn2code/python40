def tail_recursive_factorial(n, accumulator=1):
    if n <= 1:
        return accumulator
    else:
        return tail_recursive_factorial(n - 1, n * accumulator)

def iterative_factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

tail_result = tail_recursive_factorial(5)
iter_result = iterative_factorial(5)

print("Factorial of 5 using tail recursion:", tail_result)
print("Factorial of 5 using iteration:", iter_result)
