#!/usr/bin/env python3
# Created By: Jack Turcotte
# Date: April 15, 2025

# Power of two program in python


def main():

    # Get user input
    user_number = input("Enter a whole number bigger than or equal to zero: ")

    # Try catch to prevent logic error (str --> int)
    try:
        user_number = int(user_number)

        # Check if user number is less than 0
        if user_number < 0:
            print("User number must be an integer greater than or equal to zero.")
            main()
        else:

            # Loop through numbers 0 to user number
            for i in range(user_number + 1):
                print(i, "^2 = ", i**2)
                if i >= 100:
                    break
        print("Thanks for playing!")
    except:
        print("User number must be an integer greater than or equal to zero.")
        main()
    finally:
        # Tell user what they entered
        print("You entered", user_number)


if __name__ == "__main__":
    main()
