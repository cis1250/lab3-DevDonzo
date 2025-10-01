#!/usr/bin/env python3

# Fibonacci Sequence Exercise

while True:
    user_input = input("How many terms of the Fibonacci sequence do you want? ")

    # Validate input
    if not user_input.isdigit() or int(user_input) <= 0:
        print("Please enter a positive integer.")
        continue

    num_terms = int(user_input)
    break

# Generate Fibonacci sequence
a, b = 0, 1
for i in range(num_terms):
    print(a, end=" ")
    a, b = b, a + b
print()
