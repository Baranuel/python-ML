# -----------------------------
# Exercise 1: First occurrence of x in y
# -----------------------------
def find_substring(x, y):
    for i in range(len(y) - len(x) + 1):
        if y[i:i+len(x)] == x:
            return i
    return -1


# -----------------------------
# Exercise 2: Apply a function to each element
# -----------------------------
def apply_function(l, f):
    return [f(item) for item in l]

# Example function to use
def square(n):
    return n * n


# -----------------------------
# Exercise 3: Sum and Mean
# -----------------------------
def sum_and_mean(*numbers):
    total = sum(numbers)
    mean = total / len(numbers) if numbers else 0
    return total, mean


# -----------------------------
# Example runs
# -----------------------------
if __name__ == "__main__":
    print("Exercise 1 Examples:")
    print(find_substring("cat", "concatenate"))  # 3
    print(find_substring("dog", "concatenate"))  # -1

    print("\nExercise 2 Examples:")
    print(apply_function([1, 2, 3, 4], square))  # [1, 4, 9, 16]

    print("\nExercise 3 Examples:")
    print(sum_and_mean(1, 2, 3, 4, 5))  # (15, 3.0)
    print(sum_and_mean())  # (0, 0)
