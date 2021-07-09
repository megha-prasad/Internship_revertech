# --> Arithmetic operators :

#   + Addition
#   - Subtraction 
#   * Multiplication
#   / Division
#   % Mod (the remainder after dividing)
#   ** Exponentiation (note that ^ does not do this operation, as you might have seen in other languages)
#   // Divides and rounds down to the nearest integer

# *Also there are bitwise operators.
# --> Quiz: Average Electricity Bill

# My electricity bills for the last three months have been $23, $32 and $64. What is the average monthly electricity bill over the three month period? Write an expression to calculate the mean, and use print() to view the result.

print((32+23+64)/3)
print(32+64+23)

# -->Quiz: Calculate
# Two parts of a floor need tiling. One part is 9 tiles wide by 7 tiles long, the other is 5 tiles wide by 7 tiles long. Tiles come in packages of 6.

# How many tiles are needed?
# You buy 17 packages of tiles containing 6 tiles each. How many tiles will be left over?

required = ((9*7) + (5*7))      # Fill this in with an expression that calculates how many tiles are needed.
print(required)

leftov = (17*6)-required        # Fill this in with an expression that calculates how many tiles will be left over.
print(leftov)

# --> Variables : 
mv_population = 74728

# Here mv_population is a variable, which holds the value of 74728. 
# This assigns the item on the right to the name on the left, which is actually a little different than mathematical equality, as 74728 does not hold the value of mv_population.
# whatever term is on the left side, is now a name for whatever value is on the right side. 
# Once a value has been assigned to a variable name, you can access the value from the variable name.

x = 3
y = 4
z = 5
#or we can do it as:
x, y, z = 3, 4, 5

#Rules for naming a variable:
# 1. Only use ordinary letters, numbers and underscores in your variable names. They can’t have spaces, and need to start with a letter or underscore.

# 2. You can’t use Python's reserved words, or "keywords," as variable names. There are reserved words in every programming language that have important purposes, and you’ll learn about some of these throughout this course. Creating names that are descriptive of the values often will help you avoid using any of these keywords. Here you can see a table of Python's reserved words.

# 3. The pythonic way to name variables is to use all lowercase letters and underscores to separate words.

#YES
my_height = 58
my_lat = 40
my_long = 105

# #NO
# my height = 58
# MYLONG = 40
# MyLat = 105

x=x+2
x+=2

#Quiz-->Assign and Modify Variables

# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff
rainfall -= 0.1*rainfall

# add the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall

# increase reservoir_volume by 5% to account for stormwater that flows
reservoir_volume += 0.05*reservoir_volume
# into the reservoir in the days following the storm

# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume -= 0.05*reservoir_volume

# subtract 2.5e5 cubic metres from reservoir_volume to account for water
reservoir_volume -= 2.5e5
# that's piped to arid regions.

# print the new value of the reservoir_volume variable
print(reservoir_volume)

# -->Booleans, Comparison Operators, and Logical Operators
# The bool data type holds one of the values True or False, which are often encoded as 1 or 0, respectively.

# There are 6 comparison operators that are common to see in order to obtain a bool value:

# Comparison Operators
#symbol use
# 5 < 3	False	Less Than
# 5 > 3	True	Greater Than
# 3 <= 3	True	Less Than or Equal To
# 3 >= 5	False	Greater Than or Equal To
# 3 == 5	False	Equal To
# 3 != 5	True	Not Equal To
# And there are three logical operators you need to be familiar with:
# Logical Use
# 5 < 3 and 5 == 5	False	and - Evaluates if all provided statements are True
# 5 < 3 or 5 == 5	True	or - Evaluates if at least one of many statements is True
# not 5 < 3	True	not - Flips the Bool Value

# -->Quiz: Which is denser, Rio or San Francisco?
# This code calculates the population densities of Rio de Janeiro and San Francisco.

# Write code to compare these densities. Is the population of San Francisco more dense than that of Rio de Janeiro? Print True if it is and False if not.

sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

# Write code that prints True if San Francisco is denser than Rio, and False otherwise
density = san_francisco_pop_density>rio_de_janeiro_pop_density
print(density)
#Also we can code this using if condition
if (san_francisco_pop_density > rio_de_janeiro_pop_density):
    print (True)
else:
    print (False)

#-->Strings
#Strings in Python are shown as the variable type str. 
#You can define a string with either double quotes " or single quotes '. 
#If the string you are creating actually has one of these two values in it, then you need to be careful to assure your code doesn't give an error.

my_string = 'this is a string!'
my_string2 = "this is also a string!!!"
#You can also include a \ in your string to be able to include one of these quotes:

this_string = 'Simon\'s skateboard is in the garage.'
print(this_string)
>>>Simon's skateboard is in the garage.
#If we don't use this, notice we get the following error:

this_string = 'Simon's skateboard is in the garage.'
# File "<ipython-input-20-e80562c2a290>", line 1
#     this_string = 'Simon's skateboard is in the garage.'
#                          ^
# SyntaxError: invalid syntax
#                          ^
# SyntaxError: invalid syntax
# The color highlighting is also an indication of the error you have in your string in this second case. 
# There are a number of other operations you can use with strings as well. In this video you saw a few:

