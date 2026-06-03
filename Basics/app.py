#  Starting python tutorial , execute each part with shift + enter 

print("Hello World")

#  F string 

name = "John"   
print(f"Hello {name}")

# comments 
#  using # or '''  ''' for multi line comments

#  variables
x = 5
y = "Hello"

# Casting
x = str(5)    # x will be '5'
y = int(5)    # y will be 5
z = float(5)  # z will be 5.0

#  Get the type of a variable
x = 5
print(type(x))  
# Output: <class 'int'>

#  Assign multiple values to multiple variables
a, b, c = 1, 2, 3
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

#  one value to multiple variables
x = y = z = "Hello"
print(x)  # Output: Hello
print(y)  # Output: Hello
print(z)  # Output: Hello

#  Unpack a collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)  # Output: apple
print(y)  # Output: banana
print(z)  # Output: cherry  

# ------------  Strings --------------

#  Multiline string
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""
print(a)

#  Strings are arrays
a = "Hello, World!"
print(a[1])  # Output: e    

#  looping through a string
for x in "banana":
  print(x) 

# string length
a = "Hello, World!"
print(len(a))  # Output: 13

#  check string
txt = "The best things in life are free!"
print("free" in txt)  # Output: True

# check if not in string
txt = "The best things in life are free!"
print("expensive" not in txt)  # Output: True

#  slicing
b = "Hello, World!"
print(b[2:5])  # Output: llo

# slice from the start
b = "Hello, World!"
print(b[:5])  # Output: Hello

#  slice to the end
b = "Hello, World!"
print(b[2:])  # Output: llo, World! 

#  negative indexing
b = "Hello, World!"     
print(b[-5:-2])  # Output: rld

#  reverse string using slicing
b = "Hello, World!"
print(b[::-1])  # Output: !dlroW ,olleH

# ----- Modify Strings --------------

#  upper case
a = "Hello, World!"
print(a.upper())  # Output: HELLO, WORLD!

#  lower case
a = "Hello, World!"     
print(a.lower())  # Output: hello, world!

#  remove whitespace
a = " Hello, World! "   
print(a.strip())  # Output: Hello, World!

#  replace string
a = "Hello, World!"     
print(a.replace("H", "J"))  # Output: Jello, World!

#  split string
a = "Hello, World!"
print(a.split(","))  # Output: ['Hello', ' World!']

#  string methods
a = "Hello, World!"
print(a.capitalize())  # Output: Hello, world!
print(a.count("o"))  # Output: 2
print(a.endswith("!"))  # Output: True
print(a.find("World"))  # Output: 7
print(a.isalpha())  # Output: False
print(a.isdigit())  # Output: False
print(a.islower())  # Output: False
print(a.isupper())  # Output: False
print(a.startswith("Hello"))  # Output: True    


#  ----------------------  Lists  ----------------------
#  ordered, changeable, and allow duplicate members.

# create a list     
mylist = ["apple", "banana", "cherry"]
print(mylist)  # Output: ['apple', 'banana', 'cherry']

#  list constructor
mylist = list(("apple", "banana", "cherry"))  # note the double parentheses
print(mylist)  # Output: ['apple', 'banana', 'cherry']

#  list length  
mylist = ["apple", "banana", "cherry"]
print(len(mylist))  # Output: 3

#  Access list items
mylist = ["apple", "banana", "cherry"]
print(mylist[0])  # Output: apple
print(mylist[1])  # Output: banana
print(mylist[2])  # Output: cherry      

#  change list items
mylist = ["apple", "banana", "cherry"]
mylist[1] = "blackcurrant"
print(mylist)  # Output: ['apple', 'blackcurrant', 'cherry']

#  add list items
mylist = ["apple", "banana", "cherry"]
mylist.append("orange")
print(mylist)  # Output: ['apple', 'banana', 'cherry', 'orange']

# extend list -> adds the specified list elements (or any iterable) to the end of the current list
mylist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
mylist.extend(tropical)
print(mylist)  # Output: ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']      

#  remove list items
mylist = ["apple", "banana", "cherry"]
mylist.remove("banana")
print(mylist)  # Output: ['apple', 'cherry']

