#!/usr/bin/env python3

# Created by: Abdul Basit
# Created on: Nov 2021
# Grandmother age approval


def main():
    # function for grandmother age approval

    # input
    try:
        age = input("Please enter your age: ")
        age = int(age)

        # process/output
        if age > 40 or age < 25:
            print("You are NOT an acceptable age")
        else:
            print("You are an acceptable age")
    except ValueError:
        print("{} is not an integer".format(age))

    # done
    print("\nDone.")


if __name__ == "__main__":
    main()