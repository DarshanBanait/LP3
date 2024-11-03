# Iterative Approach with TC=O(n), SC=O(1)
def fibonacci_iterative(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b

n = 10
print(f"The {n}th Fibonacci number is:", fibonacci_iterative(n))

# Recursive Approach with TC=O(2^n), SC=O(n)
def fibonacci_recursive(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

n = 10
print(f"The {n}th Fibonacci number is:", fibonacci_recursive(n))

# Top-Down Dynamic Programming (Memoization) with TC=O(n), SC=O(n)
def fibonacci_memoization(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 1:
        return 0
    elif n == 2:
        return 1
    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]

n = 10
print(f"The {n}th Fibonacci number is:", fibonacci_memoization(n))

#To improve on the recursive approach, we can use memoization, which stores results of previous calculations to avoid redundant work. This reduces the time complexity