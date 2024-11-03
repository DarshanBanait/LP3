# Define a class to represent items with value and weight
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight  # Value-to-weight ratio

# Function to solve the fractional knapsack problem
def fractional_knapsack(capacity, items):
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda item: item.ratio, reverse=True)
    
    total_value = 0  # Initialize total value in the knapsack
    
    for item in items:
        if capacity <= 0:  # If the knapsack is full, break
            break
        
        # If the item can be added in full
        if item.weight <= capacity:
            total_value += item.value  # Add full value of the item
            capacity -= item.weight  # Reduce the remaining capacity
        else:
            # If the item can't be added fully, take the fractional part
            total_value += item.ratio * capacity  
            capacity = 0  # The knapsack is now full
    
    return total_value

n = int(input("Enter the number of items: "))
items = []

for i in range(n):
    value = float(input(f"Enter value of item {i + 1}: "))
    weight = float(input(f"Enter weight of item {i + 1}: "))
    items.append(Item(value, weight))

capacity = float(input("Enter the capacity of the knapsack: "))

max_value = fractional_knapsack(capacity, items)

print(f"The maximum value that can be carried in the knapsack is: {max_value:.2f}")