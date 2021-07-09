#--> Data structures
# Types of Data Structures: Lists, Tuples, Sets, Dictionaries, Compound Data Structures

#Data structures are containers that organize and group data types together in different ways. A list is one of the most common and basic data structures in Python.
#We can create a list with square brackets. Lists can contain any mix and match of the data types.

list_of_random_things = [1, 3.4, 'a string', True]
#This is a list of 4 elements. All ordered containers (like lists) are indexed in python using a starting index of 0. 
#Therefore, to pull the first value from the above list, we can write:

>>> list_of_random_things[0]
1

#It might seem like you can pull the last element with the following code, but this actually won't work:
>>> list_of_random_things[len(list_of_random_things)] 
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-34-f88b03e5c60e> in <module>()
----> 1 lst[len(lst)]

IndexError: list index out of range

#However, you can retrieve the last element by reducing the index by 1. Therefore, you can do the following:
>>> list_of_random_things[len(list_of_random_things) - 1] 
True

#Alternatively, you can index from the end of a list by using negative values, where -1 is the last element, -2 is the second to last element and so on.
>>> list_of_random_things[-1] 
True
>>> list_of_random_things[-2] 
a string

#-->Slicing Lists
#we can pull more than one value from a list at a time by using slicing. 
>>> list_of_random_things = [1, 3.4, 'a string', True]
>>> list_of_random_things[1:2]
[3.4]
#will only return 3.4 in a list. Notice this is still different than just indexing a single element, because you get a list back with this indexing. The colon tells us to go from the starting value on the left of the colon up to, but not including, the element on the right.

#If you know that you want to start at the beginning, of the list you can also leave out this value.
>>> list_of_random_things[:2]
[1, 3.4]

#or to return all of the elements to the end of the list, we can leave off a final element.
>>> list_of_random_things[1:]
[3.4, 'a string', True]
#This type of indexing works exactly the same on strings, where the returned value will be a string.

#-->in OR not in?
#we can also use in and not in to return a bool of whether an element exists within our list, or if one string is a substring of another.

>>> 'this' in 'this is a string'
True
>>> 'in' in 'this is a string'
True
>>> 'isa' in 'this is a string'
False
>>> 5 not in [1, 2, 3, 4, 6]
True
>>> 5 in [1, 2, 3, 4, 6]
False

#-->Mutability and Order
#Mutability is about whether or not we can change an object once it has been created. If an object (like a list or string) can be changed (like a list can), then it is called mutable. 
#However, if an object cannot be changed with creating a completely new object (like strings), then the object is considered immutable.

>>> my_lst = [1, 2, 3, 4, 5]
>>> my_lst[0] = 'one'
>>> print(my_lst)
['one', 2, 3, 4, 5]

#However, the following does not work:

>>> greeting = "Hello there"
>>> greeting[0] = 'M'
#This is because strings are immutable. This means to change this string, you will need to create a completely new string.

# There are two things to keep in mind for each of the data types you are using:

# Are they mutable?
# Are they ordered?

# Order is about whether the position of an element in the object can be used to access the element. 
# Both strings and lists are ordered. We can use the order to access parts of a list and string.

# Quiz: List Indexing
# Use list indexing to determine how many days are in a particular month based on the integer variable month, and store that value in the integer variable num_days. 
# For example, if month is 8, num_days should be set to 31, since the eighth month, August, has 31 days.

month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
num_days = days_in_month[month-1]   # use list indexing to determine the number of days in month
print(num_days)
>>>31

# Quiz: Slicing Lists
# Select the three most recent dates from this list using list slicing notation. Hint: negative indexes work in slices!

eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']                
# TODO: Modify this line so it prints the last three elements of the list
print(eclipse_dates[-3:])

# Useful Functions for Lists I
# len() returns how many elements are in a list.
# max() returns the greatest element of the list. How the greatest element is determined depends on what type objects are in the list. The maximum element in a list of numbers is the largest number. The maximum elements in a list of strings is element that would occur last if the list were sorted alphabetically. This works because the the max function is defined in terms of the greater than comparison operator. The max function is undefined for lists that contain elements from different, incomparable types.
# min() returns the smallest element in a list. min is the opposite of max, which returns the largest element in a list.
# sorted() returns a copy of a list in order from smallest to largest, leaving the list unchanged.
>>>sizes = [13,25,4,9,56]
>>>print(sorted(sizes))   #ascending order
[4,9,13,25,56]

>>>print(sorted(sizes, reverse=True))   #descending order
[56,25,13,9,4]

#-->join method
#Join is a string method that takes a list of strings as an argument, and returns a string consisting of the list elements joined by a separator string.

>>>new_str = "\n".join(["fore", "aft", "starboard", "port"])
>>>print(new_str)
fore
aft
starboard
port
#In this example we use the string "\n" as the separator so that there is a newline between each element. 
#We can also use other strings as separators with .join. Here we use a hyphen.

>>>name = "-".join(["García", "O'Kelly"])
>>>print(name)
García-O'Kelly
#It is important to remember to separate each of the items in the list you are joining with a comma (,). 
#Forgetting to do so will not trigger an error, but will also give you unexpected results.

#-->append method
#A helpful method called append adds an element to the end of a list.

>>>letters = ['a', 'b', 'c', 'd']
>>>letters.append('z')
>>>print(letters)
['a', 'b', 'c', 'd', 'z']

#--> Tuples
# A tuple is another useful container. 
#It's a data type for immutable ordered sequences of elements. They are often used to store related pieces of information.
#Consider this example involving latitude and longitude:

