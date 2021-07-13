#-->For Loops
# Python has two kinds of loops - for loops and while loops. A for loop is used to "iterate", or do something repeatedly, over an iterable.

# An iterable is an object that can return one of its elements at a time. 
# This can include sequence types, such as strings, lists, and tuples, as well as non-sequence types, such as dictionaries and files.

# Example
# Let's break down the components of a for loop, using this example with the list cities:

>>>cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
>>>for city in cities:
>>>    print(city)
>>>print("Done!")
# Components of a for Loop
# The first line of the loop starts with the for keyword, which signals that this is a for loop
# Following that is city in cities, indicating city is the iteration variable, and cities is the iterable being looped over. 
# In the first iteration of the loop, city gets the value of the first element in cities, which is “new york city”.
# The for loop heading line always ends with a colon :
# Following the for loop heading is an indented block of code, the body of the loop, to be executed in each iteration of this loop. 
# There is only one line in the body of this loop - print(city).
# After the body of the loop has executed, we don't move on to the next line yet; we go back to the for heading line, where the iteration variable takes the value of the next element of the iterable. 
# In the second iteration of the loop above, city takes the value of the next element in cities, which is "mountain view".
# This process repeats until the loop has iterated through all the elements of the iterable. 
# Then, we move on to the line that follows the body of the loop - in this case, print("Done!"). 
# We can tell what the next line after the body of the loop is because it is unindented.
# Executing the code in the example above produces this output:

new york city
mountain view
chicago
los angeles
Done!
# You can name iteration variables however you like.
# A common pattern is to give the iteration variable and iterable the same names, except the singular and plural versions respectively (e.g., 'city' and 'cities').

# -->Using the range() Function with for Loops
# range() is a built-in function used to create an iterable sequence of numbers. 
# You will frequently use range() with a for loop to repeat an action a certain number of times. 
# Any variable can be used to iterate through the numbers, but Python programmers conventionally use i, as in this example:

for i in range(3):
    print("Hello!")
# Output:

Hello!
Hello!
Hello!
# range(start=0, stop, step=1)
# The range() function takes three integer arguments, the first and third of which are optional:

# The 'start' argument is the first number of the sequence. If unspecified, 'start' defaults to 0.
# The 'stop' argument is 1 more than the last number of the sequence. This argument must be specified.
# The 'step' argument is the difference between each number in the sequence. If unspecified, 'step' defaults to 1.

# Notes on using range():

# If you specify one integer inside the parentheses withrange(), it's used as the value for 'stop,' and the defaults are used for the other two.
# e.g. - range(4) returns 0, 1, 2, 3
# If you specify two integers inside the parentheses withrange(), they're used for 'start' and 'stop,' and the default is used for 'step.'
# e.g. - range(2, 6) returns 2, 3, 4, 5
# Or you can specify all three integers for 'start', 'stop', and 'step.'
# e.g. - range(1, 10, 2) returns 1, 3, 5, 7, 9.

# -->Creating and Modifying Lists
# In addition to extracting information from lists, as we did in the first example above, you can also create and modify lists with for loops. 
# You can create a list by appending to a new list at each iteration of the for loop like this:

# Creating a new list
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
capitalized_cities = []

for city in cities:
    capitalized_cities.append(city.title())
# Modifying a list is a bit more involved, and requires the use of the range() function.

# We can use the range() function to generate the indices for each value in the cities list.
# This lets us access the elements of the list with cities[index] so that we can modify the values in the cities list in place.

cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

for index in range(len(cities)):
    cities[index] = cities[index].title()

# Quiz: Create Usernames
# Write a for loop that iterates over the names list to create a usernames list. 
# To create a username for each name, make everything lowercase and replace spaces with underscores. Running your for loop over the list:

# names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# should create the list:

# usernames = ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]

# HINT: Use the .replace() method to replace the spaces with underscores. 

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# # write your for loop here
for name in names:
    i = name.lower().replace(" ","_")
    usernames.append(i)

print(usernames)
#OR
usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for i in range(len(usernames)):
    usernames[i] = usernames[i].lower().replace(" ","_")
    

print(usernames)

# Quiz: Tag Counter
# Write a for loop that iterates over a list of strings, tokens, and counts how many of them are XML tags. 
# XML is a data language similar to HTML. You can tell if a string is an XML tag if it begins with a left angle bracket "<" and ends with a right angle bracket ">". 
# Keep track of the number of tags using the variable count.

# You can assume that the list of strings will not contain empty strings.

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

for i in tokens:
    if '<' and '>' in i:
        count+=1
    else :
        count=count# write your for loop here


print(count)

# Quiz: Create an HTML List
# Write some code, including a for loop, that iterates over a list of strings and creates a single string, html_str, which is an HTML list. For example, if the list is items = ['first string', 'second string'], printing html_str should output:

