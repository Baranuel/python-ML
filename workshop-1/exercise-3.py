#Write a Python function that takes any sequence as its argument
#  and returns the reverse of the sequence.
#  Get the function to notify the user when the input sequence is a palindrome.

import sys
sequence = sys.argv[1] if len(sys.argv) > 1 else "racecar"

def reverse_sequence(seq: str) -> str:
    reversed_seq = seq[::-1]
    if seq == reversed_seq:
        print(f"The input sequence is a palindrome: {sequence}")
    else:
        print(f"The input sequence is not a palindrome: {sequence}")
    return reversed_seq



def main():
    reverse_sequence(sequence)

if __name__ == "__main__":
    main()