location = (13.4125, 103.866667)
print("Latitude:", location[0])
print("Longitude:", location[1])
#Tuples are similar to lists in that they store an ordered collection of objects which can be accessed by their indices. 
#Unlike lists, however, tuples are immutable - you can't add and remove items from tuples, or sort them in place.

#Tuples can also be used to assign multiple variables in a compact way.

dimensions = 52, 40, 100
length, width, height = dimensions
print("The dimensions are {} x {} x {}".format(length, width, height))
#The parentheses are optional when defining tuples, and programmers frequently omit them if parentheses don't clarify the code.

#In the second line, three variables are assigned from the content of the tuple dimensions. This is called tuple unpacking.
#You can use tuple unpacking to assign the information from a tuple into multiple variables without having to access them one by one and make multiple assignment statements.

#If we won't need to use dimensions directly, we could shorten those two lines of code into a single line that assigns three variables in one go!

length, width, height = 52, 40, 100
print("The dimensions are {} x {} x {}".format(length, width, height))

#--> Sets
#A set is a data type for mutable unordered collections of unique elements. 
#One application of a set is to quickly remove duplicates from a list.

>>>numbers = [1, 2, 6, 3, 1, 1, 6]
>>>unique_nums = set(numbers)
>>>print(unique_nums)
{1, 2, 3, 6}

#Sets support the in operator the same as lists do. 
#We can add elements to sets using the add method, and remove elements using the pop method, similar to lists. 
#Although, when you pop an element from a set, a random element is removed. Remember that sets, unlike lists, are unordered so there is no "last element".

>>>fruit = {"apple", "banana", "orange", "grapefruit"}  # define a set
>>>print("watermelon" in fruit)  # check for element
>>>fruit.add("watermelon")  # add an element
>>>print(fruit)
>>>print(fruit.pop())  # remove a random element
>>>print(fruit)
False
{'grapefruit', 'orange', 'watermelon', 'banana', 'apple'}
grapefruit
{'orange', 'watermelon', 'banana', 'apple'}

#Other operations you can perform with sets include those of mathematical sets. 
#Methods like union, intersection, and difference are easy to perform with sets, and are much faster than such operators with other containers.

#--> Dictionaries And Identity Operators
#-->Dictionaries
#A dictionary is a mutable data type that stores mappings of unique keys to values. Here's a dictionary that stores elements and their atomic numbers.

elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
#Dictionaries can have keys of any immutable type, like integers or tuples, not just strings. It's not even necessary for every key to have the same type! 
#We can look up values or insert new values in the dictionary using square brackets that enclose the key.

>>>print(elements["helium"])  # print the value mapped to "helium"
2
>>>elements["lithium"] = 3  # insert "lithium" with a value of 3 into the dictionary
{"hydrogen": 1, "helium": 3, "carbon": 6}

#We can check whether a value is in a dictionary the same way we check whether a value is in a list or set with the in keyword. 
#Dicts have a related method that's also useful, get. get looks up values in a dictionary
#but unlike square brackets, get returns None (or a default value of your choice) if the key isn't found.

>>>print("carbon" in elements)
>>>print(elements.get("dilithium"))
True
None
#Carbon is in the dictionary, so True is printed. Dilithium isn’t in our dictionary so None is returned by get and then printed. 
#If you expect lookups to sometimes fail, get might be a better tool than normal square bracket lookups because errors can crash your program.

#--> Identity Operators
#--> Keyword	Operator
#'is'	evaluates if both sides have the same identity
#'is not'	evaluates if both sides have different identities
#You can check if a key returned None with the is operator. You can check for the opposite using is not.

>>>n = elements.get("dilithium")
>>>print(n is None)
>>>print(n is not None)
True
False
>>>elements.get('kryptonite', 'There\'s no such element!')
"There's no such element!"

#NOTE-  A dictionary is a mutable, unordered data structure that contains mappings of keys to values. 
#       Because these keys are used to index values, they must be unique and immutable. 
#       For example, a string or tuple can be used as the key of a dictionary, but if you try to use a list as a key of a dictionary, you will get an error

#TypeError: unhashable type: 'list'. 
#In Python, any immutable object (such as an integer, boolean, string, tuple) is hashable, meaning its value does not change during its lifetime.
#This allows Python to create a unique hash value to identify it, which can be used by dictionaries to track unique keys and sets to track unique values. 
#This is why Python requires us to use immutable datatypes for the keys in a dictionary.

#--> Compound Data Structures
#We can include containers in other containers to create compound data structures. For example, this dictionary maps keys to values that are also dictionaries!

>>>elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
              "helium": {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}   #nested dictionary
#We can access elements in this nested dictionary like this.

>>>helium = elements["helium"]  # get the helium dictionary
>>>hydrogen_weight = elements["hydrogen"]["weight"]  # get hydrogen's weight
4.002602
#You can also add a new key to the element dictionary.

>>>oxygen = {"number":8,"weight":15.999,"symbol":"O"}  # create a new oxygen dictionary 
>>>elements["oxygen"] = oxygen  # assign 'oxygen' as a key to the elements dictionary
>>>print('elements = ', elements)
elements =  {"hydrogen": {"number": 1,
                          "weight": 1.00794,
                          "symbol": 'H'},
               "helium": {"number": 2,
                          "weight": 4.002602,
                          "symbol": "He"}, 
               "oxygen": {"number": 8, 
                          "weight": 15.999, 
                          "symbol": "O"}}