#  pop list items ( remove by index )
mylist = ["apple", "banana", "cherry"]
mylist.pop(1)
print(mylist)  # Output: ['apple', 'cherry']

#  clear list
mylist = ["apple", "banana", "cherry"]
mylist.clear()  

# Note - we can also use the del keyword to delete the list completely
mylist = ["apple", "banana", "cherry"]
del mylist

#  also we can use the del keyword to delete a specific item in the list        
mylist = ["apple", "banana", "cherry"]
del mylist[0]
print(mylist)  # Output: ['banana', 'cherry']

#  loop through a list
mylist = ["apple", "banana", "cherry"]
for x in mylist:
  print(x)

#  loop through a list using index
mylist = ["apple", "banana", "cherry"]
for i in range(len(mylist)):
  print(mylist[i])  

# looping using list comprehension
mylist = ["apple", "banana", "cherry"]
[print(x) for x in mylist]  

#  List comprehension syntax
#  newlist = [expression for item in iterable if condition == True]

# sort a list
mylist = ["banana", "cherry", "apple"]
mylist.sort()
print(mylist)  # Output: ['apple', 'banana', 'cherry']

# sort a list in descending order
mylist = ["banana", "cherry", "apple"]      
mylist.sort(reverse = True)
print(mylist)  # Output: ['cherry', 'banana', 'apple']

# reverse a list        
mylist = ["apple", "banana", "cherry"]
mylist.reverse()
print(mylist)  # Output: ['cherry', 'banana', 'apple']

#  copy a list ( Without reference )
#  Method 1 - using copy() method
mylist = ["apple", "banana", "cherry"]
mylist2 = mylist.copy()
print(mylist2)  # Output: ['apple', 'banana', 'cherry'] 

#  Method 2 - using list() constructor
mylist = ["apple", "banana", "cherry"]
mylist2 = list(mylist)
print(mylist2)  # Output: ['apple', 'banana', 'cherry']

# Method 3 - using slicing
mylist = ["apple", "banana", "cherry"]
mylist2 = mylist[:]
print(mylist2)  # Output: ['apple', 'banana', 'cherry']

#  Join two lists
#  Method 1 - using + operator
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)  # Output: ['a', 'b', 'c', 1

#  Method 2 - using extend() method
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)  # Output: ['a', 'b', 'c', 1, 2, 3]

#  ------ List Methods --------------   
mylist = ["apple", "banana", "cherry"]
print(mylist.append("orange"))  # Output: None
print(mylist)  # Output: ['apple', 'banana', 'cherry', 'orange']
print(mylist.clear())  # Output: None
print(mylist)  # Output: []
print(mylist.copy())  # Output: []      
# count() method returns the number of times the specified element appears in the list
mylist = ["apple", "banana", "cherry", "apple"]
print(mylist.count("apple"))  # Output: 2



# -----------------------  Tuples  ----------------------   
#  immutable - cannot be changed after creation

mytuple = ("apple", "banana", "cherry")

#  create tuple 
# method 1 - using parentheses
mytuple = ("apple", "banana", "cherry")
print(mytuple)  # Output: ('apple', 'banana', 'cherry')

# method 2 - without parentheses
mytuple = "apple", "banana", "cherry"
print(mytuple)  # Output: ('apple', 'banana', 'cherry')

#  tuple constructor
mytuple = tuple(("apple", "banana", "cherry"))  # note the double parentheses
print(mytuple)  # Output: ('apple', 'banana', 'cherry')

#  Create a tuple with one item
mytuple = ("apple",)  # note the comma
print(mytuple)  # Output: ('apple',)

# Access tuple items
mytuple = ("apple", "banana", "cherry")
print(mytuple[0])  # Output: apple
print(mytuple[1])  # Output: banana
print(mytuple[2])  # Output: cherry 

# Range of indexes
mytuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(mytuple[2:5])  # Output: ('cherry', 'orange', 'kiwi') 

# check if item exists  
mytuple = ("apple", "banana", "cherry")
if "apple" in mytuple:
    print("Yes, 'apple' is in the tuple")  # Output: Yes, 'apple' is in the tuple

# change tuple values ( we can convert the tuple to a list, change the list, and convert it back to a tuple )
mytuple = ("apple", "banana", "cherry")
mylist = list(mytuple)
mylist[1] = "kiwi"
mytuple = tuple(mylist)
print(mytuple)  # Output: ('apple', 'kiwi', 'cherry')   

