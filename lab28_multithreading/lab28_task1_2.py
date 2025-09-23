# Task 1 & 2: Import threading and define function

import threading

def print_numbers(thread_name, start, end):
    """Prints numbers from start to end."""
    for number in range(start, end):
        print(f"{thread_name}: {number}")
