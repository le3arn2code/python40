# Lab 38: Parameter Passing & Unpacking

def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usage
if __name__ == "__main__":
    print("Sum:", add_numbers(1, 2, 3, 4, 5))  # 15
    
    show_info(name="Alice", age=30, city="New York")
    
    numbers = [1, 2, 3, 4]
    print("Sum with unpacked list:", add_numbers(*numbers))
    
    info = {'occupation': 'Engineer', 'country': 'USA'}
    show_info(**info)
