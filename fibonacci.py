#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.
while True:
    user_input = input("How many terms of Fibonacci sequence do you want? ")

    if user_input.isdigit():
        n = int(user_input)
        if n > 0:
            break   # valid input, exit loop
        else:
            print("Please enter a positive integer.")
    else:
        print("Please enter a positive integer.")

a = 0
b = 1

print("Fibonacci Sequence:")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b   # update inside the loop
