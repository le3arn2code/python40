# Task 3 & 4: Create, start, and join threads

from lab28_task1_2 import print_numbers
import threading

# Create threads
thread1 = threading.Thread(target=print_numbers, args=("Thread-1", 0, 5))
thread2 = threading.Thread(target=print_numbers, args=("Thread-2", 5, 10))

# Start threads
thread1.start()
thread2.start()

# Wait for threads to finish
thread1.join()
thread2.join()

print("Both threads have completed.")
