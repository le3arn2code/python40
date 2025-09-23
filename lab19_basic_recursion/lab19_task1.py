def recursion_example(n):
    if n <= 0:  # Base case
        print("Base case reached")
    else:       # Recursive call
        print("Recursing with n =", n)
        recursion_example(n - 1)

recursion_example(3)
