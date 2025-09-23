import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Log messages at different levels
logging.debug("This is a debug message.")
logging.info("This is an info message.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")
logging.critical("This is a critical message.")

# Practical application function
def divide_numbers(a, b):
    try:
        result = a / b
        logging.info("Division successful.")
        return result
    except ZeroDivisionError:
        logging.error("Division by zero error.")
        return None

print("Result of 10 / 2:", divide_numbers(10, 2))
print("Result of 10 / 0:", divide_numbers(10, 0))
