#!/usr/bin/env python3

def print_fibonacci(length):
 """
    Prints the Fibonacci sequence up to the specified length.
    
    Args:
        length (int): The number of Fibonacci numbers to print.
    """
 if length <= 0:
        print("[]")
        return
    
fibonacci = [0, 1]
print(fibonacci[0])
print(fibonacci[1])
    
for i in range(2, length):
        next_number = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_number)
    
