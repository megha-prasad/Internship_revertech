#--> Variable Scope
# Variable scope refers to which parts of a program a variable can be referenced, or used, from.

# It's important to consider scope when using variables in functions. 
# If a variable is created inside a function, it can only be used within that function. Accessing it outside that function is not possible.

# This will result in an error
def some_function():
    word = "hello"

print(word)
# In the example above and the example below, word is said to have scope that is only local to each function. 
# This means you can use the same name for different variables that are used in different functions.

# This works fine
def some_function():
    word = "hello"

def another_function():
    word = "goodbye"
    
# Variables defined outside functions, as in the example below, can still be accessed within a function. Here, word is said to have a global scope.

# This works fine
word = "hello"

def some_function():
    print(word)

some_function()
# Notice that we can still access the value of the global variable word within this function. 
# However, the value of a global variable can not be modified inside the function. 
# If you want to modify that variable's value inside this function, it should be passed in as an argument. 

# Scope is essential to understanding how information is passed throughout programs in Python and really any programming language.

egg_count = 0

def buy_eggs():
    egg_count += 12 # purchase a dozen eggs

buy_eggs()

# This code causes an UnboundLocalError, because the variable egg_count in the first line has global scope.
# Note that it is not passed as an argument into the function, so the function assumes the egg_count being referred to is the global variable.
# If we try to change or reassign this global variable, however, as we do in this code, we get an error. 
# Python doesn't allow functions to modify variables that aren't in the function's scope.

# A better way to write this would be:
egg_count = 0

def buy_eggs(count):
    return count + 12  # purchase a dozen eggs

egg_count = buy_eggs(egg_count)

# -->Documentation
# Documentation is used to make your code easier to understand and use. 
# Functions are especially readable because they often use documentation strings, or docstrings. 
# Docstrings are a type of comment used to explain the purpose of a function, and how it should be used. Here's a function for population density with a docstring.

def population_density(population, land_area):
    """Calculate the population density of an area. """
    return population / land_area
# Docstrings are surrounded by triple quotes. 
# The first line of the docstring is a brief explanation of the function's purpose. 
# If you feel that this is sufficient documentation you can end the docstring at this point; single line docstrings are perfectly acceptable, as in the example above.

def population_density(population, land_area):
    """Calculate the population density of an area.

    INPUT:
    population: int. The population of that area
    land_area: int or float. This function is unit-agnostic, if you pass in values in terms
    of square km or square miles the function will return a density in those units.

    OUTPUT: 
    population_density: population / land_area. The population density of a particular area.
    """
    return population / land_area
# If you think that a longer description would be appropriate for the function, you can add more information after the one-line summary. 
# In the example above, you can see that we wrote an explanation of the function's arguments, stating the purpose and types of each one. 
# It's also common to provide some description of the function's output.

# Every piece of the docstring is optional, however, docstrings are a part of good coding practice. 

# -->Lambda Expressions
# You can use lambda expressions to create anonymous functions. 
# That is, functions that don’t have a name. 
# They are helpful for creating quick functions that aren’t needed later in your code. 
# This can be especially useful for higher order functions, or functions that take in other functions as arguments.

# With a lambda expression, this function:

def multiply(x, y):
    return x * y
# can be reduced to:

multiply = lambda x, y: x * y
#Both of these functions are used in the same way. In either case, we can call multiply like this:

multiply(4, 7)
# This returns 28.

# -->Components of a Lambda Function
# The lambda keyword is used to indicate that this is a lambda expression.
# Following lambda are one or more arguments for the anonymous function separated by commas, followed by a colon :. Similar to functions, the way the arguments are named in a lambda expression is arbitrary.
# Last is an expression that is evaluated and returned in this function. This is a lot like an expression you might see as a return statement in a function.
# With this structure, lambda expressions aren’t ideal for complex functions, but can be very useful for short, simple functions.

# --> map() is a higher-order built-in function that takes a function and iterable as inputs, and returns an iterator that applies the function to each element of the iterable. 
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

# def mean(num_list):
#     return sum(num_list) / len(num_list)
mean = lambda num_list: sum(num_list) / len(num_list)

averages = list(map(mean, numbers))
print(averages)

# -->filter() is a higher-order built-in function that takes a function and iterable as inputs and returns an iterator with the elements from the iterable for which the function returns True.

cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

short_cities = list(filter(lambda x: len(x) < 10, cities))
print(short_cities)

