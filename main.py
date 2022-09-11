import functions


def main():
    """Draw lotto numbers based on user input."""
    active = True

    while active:
        functions.lotto()
        active = functions.draw_again()


if __name__ == '__main__':
    main()
