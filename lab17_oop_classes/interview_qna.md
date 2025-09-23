# Interview Q&A - Lab 17: OOP Classes

### 1. What is a class in Python?
A class is a blueprint for creating objects, encapsulating data (attributes) and behavior (methods).

### 2. What is the difference between instance attributes and class attributes?
Instance attributes are unique to each object; class attributes are shared across all instances.

### 3. How do you define a class in Python?
Using the `class` keyword followed by the class name and methods inside it.

### 4. What is the purpose of the __init__ method?
It initializes the object’s attributes when a new instance is created.

### 5. What happens if you forget to include `self` in method definitions?
Python will raise an error because instance methods must explicitly reference the instance.

### 6. Can you override a class attribute in an instance?
Yes, assigning the same attribute name in an instance will shadow the class attribute.

### 7. What is encapsulation in OOP?
Encapsulation is the bundling of data and methods that operate on that data into a single unit (class).

### 8. How do you create an object in Python?
By calling the class as a function, e.g., `car = Car("Toyota", "Corolla")`.

### 9. What is the difference between `Car.wheels` and `car.wheels`?
`Car.wheels` refers to the class attribute, while `car.wheels` accesses it via an instance.

### 10. How do you check if an attribute belongs to a class or an instance?
Using `__dict__` property: instance attributes appear in `obj.__dict__`, class attributes in `ClassName.__dict__`.
