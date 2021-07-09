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



;
