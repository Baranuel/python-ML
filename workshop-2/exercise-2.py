# Write a function that takes two arguments, a list, l, and a function, f,
# and returns a list containing the results of applying f to each element in l.
# Test your function by defining an argument function, f, that returns the square of an input number.

def execute_func(l:list, f:function) -> list:
    result = [];
    for i in l:
        result.append(f(i))
    return result


def square(x:int) -> int:
    return x * x

def main():
    print(execute_func([1,2,3,4,5], square))

if __name__ == "__main__":
    main()