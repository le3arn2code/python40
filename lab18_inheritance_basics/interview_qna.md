# Interview Q&A - Lab 18: OOP Inheritance Basics

### 1. What is inheritance in Python?
Inheritance allows a class (subclass) to derive attributes and methods from another class (parent).

### 2. Why do we use inheritance?
It promotes code reuse, avoids duplication, and supports modular design.

### 3. What is the role of the super() function?
`super()` allows access to parent class methods and constructors inside a subclass.

### 4. How do you override a method in Python?
Define the method with the same name in the subclass; it replaces the parent’s version.

### 5. What is the difference between parent and child class?
The parent class defines general attributes and methods, while the child extends or customizes them.

### 6. Can a subclass have additional attributes?
Yes, subclasses can introduce new attributes not defined in the parent class.

### 7. What happens if you don’t call super() in the subclass constructor?
The parent’s constructor won’t run automatically, and parent attributes may not initialize.

### 8. Can you override __init__ in a subclass?
Yes, you can override it and call `super().__init__()` to reuse parent initialization logic.

### 9. How do you check class inheritance in Python?
Using `issubclass(SubClass, ParentClass)` or `isinstance(object, Class)`.

### 10. Give a real-world example of inheritance.
A `Car` as a base class and `ElectricCar` as a subclass with battery-specific attributes.
