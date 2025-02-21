#!/usr/bin/env python3

def print_fibonacci(n):
    """Prints the Fibonacci sequence up to the given length n."""
    if n <= 0:
        print([])  # Edge case: If n is 0 or negative, return an empty list.
        return
    
    # Start with the base cases
    fib_sequence = [0, 1]

    # Generate the sequence up to the desired length
    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    # If n is 1, return only the first element
    print(fib_sequence[:n])