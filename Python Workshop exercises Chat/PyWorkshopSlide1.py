# -----------------------------
# Exercise 2: Max, Min, Median
# -----------------------------
def stats(numbers):
    numbers = sorted(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    n = len(numbers)

    if n % 2 == 1:
        median = numbers[n // 2]
    else:
        median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2

    return maximum, minimum, median


# -----------------------------
# Exercise 3: Letter Frequencies
# -----------------------------
def letter_frequency(s):
    s = s.lower()
    freq = {}
    for char in s:
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1

    for letter, count in freq.items():
        print(f"{letter}: {count}")


# -----------------------------
# Exercise 4: Reverse & Palindrome Check
# -----------------------------
def reverse_and_check(seq):
    reversed_seq = seq[::-1]
    if seq == reversed_seq:
        print("This sequence is a palindrome!")
    return reversed_seq


# -----------------------------
# Example runs (you can change these)
# -----------------------------
if __name__ == "__main__":
    print("Exercise 2 Example:", stats([5, 1, 9, 3, 7]))
    print("\nExercise 3 Example:")
    letter_frequency("Hello World")
    print("\nExercise 4 Example:")
    print(reverse_and_check("racecar"))
    print(reverse_and_check([1, 2, 3, 2, 1]))
    print(reverse_and_check("hello"))