first_word = 'Hello'
second_word = 'There'
rint(first_word + second_word)
>>>HelloThere  #concatination

print(first_word + ' ' + second_word)
>>>Hello There

print(first_word * 5)
>>>HelloHelloHelloHelloHello

print(len(first_word))
>>>5

#Inexing - Python uses 0 indexing 

first_word[0]
>>>H

first_word[1]
>>>e
# The len() function
# len() is a built-in Python function that returns the length of an object, like a string. 
#The length of a string is the number of characters in the string. This will always be an integer.

print(len("ababa") / len("ab"))
>>>2.5

print(type(4)) #data type
>>>int
print(type(3.7))
>>>float
print(type('this'))
>>>str
print(type(True))
bool

#--> Find total sales
mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"
total_sales = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales) 
print("This week's total sales:",total_sales)
#TODO: Print a string with this format: This week's total sales: xxx

# len("this")
# type(12)
# print("Hello world")
# These three above are functions - they use parentheses, and accept one or more arguments. 

# A method in Python behaves similarly to a function. Methods actually are functions that are called using dot notation. 
# For example, lower() is a string method that can be used like this, on a string called "sample string": sample_string.lower().

#Methods are specific to the data type for a particular variable. 
#So there are some built-in methods that are available for all strings, different methods that are available for all integers, etc.

#Each of these methods accepts the string itself as the first argument of the method. 
#However, they also could receive additional arguments, that are passed inside the parentheses.

>>> my_string.islower()
True
>>> my_string.count('a')
2
>>> my_string.find('a')
3
#the count and find methods both take another argument. 
#However, the .islower() method does not accept another argument.

#One important string method: format()

>>>print("Mohammed has {} balloons".format(27))
Mohammed has 27 balloons

animal = "dog"
action = "bite"
print("Does your {} {}?".format(animal, action))
>>>Does your dog bite?
maria_string = "Maria loves {} and {}"
print(maria_string.format("math", "statistics")
>>>Maria loves math and statistics 
#the number of pairs of curly braces {} you use inside the string is the same as the number of replacements you want to make using the values inside format().
      
#Another important string method: split()
#This function or method returns a data container called a list that contains the words from the input string. 
#The split method has two additional arguments (sep and maxsplit). 
#The sep argument stands for "separator". It can be used to identify how the string should be split up (e.g., whitespace characters like space, tab, return, newline; specific punctuation (e.g., comma, dashes)). 
#If the sep argument is not provided, the default separator is whitespace.

#the maxsplit argument provides the maximum number of splits. 
#The argument gives maxsplit + 1 number of elements in the new list, with the remaining string being returned as the last element in the list.

#A basic split method:

new_str = "The cow jumped over the moon."
new_str.split()
>>>['The', 'cow', 'jumped', 'over', 'the', 'moon.']
#Here the separator is space, and the maxsplit argument is set to 3.

new_str.split(' ', 3)
>>>['The', 'cow', 'jumped', 'over the moon.']
#Using '.' or period as a separator.

new_str.split('.')
>>>['The cow jumped over the moon', '']
#Using no separators but having a maxsplit argument of 3.

new_str.split(None, 3)
>>>['The', 'cow', 'jumped', 'over the moon.']

# Quiz: String Methods Coding Practice
# Below, we have a string variable that contains the first verse of the poem, If by Rudyard Kipling.Remember, \n is a special sequence of characters that causes a line break (a new line).

#verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
# Use the code editor below to answer the following questions about verse and use Test Run to check your output in the quiz at the bottom of this page.

# What is the length of the string variable verse?
# What is the index of the first occurrence of the word 'and' in verse?
# What is the index of the last occurrence of the word 'you' in verse?
# What is the count of occurrences of the word 'you' in the verse?
# You will need to refer to Python's string methods documentation.

verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse)
print(len(verse))
print(verse.find("and"))
print(verse.rfind("you"))
print(verse.count("you"))
# Use the appropriate functions and methods to answer the questions above

#--> debugging tips
# Understand common error messages you might receive and what to do about them.
# Search for your error message, using the Web community.
# Use print statements.

#Common error messages:
      #"ZeroDivisionError: division by zero." 
      #"SyntaxError: unexpected EOF while parsing" : 
        #This message is often produced when you have accidentally left out something, like a parenthesis. 
        #This message is often produced when you have accidentally left out something, like a parenthesis. 
        #The message is saying it has unexpectedly reached the end of file ("EOF") and it still didn't find that right parenthesis. 
        #This can easily happen with code syntax involving pairs, like beginning and ending quotes also.
      #"TypeError: len() takes exactly one argument (0 given)" 
        #This kind of message could be given for many functions.
        #like len in this case, if I accidentally do not include the  required number of arguments when I'm calling a function, as below. 
        #This message tells me how many arguments the function requires (one in this case), compared with how many I gave it (0). 
        #I meant to use len(chars) to count the number of characters in this long word, but I forgot the argument.
          chars = "supercalifragilisticexpialidocious"
          len()
