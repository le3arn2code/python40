# Interview Q&A - Lab 19: Basic Recursion Example

### 1. What is recursion?
Recursion is when a function calls itself to solve smaller instances of the same problem.

### 2. What are the two main parts of recursion?
A base case (stopping condition) and a recursive call.

### 3. What is factorial and how is it defined?
Factorial of n is n * (n-1) * (n-2) … * 1, with 0! = 1.

### 4. How is factorial implemented recursively in Python?
By defining a base case for n <= 1, and otherwise returning n * factorial(n-1).

### 5. What is the difference between recursion and iteration?
Recursion uses function calls, while iteration uses loops. Recursion can be more elegant; iteration is often more efficient.

### 6. What is tail recursion?
Tail recursion is when the recursive call is the last statement executed in the function.

### 7. Why is recursion not always efficient?
Each recursive call uses stack memory, and deep recursion can lead to stack overflow.

### 8. How can you avoid stack overflow in Python recursion?
Use iteration or optimize recursion (e.g., tail recursion, memoization).

### 9. What error occurs if recursion goes too deep in Python?
`RecursionError: maximum recursion depth exceeded`.

### 10. When should you prefer recursion over iteration?
When problems are naturally recursive (e.g., tree traversal, divide-and-conquer algorithms). Iteration should be used for very large repetitive tasks.
