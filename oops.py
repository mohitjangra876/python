#  Class in python 
#  We cna create class using the class keyword 
class abc:
    x= 5

#  class instance/object -> creating object of class 

ob = abc()
print(ob.x)

#  del keyword -> we can delete objects with del keyword
del ob


#  we can  create multiple objects for same class

class MyClass:
    x = "Hello"

p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)


#  The pass statement -> class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

class Person:
  pass


"""  Imp ->  The __init__() Method  """

"""
All classes have a built-in method called __init__(), which is always executed when the class is being initiated.

The __init__() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created.
"""

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)


#  Note -> Why Use __init__()?

#  Without the __init__() method, you would need to set properties manually for each object:

#  Example -> withouot __init__ method 

class Person:
  pass

p1 = Person()
p1.name = "Tobias"
p1.age = 25

print(p1.name)
print(p1.age)


#  Default Values in __init__()

class Person:
  def __init__(self, name, age=18):   # age default value set
    self.name = name
    self.age = age

p1 = Person("Emil")
p2 = Person("Tobias", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)