# <ul>
# <li>first string</li>
# <li>second string</li>
# </ul>
# That is, the string's first line should be the opening tag <ul>. Following that is one line per element in the source list, surrounded by <li> and </li> tags. The final line of the string should be the closing tag </ul>.

items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line
for i in items:
    html_str+='<li>{}</li>\n'.format(i) 
# write your code here
html_str+='</ul>'
print(html_str)


# -->Building Dictionaries
#two important concepts: 1) counting with for loops and 2) the dictionary get method. 
# These two can actually be combined to create a useful counter dictionary, something you will likely come across again. 
# For example, we can create a dictionary, word_counter, that keeps track of the total count of each word in a string.

# The following are a couple of ways to do it:

# Method 1: Using a for loop to create a set of counters
# Let's start with a list containing the words in a series of book titles:

book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
# Step 1: Create an empty dictionary.

word_counter = {}
# Step 2. Iterate through each element in the list. If an element is already included in the dictionary, add 1 to its value. If not, add the element to the dictionary and set its value to 1.

for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1
# What's happening here?
# The for loop iterates through each element in the list. For the first iteration, word takes the value 'great'.
# Next, the if statement checks if word is in the word_counter dictionary.
# Since it doesn't yet, the statement word_counter[word] = 1 adds great as a key to the dictionary with a value of 1.
# Then, it leaves the if else statement and moves on to the next iteration of the for loop. word now takes the value expectations and repeats the process.
# When the if condition is not met, it is because thatword already exists in the word_counter dictionary, and the statement word_counter[word] = word_counter[word] + 1 increases the count of that word by 1.
# Once the for loop finishes iterating through the list, the for loop is complete.
# We can see the output by printing out the dictionary. Printing word_counter results in the following output.

{'great': 2, 'expectations': 1, 'the': 2, 'adventures': 2, 'of': 2, 'sherlock': 1, 'holmes': 1, 'gasby': 1, 'hamlet': 1, 'huckleberry': 1, 'fin': 1}

# Method 2: Using the get method
# We will use the same list for this example:

book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
# Step 1: Create an empty dictionary.
word_counter = {}
# Step 2. Iterate through each element, get() its value in the dictionary, and add 1.
# the dictionary get method is another way to retrieve the value of a key in a dictionary. 
# Except unlike indexing, this will return a default value if the key is not found. 
# If unspecified, this default value is set to None. We can use get with a default value of 0 to simplify the code from the first method above.

for word in book_title:
    word_counter[word] = word_counter.get(word, 0) + 1
# What's happening here?
# The for loop iterates through the list as we saw earlier. The for loop feeds 'great' to the next statement in the body of the for loop.
# In this line: word_counter[word] = word_counter.get(word,0) + 1, since the key 'great' doesn't yet exist in the dictionary, get() will return the value 0 and word_counter[word] will be set to 1.
# Once it encounters a word that already exists in word_counter (e.g. the second appearance of 'the'), the value for that key is incremented by 1. On the second appearance of 'the', the key's value would add 1 again, resulting in 2.
# Once the for loop finishes iterating through the list, the for loop is complete.
# Printing word_counter shows us we get the same result as we did in method 1.

{'great': 2, 'expectations': 1, 'the': 2, 'adventures': 2, 'of': 2, 'sherlock': 1, 'holmes': 1, 'gasby': 1, 'hamlet': 1, 'huckleberry': 1, 'fin': 1}

# -->Iterating Through Dictionaries with For Loops
# When you iterate through a dictionary using a for loop, doing it the normal way (for n in some_dict) will only give you access to the keys in the dictionary.
# If we want to iterate through both the keys and values in the dictionary. Consider this dictionary that uses names of actors as keys and their characters as values.

cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }
# Iterating through it in the usual way with a for loop would give you just the keys, as shown below:

for key in cast:
    print(key)
# This outputs:

Jerry Seinfeld
Julia Louis-Dreyfus
Jason Alexander
Michael Richards
# If you wish to iterate through both keys and values, you can use the built-in method items like this:

for key, value in cast.items():
    print("Actor: {}    Role: {}".format(key, value))
# This outputs:

Actor: Jerry Seinfeld    Role: Jerry Seinfeld
Actor: Julia Louis-Dreyfus    Role: Elaine Benes
Actor: Jason Alexander    Role: George Costanza
Actor: Michael Richards    Role: Cosmo Kramer
# items is an awesome method that returns tuples of key, value pairs, which you can use to iterate over dictionaries in for loops.

#--> Quiz
# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits, but you do not want to count the other items in your basket.

result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for keys, values in basket_items.items():
    if keys in fruits:
        result+=values#Iterate through the dictionary
    else:
        result = result

#if the key is in the list of fruits, add the value (number of fruits) to result


print(result)

#--> Quiz
# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for keys, values in basket_items.items():
    if keys in fruits:
        fruit_count+=values
    elif keys not in fruits:
        not_fruit_count += values


print(fruit_count, not_fruit_count)

