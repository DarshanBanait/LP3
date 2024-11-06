n = int(input("Enter the number: "))


# Iterative Approach with TC=O(n), SC=O(1)
def fibonacci_iterative(n):
    iterative_steps = 0
    if n == 1:
        return 0, iterative_steps
    elif n == 2:
        return 1, iterative_steps
    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
        iterative_steps += 1
    return b, iterative_steps


fib_number, iterative_steps = fibonacci_iterative(n)
print(
    f"Iterative: The {n}th Fibonacci number is: {fib_number} (calculated in {iterative_steps} steps)"
)


# Recursive Approach with TC=O(2^n), SC=O(n) with corrected steps
def fibonacci_recursive(n, recursive_steps):
    recursive_steps[0] += 1  # Increment shared step counter for each call
    if n == 1:
        recursive_steps[0] += 1
        return 0
    elif n == 2:
        recursive_steps[0] += 1
        return 1
    else:
        return fibonacci_recursive(n - 1, recursive_steps) + fibonacci_recursive(
            n - 2, recursive_steps
        )


# Initialize a mutable list to act as a shared counter for recursion
recursive_steps = [0]
fib_number = fibonacci_recursive(n, recursive_steps)
print(
    f"Recursive: The {n}th Fibonacci number is: {fib_number} (calculated in {recursive_steps[0]+1} steps)"
)


# Top-Down Dynamic Programming (Memoization) with TC=O(n), SC=O(n)
def fibonacci_memoization(n, memo={}, memoization_steps=[0]):
    if n in memo:
        return memo[n], memoization_steps[0]
    memoization_steps[
        0
    ] += 1  # Increment step counter when calculating a new Fibonacci value
    if n == 1:
        return 0, memoization_steps[0]
    elif n == 2:
        return 1, memoization_steps[0]
    fib1, _ = fibonacci_memoization(n - 1, memo, memoization_steps)
    fib2, _ = fibonacci_memoization(n - 2, memo, memoization_steps)
    memo[n] = fib1 + fib2
    return memo[n], memoization_steps[0]


# Reset steps counter for memoization approach
memoization_steps = [0]
fib_number, memoization_steps = fibonacci_memoization(n)
print(
    f"Memoization: The {n}th Fibonacci number is: {fib_number} (calculated in {memoization_steps} steps)"
)

# To improve on the recursive approach, we can use memoization, which stores results of previous calculations to avoid redundant work. This reduces the time complexity
