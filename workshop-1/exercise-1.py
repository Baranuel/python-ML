
#Write a Python function that takes a list of numbers as input
#and outputs the maximum, minimum and median values in the list.

numbers_list = [1, 2, 3, 4, 5]

def get_min_max(list: list[int]) -> tuple[int, int]:
    min, max = list[0], list[0]
    
    for i in list:
        if i < min: min = i
        if i > max: max = i

    return min, max
    

def get_median(list: list[int]) -> float:
    sorted_list = sorted(list)
    n = len(sorted_list)
    if n % 2 == 1:
        return sorted_list[n // 2]
    else:
        return (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2


def print_list(list:list[int]) -> None:
    min, max = get_min_max(list)
    median = get_median(list)
    print(f"Min: {min}, Max: {max}, Median: {median}")


def main():
    print_list(numbers_list)

if __name__ == "__main__":
    main()