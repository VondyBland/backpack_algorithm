from itertools import combinations

class BackpackOptimizer:
    def __init__(self, weights, prices, limit):
        self.weights = weights
        self.prices = prices
        self.limit = limit

    def find_combinations(self):
        result = []
        for r in range(1, len(self.weights) + 1):
            for combo in combinations(self.weights, r):
                if sum(combo) == self.limit:
                    result.append(combo)
        return result

    def max_backpack_min_backpain(self):
        combinations = self.find_combinations()
        print(f'Найденные комбинации: {combinations}')

        indices_list = []
        for combo in combinations:
            indices = []
            for value in combo:
                if value in self.weights:
                    indices.append(self.weights.index(value))
                else:
                    indices.append(None)
            indices_list.append(indices)

        max_values = []
        for indices in indices_list:
            sum_values = sum([self.prices[idx] for idx in indices if idx < len(self.prices)])
            max_values.append(sum_values)

        max_val = max(max_values)
        result = [max_val]

        if max_values.count(max_val) > 1:
            result.extend([val for val in max_values if val == max_val][1:])

        print("Максимальные значения:")
        return result