#  unpacking a tuple
mytuple = ("apple", "banana", "cherry")
(green, yellow, red) = mytuple
print(green)  # Output: apple
print(yellow)  # Output: banana
print(red)  # Output: cherry    

#  using Asterisk * to unpack a tuple
mytuple = ("apple", "banana", "cherry", "orange", "kiwi ", "melon", "mango")
(green, yellow, *red) = mytuple
print(green)  # Output: apple
print(yellow)  # Output: banana
print(red)  # Output: ['cherry', 'orange', 'kiwi ', 'melon', 'mango']       
#  All items will be assigned to the variable specified with the Asterisk, and the list will be created with the remaining items. If the Asterisk is not used, it will raise an error because there are more values to unpack than variables specified. 

# loop through a tuple
mytuple = ("apple", "banana", "cherry")
for x in mytuple:
  print(x)  

# loop thirough a tuple using index
mytuple = ("apple", "banana", "cherry")
for i in range(len(mytuple)):
  print(mytuple[i]) 

#  Join two tuples  
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)  # Output: ('a', 'b', 'c', 1

#  Multiply tuples  
tuple1 = ("a", "b", "c")
tuple2 = tuple1 * 2
print(tuple2)  # Output: ('a', 'b', 'c', 'a

#  ----------- Tuple Methods -------------
mytuple = ("apple", "banana", "cherry", "apple")
print(mytuple.count("apple"))  # Output: 2
print(mytuple.index("banana"))  # Output: 1


# -----------------------  Sets  ----------------------
#  unordered, unchangeable, and unindexed. No duplicate members.

myset = {"apple", "banana", "cherry"}

#  create a set
# method 1 - using curly braces
myset = {"apple", "banana", "cherry"}
print(myset)  # Output: {'banana', 'cherry', 'apple'}   

# method 2 - using set() constructor
myset = set(("apple", "banana", "cherry"))  # note the double
print(myset)  # Output: {'banana', 'cherry', 'apple'}

#  length of a set
myset = {"apple", "banana", "cherry"}
print(len(myset))  # Output: 3

#  Access set items ( we cannot access items in a set by referring to an index or a key, but we can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword )
myset = {"apple", "banana", "cherry"}
for x in myset:
    print(x)

# check if item exists
myset = {"apple", "banana", "cherry"}
print("banana" in myset)  # Output: True

#  Note -> Once a set is created, you cannot change its items, but you can add new items.

# Add items to a set
myset = {"apple", "banana", "cherry"}
myset.add("orange")
print(myset)  # Output: {'banana', 'cherry', 'apple', '

#  Add any iterable (lists, tuples, dictionaries etc.)
myset = {"apple", "banana", "cherry"}
myset.update(["orange", "mango", "grapes"])
print(myset)  # Output: {'banana', 'cherry', 'apple', '
#  we have added a list with the update() method, but you can add any iterable object (tuples, sets, dictionaries etc.).

#  Remove items from a set
myset = {"apple", "banana", "cherry"}
myset.remove("banana")
print(myset)  # Output: {'cherry', 'apple'}

#  pop method removes and returns a random item from the set. If the set is empty, it raises a KeyError.
myset = {"apple", "banana", "cherry"}
x = myset.pop()
print(x)  # Output: apple (or banana, or cherry)
print(myset)  # Output: {'banana', 'cherry'} (or {'apple

#  Loop through a set
myset = {"apple", "banana", "cherry"}
for x in myset:
    print(x)

#  Join two sets  / Set methods ( Uninon , Intersection , Difference ) )

#  union() method returns a new set with all items from both sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)  # Output: {'a', 'b', 'c', 1

# intersection() method returns a new set with only the items that are present in both sets
set1 = {"a", "b", "c"}
set2 = {"b", "c", "d"}
set3 = set1.intersection(set2)
print(set3)  # Output: {'b', 'c'}

# difference() method returns a new set with the items that are only present in the first set, and not in both sets
set1 = {"a", "b", "c"}
set2 = {"b", "c", "d"}
set3 = set1.difference(set2)
print(set3)  # Output: {'a'}

