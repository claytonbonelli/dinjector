# dinjector
A Python implementation for dependency injection. Through the injection of dependencies it is possible to obtain a weak coupling between different classes. The purpose is not to explicitly import classes when it is necessary to create instances of these classes, but instantiations will be created through a name (a selector) associated with a class, and through this selector new instances will be created and no explicit import will be made. In this way we guarantee that a class and the place where it is used does not have a strong coupling.


# Example:    

First: decorate your classes with the decorator "dinjector.register", next provide a selector, which will be used 
later to find and create instances without explicit module import. In this way we can have a decoupling 
between the classes and where they are used.

```python
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
```