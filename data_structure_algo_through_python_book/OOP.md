## All About Python Object-Oriented Programming

- [Class & Object](#class--object).
- [Constructor](#constructor).
- [Types Of Variables](#python-variables-types-local--global).
- [Types Of Methods](#type-of-methods).
- [Types of Inheritance](#type-of-inheritance).
- [Polymorphism](#polymorphism).
- [Abstraction](#abstract).

### Class & Object
- A `class` is blueprint of objects.
- `Object` is real world entities.
- `Object-Oriented Programming`  mainly helps us to create reusable code & reduce redundancy.

```python
class Parrot:
    pass

obj = Parrot()
```
In above example, an `object` is instance of a `class`.
`class` is just definition of `object` no memory or storage is allocated.
In above code `obj` is object of `Parrot`, when initiate `Parrot()` only that time allocated memory by `obj`.

### Class & Instance/Object attribute:

```python
class Vehicle:
    # class attribute
    vehicle_count = 0

    # instance attribute
    def __init__(self, name, model):
        self.name = name
        self.model = model
        Vehicle.vehicle_count += 1


car1 = Vehicle('BMW', "BPX11")
car2 = Vehicle('Lamborghini', "MJL44")

# Access class attributes
print(f"BMW is a {car1.__class__.vehicle_count}")
print(f"Lamborghini is a {car2.__class__.vehicle_count}")

# Access instance attribute
print(f"Car name is {car1.name} & model is {car1.model}")
print(f"Car name is {car2.name} & model is {car2.model}")
```
```
BMW is a 2
Lamborghini is a 2
Car name is BMW & model is BPX11
Car name is Lamborghini & model is MJL44
```
In above code snippet defined a class `Vehicle` & some attributes which are characteristics of an object.
We defined class level object & instance level object differently such as `vehicle_count`, `self.name` & `self.model`.
`vehicle_count` is class level attribute & inside `__init__` we defined instance level attributes.(Conventionally `self`
is instance of object, explain it further section).

When initialize an object, automatically `__init__` method call first. This called contructor, in below I about that.
We can access class attributes through `__class__`(special attribute) because all class level attributes are same for
all instances. Let me explain above code, we created two instance `car1` & `car2`, when we 
initialize two instances the `vehicle_count` incremented two times so result is 2, because we have already known when
we initialize any object, firstly loaded `__init__` part. So all instance will have same result. But in case of instance
attribute different for every instance.

### Constructor
A `constructor` is a method that is called when object is created. This method called inside class and can initialize
basic variables. 
In above, we created two objects, so constructor call twice. Every class has constructor but no need to explicit 
declaration.
In above code `__init__` is a constructor & `self` keyword indicates instance itself. 
How works or load constructor:<br>
**Start** ->  **Created Obj** -> **Call Class Object** -> **Return**

```python
    # instance attribute
    def __init__(self, name, model):
        self.name = name
        self.model = model
```
In the provided code snippet, we have a constructor method `__init__` within a class. The `__init__` method is a special 
method in Python classes, often referred to as the `constructor`. It is automatically called when an object of the class 
is created. The purpose of the constructor is to initialize the attributes of the object.
Here, the constructor takes two parameters `name` and `model`, and it initializes two instance attributes, 
`self.name` and `self.model`. These instance attributes store specific values for each instance of the class. 
For example, if we create an object like `my_car = Car("Toyota", "Camry")`, the name attribute of my_car will be set to
`Toyota` and the model attribute will be set to `Camry`.

### Python variables Types: Local & Global
There are two types of variable in python, one is Local & another is Global variables. The key difference between them 
use case. `Global Variable` declared outside the function and can be access & modify within any part of code & 
`Local variable` is declared inside function or class, can't be access or modify from outside of that function.
```python
# Global variable
variable = 233

def local_var_func():
    # local variable
    variable = 566
    print(f"Local variable: {variable}") #Local variable: 566

local_var_func()
print(f"Global variable: {variable}") #Global variable: 233
```
```
Local variable: 566
Global variable: 233
```
In above, first declared `variable = 233` is a global variable & inside function `variable = 566` is local variable .

### Type of methods

- Instance Method
- Class Method
- Static Method

Before explain above concepts, we need to understand some basic stuff, below I explain these:<br>
**Accessor (getter):** An accessor, also known as a getter method, is a method used to retrieve the value of an instance 
variable.<br>
**Mutator (setter):** A mutator, or setter method, is a method used to modify the value of an instance variable.

##### Instance Method:
This is a basic method, it is associate with instance of class. When we create method using `self` this method is called 
instance method. It takes `self` as a first parameter, representing the instance on which the method is called.
Instance or class variable can be called by instance method.
```python
class Vehicle:
    class_var = "Mr Nas"
    # instance attribute
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def get_model(self):
        return self.model

c1 = Vehicle('BM1', 'M33')
print(c1.get_model()) #M33
```
```
Output:
M33
```
In above, `self.name` & `self.model` is instance variable.

##### Class Method:
In Python, a class method is a method that is bound to the class and not the instance of the class. It is defined using 
the `@classmethod` decorator. `Class methods` take the class itself as their first parameter, conventionally named `cls`. 
Unlike instance methods, which take `self` as the first parameter, class methods do not have access to the 
`instance-specific` data, but they have access to the `class-level` attributes.
```python
class Vehicle:
    # class-level attribute
    class_var = "Mr. Nas"

    # instance-specific attribute
    def __init__(self, name, model):
        self.name = name
        self.model = model

    @classmethod
    def info(cls):
        cls.class_var = "Mr. Sifat"
        return cls.class_var

print(Vehicle.info()) ## Output: Mr. Sifat
```
```
# Output: Mr. Sifat
```
In above code snippet `class_var = "Mr. Nas"` is a class-level attribute, using `classmethod` we change this value 
to `cls.class_var = "Mr. Sifat"`.

##### Static Method:
A `static method` is a method bound to the class and not the instance of the class. `@staticmethod` decorator define 
static method. Static method useful when you need a method that is not associate with class not instance.
```python
class Vehicle:
    # class-level attribute
    class_var = "Mr. Nas"

    # instance-specific attribute
    def __init__(self, name, model):
        self.name = name
        self.model = model

    @staticmethod
    def info():
        return "This is static method"

print(Vehicle.info()) ## Output: This is static method
```
```
# Output: This is static method
```
In above code example, we use `staticmethod()` for creating static method. 

### Type of inheritance

The `inheritance` is the process of acquiring the properties of one class to another class.

There are five types of inheritance:
- **Simple Inheritance**
   - This kind of inheritance `child` class derived from one `parent` class.
```python
class ParentClass(object):
    def feature_1(self):
        print("Feature 1 is from ParentClass1")
        
# Multiple Inheritance
class ChildClass(ParentClass):
    def feature_3(self):
        print("Feature 3 is from ChildClass")
```
- **Multiple Inheritance**
   - One child class derived from multiple parent classes.
```python
class ParentClass1(object):
    def feature_1(self):
        print("Feature 1 is from ParentClass1")

class ParentClass2(object):
    def feature_2(self):
        print("Feature 2 is from ParentClass2")
        
# Multiple Inheritance
class ChildClass(ParentClass1, ParentClass2):
    ## do something here
    pass
```
In `multiple inheritance` can lead to the Diamond problem, where same methods or attribute can be present in multiple 
parent classes, in that case, the order in which the parent classes are inherited becomes crucial and the method 
regulation order (MRO) is used to determined which method to call.
```python
class ParentClass1(object):
    def feature_1(self):
        print("Feature 1 is from ParentClass1")


class ParentClass2(object):
    def feature_2(self):
        print("Feature 2 is from ParentClass2")


# Multiple Inheritance
class ChildClass(ParentClass1, ParentClass2):
    def call_features(self):
        # Accessing features using super()
        super().feature_1()
        super().feature_2()


# Creating an instance of ChildClass
child_instance = ChildClass()

# Calling the method to see the MRO
child_instance.call_features()

# Checking the MRO
print(ChildClass.__mro__)
```
```
Feature 2 is from ParentClass2
Feature 1 is from ParentClass1
(<class '__main__.ChildClass'>, <class '__main__.ParentClass1'>, <class '__main__.ParentClass2'>, <class 'object'>)
```
- **Multi-level Inheritance**
   - The Child class derived from a class which is already derived from another class.
```python
class ParentClass1(object):
    def feature_1(self):
        print("Feature 1 is from ParentClass1")

class ParentClass2(object):

    def feature_2(self):
        print("Feature 2 is from ParentClass2")

# This class derived from both ParentClass1 & ParentClass2.
class ChildClass1(ParentClass1, ParentClass2):
    def feature_3(self):
        print("Feature 3 is from ChildClass")

# Multi-level Inheritance
class ChildClass2(ChildClass1):
    pass
```
- **Hierarchical Inheritance**
   - Two or more child class is derived from one parent class.
```python
class ParentClass1(object):
    def feature_1(self):
        print("Feature 1 is from ParentClass1")

class ChildClass1(ParentClass1):
    pass

class ChildClass2(ChildClass1):
    pass
```
- Hybrid Inheritance
 - This is combination of all inheritance.

### Polymorphism
Polymorphism is concept which means multiple forms or more than one form. It enables using a single interface
with input of different datatypes, class or may be for different number of input.
```python
len("Sifat")
len([1,2,3,4,5])
```
In above case, inside len we can give string or numbers, it just gives us length of that value, this is one kind of 
polymorphic example.<br>
**Method overriding:** This is important concept for polymorphism. In child class get some method from derived parent
class, in that case child class change these methods its own requirement, this is called method overriding.

Let's try to understand polymorphism by using proper example:
```python
class Bus:
    def start_engine_bus(self):
        print("Bus Starting")

class Car:
    def start_engine_car(self):
        print("Car Starting")

b = Bus()
c = Car()
b.start_engine_bus()
c.start_engine_car()
```
In above code snippet, we can see two classes `Bus` & `Car`. We defined a method each class & they do about same thing. 
But in that case we need to remember method name separately which is difficult to memorize. 
So what can we do, let's see:
```python
class Bus:
    def start_engine(self):
        print("Bus Starting")

class Car:
    def start_engine(self):
        print("Car Starting")
b = Bus()
c = Car()
for item in [b, c]:
    item.start_engine()
```
In that case I defined same method name, despite being different objects, but they work correctly, this is one kind of
polymorphic solution. But we can do it better way:

```python
class Vehicle(object):
    def start_engine(self):
        print("Vehicle star_engin")

class Bus(Vehicle):
    def start_engine(self):
        print("Bus Starting")

class Car(Vehicle):
    def start_engine(self):
        print("Car Starting")

obj_v = Vehicle()
obj_b = Bus()
obj_c = Car()

obj_v.start_engine()
obj_b.start_engine()
obj_c.start_engine()
```
```
Output:
Vehicle start_engin
Vehicle start_engin
Car Starting
```
We just derived `Bus` & `Car` from `Vehicle` & override parent class method on both of child classes.

### Abstract
Abstraction is one of the great feature of object-oriented programming. It just hides the background detail rather than 
expose whole functionality. For example, when we use smartphone and make call to communicate other person, we don't 
need to understand how does it work? What mechanism does it use? A user is not required to know behind the engineering.
This process basically known as data abstraction, when all unnecessary information keep hide from end user.

Now I give you some example for better understanding, I just copy last code example & and modify it:
```python
from abc import ABC, abstractmethod

# Define an abstract class name Vehicle that inherit from ABC
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

# Create concrete class Inherit from abstract Vehicle class
class Bus(Vehicle):
    def start_engine(self):
        print("Bus Starting...")

# Create another concrete class Inherit from abstract Vehicle class
class Car(Vehicle):
    def start_engine(self):
        print("Car Starting...")

obj_v = Vehicle()
obj_b = Bus()
obj_c = Car()

obj_v.start_engine()
obj_b.start_engine()
obj_c.start_engine()
```
```
Output:
Vehicle start_engin
Vehicle start_engin
Car Starting
```
In above code create a `Vechicle` abstract class, inside this we just derived method, not exist any implementation.
Then we just inherit this class into concrete class like `Car` & `Bus`. 
In Python, there hasn't any explicitly defined interface, but using abstract class we can get this flavour. 
Abstract is not an interface, because inside abstract class we create concrete methods, but in interface this is 
not possible.



In conclusion, `object-oriented programming (OOP)` in Python empowers developers to organize code efficiently, enhance 
code reusability, and promote a modular approach. Classes and objects encapsulate data and behavior, fostering a clearer
understanding of the code structure. Inheritance facilitates code hierarchy, while polymorphism allows for flexible and 
dynamic behavior. By embracing OOP principles, developers can create scalable and maintainable systems, making it easier
to adapt to evolving project requirements. Python's syntax and simplicity make it an excellent choice for implementing 
OOP concepts, contributing to the language's widespread popularity for diverse software development needs.