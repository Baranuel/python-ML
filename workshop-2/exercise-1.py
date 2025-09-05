# Write a Python function that takes two string arguments, x and y,
# and returns the index of the first occurrence of x in y, or -1 if x does not occur in y

def find_first_occurrence(x:str, y:str) -> int:
    return y.find(x)

def main():
    print(find_first_occurrence("long string", "This is a long string."))


if __name__ == "__main__":
    main()
