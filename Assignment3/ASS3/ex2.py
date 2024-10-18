def generate_combinations(chars, n, current_combination="", results=None):
    if results is None:
        results = []

    if n == 0:
        results.append(current_combination)
        return results

    for char in chars:
        generate_combinations(chars, n - 1, current_combination + char, results)

    return results

def print_combinations(chars, n):
    combinations = generate_combinations(chars, n)
    for i in range(0, len(combinations), len(chars)):
        print(" ".join(combinations[i:i + len(chars)]))

# Example usage:
characters = ["a", "b", "c"]
n = 2
print_combinations(characters, n)
