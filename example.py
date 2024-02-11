import sys

from backpack_algorithm import BackpackOptimizer

# Example:
weights = [2, 6, 1, 5]
prices = [3, 10, 5, 6]
limit = 7

optimizer = BackpackOptimizer(weights, prices, limit)
result = optimizer.max_backpack_min_backpain()
print(result)