#  Frozenset -> is a set that cannot be changed. Once a frozenset is created, you cannot add or remove items from it. Frozensets are used to create immutable sets, which can be used as keys in dictionaries or as elements of other sets.
myfrozenset = frozenset({"apple", "banana", "cherry"})
print(myfrozenset)  # Output: frozenset({'banana', 'cherry


#  --------------- set Methods ---------------
myset = {"apple", "banana", "cherry"}
print(myset.add("orange"))  # Output: None
print(myset)  # Output: {'banana', 'cherry', 'apple', '

#  set has clear , pop , remove , union , intersection , difference methods as well

# -----------------------  Dictionaries  ----------------------
#  unordered, changeable and indexed. No duplicate members.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#  create a dictionary
# method 1 - using curly braces
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# method 2 - using dict() constructor
thisdict = dict(brand="Ford", model="Mustang", year=1964)
print(thisdict)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# length of a dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(len(thisdict))  # Output: 3

#  access dictionary items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])  # Output: Ford
print(thisdict.get("model"))  # Output: Mustang

# get keys and values , items methods
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict.keys())  # Output: dict_keys(['brand', 'model', 'year
print(thisdict.values())  # Output: dict_values(['Ford', 'Mustang', 1964])
print(thisdict.items())  # Output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

#  change dictionary items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2020
print(thisdict)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

#  update method to change dictionary items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

# add dictionary items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["color"] = "red"
print(thisdict)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

#  we can also use the update() method to add items to a dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

#  remove dictionary items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
print(thisdict)  # Output: {'brand': 'Ford', 'year': 1964}

# popitem() method removes the last inserted item (in versions before 3.7, it removes a random item) and returns it as a tuple
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict.popitem()
print(x)  # Output: ('year', 1964)
print(thisdict)  # Output: {'brand': 'Ford', 'model': 'Mustang'}

#  clear dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)  # Output: {}

# loop through a dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in thisdict:
    print(x)  # Output: brand model year (Print keys)

for x in thisdict:
    print(thisdict[x])  # Output: Ford Mustang 1964 ( Print values)

for x in thisdict.values():
    print(x)  # Output: Ford Mustang 1964 ( Print values)

for x in thisdict.keys():
    print(x)  # Output: brand model year ( Print keys)

for x, y in thisdict.items():
    print(x, y)  # Output: brand Ford model Mustang year 1964 ( Print keys and values )

# copy a dictionary ( without reference )
# method 1 - using copy() method
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict.copy()
print(mydict)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# method 2 - using dict() constructor
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = dict(thisdict)
print(mydict)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

#  Nested dictionaries
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
print(myfamily)  # Output: {'child1': {'name': 'Emil',  'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}

#  nested dictionary loop but not all are nested
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    },
    "child4": "Not nested"
}
#  printing complete dictionary

for a,obj in myfamily.items():
    print(a,obj)  # Output: child1 {'name': 'Emil', 'year': 2004} child2 {'name': 'Tobias', 'year': 2007} child3 {'name': 'Linus', 'year': 2011} child4 Not nested      
#  printing only nested dictionaries
for a,obj in myfamily.items():
    if type(obj) is dict:
        print(a,obj)  # Output: child1 {'name': 'Emil', 'year': 2004} child2 {'name': 'Tobias', 'year': 2007} child3 {'name': 'Linus', 'year': 2011}    


#  --------------- Dictionary Methods ---------------
mydict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(mydict.get("model"))  # Output: Mustang
print(mydict.keys())  # Output: dict_keys(['brand', 'model', '
print(mydict.values())  # Output: dict_values(['Ford', 'Mustang', 1964])
print(mydict.items())  # Output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
print(mydict.pop("model"))  # Output: Mustang
print(mydict)  # Output: {'brand': 'Ford', 'year': 1964}
print(mydict.popitem())  # Output: ('year', 1964)
print(mydict)  # Output: {'brand': 'Ford'}
print(mydict.update({"year": 2020}))  # Output: None
print(mydict)  # Output: {'brand': 'Ford', 'year': 2020}    


#  If - else short hand

a = 10
b = 20  

print("A") if a > b else print("B")


