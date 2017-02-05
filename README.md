# dinjector
A Python implementation for dependency injection.


# Use as follows:    

First: decorate your classes with the decorator "dinjector.register", next provide a selector, which will be used 
later to find and create instances without explicit module import. In this way we can have a decoupling 
between the classes and where they are used.

from dinjector import dinjector

@dinjector.register("one")
class MyClass:
    def __init__(self):
        self.name = "clayton"


@dinjector.register(123)
class OtherClass:
    def __init__(self, pk, name):
        self.id = pk
        self.name = name
       
       
Second:  use as follows

from dinjector import dinjector

o1 = dinjector.new("one")
print(o1.name)

o2 = dinjector.new(123, 1000, "john doe")
print(o2.id)
print(o2.name)
