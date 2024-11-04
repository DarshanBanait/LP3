class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight

def fractional_knapsack(capacity, items):

    items.sort(key=lambda item: item.ratio, reverse=True)
    
    total_value = 0
    
    for item in items:
        if capacity <= 0:
            break

        if item.weight <= capacity:
            total_value += item.value
            capacity -= item.weight
        else:
            total_value += item.ratio * capacity  
            capacity = 0  
    
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