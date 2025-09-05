#Write a function that takes any number of numbers as its arguments
# and returns the sum and mean of the numbers as a pair, (sum,mean).

def sum_and_mean(*args):
    total = sum(args)
    mean = total / len(args) if args else 0
    return total, mean

def main():
    print(sum_and_mean(1, 2, 3, 4, 5))

if __name__ == "__main__":
    main()