def knapsack(max_capacity, weights, values, n):
    # Create a 2D array to store the maximum value at each n and max_capacity
    K = [[0 for x in range(max_capacity + 1)] for x in range(n + 1)]

    # Build the table K[][] in bottom-up manner
    for i in range(n + 1):
        for w in range(max_capacity + 1):
            if i == 0 or w == 0:
                # Base case: If there are no items or capacity is 0, max value is 0
                K[i][w] = 0
            elif weights[i-1] <= w:
                # If the weight of the current item is less than or equal to the current capacity
                # Take the maximum of including the item or not including the item
                K[i][w] = max(values[i-1] + K[i-1][w-weights[i-1]], K[i-1][w])
            else:
                # If the weight of the current item is more than the current capacity
                # Do not include the item
                K[i][w] = K[i-1][w]

    # The last cell of the table contains the maximum value that can be obtained
    return K[n][max_capacity]

n = int(input("Enter the number of items: "))
weights = []
values = []

for i in range(n):
    weight = int(input(f"Enter weight of item {i+1}: "))
    value = int(input(f"Enter value of item {i+1}: "))
    weights.append(weight)
    values.append(value)

max_capacity = int(input("Enter the maximum capacity of the knapsack: "))

max_value = knapsack(max_capacity, weights, values, n)
print(f"The maximum value that can be obtained is: {max_value}")

# Time Complexity: (O(n * C)) Where (n) is the number of items and (W) is the maximum capacity of the knapsack.

# formula => v[i][w] = max(v[i-1][w], v[i-1][w-wt[i]] + profit[i]) if w >= wt[i] , i is row, w is column