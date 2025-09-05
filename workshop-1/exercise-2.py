#Write a Python function that takes a string as its only argument and prints out the 
#frequency with which each letter occurs in the string.
#  The function should only print out the frequency of occurrence
# for letters that actually occur in the input string

string_to_test_against = "this is a long-ass string"

def letter_frequency(input: str) -> None:
    frequencies:dict[str,int] = {}
    input_text = input.strip().lower().replace(' ','')

    for i in input_text:
        if i in frequencies:
            frequencies[i] += 1
        else:
            frequencies[i] = 1

    for letter, count in frequencies.items():
        print(f"{letter}: {count}")


def main():
    letter_frequency(string_to_test_against)

if __name__ == "__main__":
    main()