#  The pass statement is used when a statement is required syntactically but you do not want any command or code to execute. It is often used as a placeholder for future code.
a = 10
if a > 5:
    pass  # This is a placeholder for future code

#  Python match statement -> same as java switch statement

day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")

#  Python for loops 

#  range (start , stop , step )

for x in range(2, 30, 3):
  print(x) 


#  ----------------  Python functions   -------------------------

def my_function():
    print("Hello from a function")

my_function()  # Output: Hello from a function


# Return values from a function

def my_function(x):
    return 5 * x

print(my_function(3))  # Output: 15

#  Pass statement in functions

# Function definitions cannot be empty. If you need to create a function placeholder without any code, use the pass statement:

def my_function():
    pass  # This is a placeholder for future code

my_function()  # Output: None (since the function does not return anything)


#  keyword arguments in functions   -> orders of the arguments does not matter when we use keyword arguments
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1="Emil", child2="Tobias", child3="Linus")  # Output: The youngest child is Linus


# postiton-only parameters in functions -> we can use / to indicate that some parameters are position-only, meaning they must be specified positionally and cannot be used as keyword arguments.
def my_function(a, b, /, c, d):
    print(a, b, c, d)

my_function(1, 2, c=3, d=4)  # Output: 1 2 3 4
#  In this example, a and b are position-only parameters, while c and d can

# Keyword-only parameters in functions -> we can use * to indicate that some parameters are keyword-only, meaning they must be specified as keyword arguments and cannot be used positionally.
def my_function(a, b, *, c, d):
    print(a, b, c, d)   

my_function(1, 2, c=3, d=4)  # Output: 1 2 3 4
#  In this example, a and b can be specified positionally or as keyword arguments, while c and d are keyword-only parameters and must be specified as keyword arguments.    

#  Note - > / → Parameters before it are position-only.
# * → Parameters after it are keyword-only.

# ---------------  Python *args and **kwargs   -----------------------

#  *args and **kwargs allow functions to accept a unknown number of arguments.

"""
Arbitrary Arguments - *args
If you do not know how many arguments will be passed into your function, add a * before the parameter name.

This way, the function will receive a tuple of arguments and can access the items accordingly:

"""  

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus") # Output: The youngest child is Linus


# Using *args with Regular Arguments ->  Regular parameters must come before *args:

def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")  
# Output:
# Hello Emil
# Hello Tobias
# Hello Linus   

""""
Arbitrary Keyword Arguments - **kwargs
If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.
"""

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")  # Output: His last name is Refsnes


# Using **kwargs with Regular Arguments
#  Regular parameters must come before **kwargs:

def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")


"""   Imp
Unpacking Arguments
The * and ** operators can also be used when calling functions to unpack (expand) a list or dictionary into separate arguments.
"""

def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)  # Output: 6


"""
Unpacking Dictionaries with **
If you have keyword arguments stored in a dictionary, you can use ** to unpack them:
"""

def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes") 

#  Global Keyword -> If you need to create a global variable, but are stuck in a local scope, you can use the global keyword.

# The global keyword makes the variable global. Then we can use it anywhere in the program, both inside and outside of functions.

def myfunc():
  global x
  x = 300

myfunc()

print(x)

"""  -------------   Very Important  -------------
# List comprehesions
# List comprehensions provide a concise way to create lists. It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The expressions can be anything, meaning you can put in all kinds of objects in lists.
"""

#  example 1 - create a list of squares of numbers from 0 to 9
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]  

#  Example 


l = [1,2,3,4,5,6]
r = [x*2 for x in l if x%2==0]
print(l)
print(r)



# import m1

# m1.myfn()


from m1 import myfn2
myfn2()


"""  Importnat ------->   Python Dates   """

import datetime

x = datetime.datetime.now()
print(x)


""" Imp - Python Math module """

# Methods in math module
import math
print(math.sqrt(16))  # Output: 4.0
print(math.ceil(1.4))  # Output: 2
print(math.floor(1.4))  # Output: 1     

#  wihtout math module
print(min(1,4,5,2))  # Output: 1     
print(max(1,4,5,2))  # Output: 5     


#  Python JSON 


# Convert from JSON to Python:

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])



# Convert from Python to JSON

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)    



"""  Important ->  Python Try Except  """

"""  
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.
"""

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")