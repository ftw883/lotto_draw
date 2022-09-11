import random


def draw_again(again=""):
    """Ask user if they would like to draw again."""
    valid_response = ["y", "yes", "n", "no"]

    while again.lower() not in valid_response:
        again = input("\nWould you like to do another draw?\t")
        if again.lower() not in valid_response:
            print("Invalid entry!")

    return again.lower() == "y" or again.lower() == "yes"


def lotto():
    """Gather user input for lotto draw and create list of lotto numbers."""
    lotto_nums = []  # List to hold lotto_nums numbers

    # Collect user input for amount of numbers and highest number.
    nums = int(input("\nHow many numbers would you like to draw?\t"))
    max_num = int(input("What is the highest valid number to draw?\t"))

    # Draw numbers until all required numbers are drawn.
    while len(lotto_nums) < nums:
        lotto_nums = draw(max_num, lotto_nums)

    print(f"\nLotto numbers are: {lotto_nums}")


def draw(max_num, lotto_nums):
    """Draw random number, append it to list of numbers if unique,
    and return updated list of lotto numbers."""

    # Draw number.
    num = random.randint(1, max_num)

    # Only append number drawn to list if it is unique.
    if num not in lotto_nums:
        lotto_nums.append(num)

    return sorted(lotto_nums)
