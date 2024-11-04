from queue import PriorityQueue
class Node:
    def __init__(self, level, profit, weight, bound):
        self.level = level     # Level of the node (index of the item being considered)
        self.profit = profit   # Total profit for the current node
        self.weight = weight   # Total weight for the current node
        self.bound = bound     # Upper bound of the maximum profit reachable from this node

    # Comparison function for PriorityQueue to sort nodes by bound (higher bound first)
    def __lt__(self, other):
        return self.bound > other.bound  # For max-heap behavior in PriorityQueue

# Function to calculate the upper bound of profit for a given node
def bound(node, n, max_capacity, weights, values):
    # If weight exceeds capacity, return 0 as bound (infeasible node)
    if node.weight >= max_capacity:
        return 0

    profit_bound = node.profit  # Start with the profit of the current node
    j = node.level + 1          # Start from the next item
    total_weight = node.weight  # Start with the current node's weight

    # Add items to the knapsack while the total weight is within capacity
    while j < n and total_weight + weights[j] <= max_capacity:
        total_weight += weights[j]
        profit_bound += values[j]
        j += 1

    # If there's still capacity left, add fractional part of the next item's profit
    if j < n:
        profit_bound += (max_capacity - total_weight) * values[j] / weights[j]

    return profit_bound

def knapsack(max_capacity, weights, values, n):
    pq = PriorityQueue()
    # Root node (starting with no items)
    u = Node(-1, 0, 0, 0) 
    v = Node(-1, 0, 0, 0)  # Child node placeholder
    max_profit = 0         # Variable to store maximum profit found

    # Initialize the bound for the root node and add it to the queue
    u.bound = bound(u, n, max_capacity, weights, values)
    pq.put(u)

    # Process nodes in the queue until empty
    while not pq.empty():
        # Dequeue the node with the highest bound
        u = pq.get()

        # If this node's bound is greater than the max profit found so far, explore it
        if u.bound > max_profit:
            # Explore the node that includes the next item
            v.level = u.level + 1
            v.weight = u.weight + weights[v.level]
            v.profit = u.profit + values[v.level]

            # Update max profit if the new node's profit is higher
            if v.weight <= max_capacity and v.profit > max_profit:
                max_profit = v.profit

            # Calculate bound for the node including the next item
            v.bound = bound(v, n, max_capacity, weights, values)

            # If bound is promising, add the node to the queue
            if v.bound > max_profit:
                pq.put(Node(v.level, v.profit, v.weight, v.bound))

            # Explore the node that excludes the next item
            v.weight = u.weight
            v.profit = u.profit
            v.bound = bound(v, n, max_capacity, weights, values)

            # If bound is promising, add this node to the queue
            if v.bound > max_profit:
                pq.put(Node(v.level, v.profit, v.weight, v.bound))

    return max_profit

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
