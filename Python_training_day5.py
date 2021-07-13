# -->While Loops
# For loops are an example of "definite iteration" meaning that the loop's body is run a predefined number of times. 
# This differs from "indefinite iteration" which is when a loop repeats an unknown number of times and ends when some condition is met, which is what happens in a while loop. 
# an example of a while loop.

card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

# adds the last element of the card_deck list to the hand list
# until the values in hand add up to 17 or more
while sum(hand)  < 17:
    hand.append(card_deck.pop())
# This example features two new functions. sum returns the sum of the elements in a list, and pop is a list method that removes the last element from a list and returns it.

# Components of a While Loop
# The first line starts with the while keyword, indicating this is a while loop.
# Following that is a condition to be checked. In this example, that's sum(hand) <= 17.
# The while loop heading always ends with a colon :.
# Indented after this heading is the body of the while loop. If the condition for the while loop is true, the code lines in the loop's body will be executed.
# We then go back to the while heading line, and the condition is evaluated again. 
# This process of checking the condition and then executing the loop repeats until the condition becomes false.
# When the condition becomes false, we move on to the line following the body of the loop, which will be unindented.
# The indented body of the loop should modify at least one variable in the test condition. If the value of the test condition never changes, the result is an infinite loop!

# --> Practice: Factorials with While Loops
# Find the factorial of a number using a while loop.
# A factorial of a whole number is that number multiplied by every whole number between itself and 1. 
# For example, 6 factorial (written "6!") equals 6 x 5 x 4 x 3 x 2 x 1 = 720. So 6! = 720.
# We can write a while loop to take any given number and figure out what its factorial is.
# Example: If number is 6, your code should compute and print the product, 720.

# number to find the factorial of
number = 6   
# start with our product equal to one
product = 1
# track the current number being multiplied
current = 1
while current<=number:          # write your while loop here
    product*=current             # multiply the product so far by the current number
    current+=1                  # increment current with each iteration until it reaches number    
# print the factorial of number
print(product)

# Practice: Factorials with For Loops
# Now use a for loop to find the factorial!

# number to find the factorial of
number = 6   
# start with our product equal to one
product = 1
for n in range(1,number+1):     # write your for loop here
    product *= n
# print the factorial of number
print(product)

# for loops are ideal when the number of iterations is known or finite.

# Examples:

# When you have an iterable collection (list, string, set, tuple, dictionary)
# for name in names:
# When you want to iterate through a loop for a definite number of times, using range()
# for i in range(5):
# while loops are ideal when the iterations need to continue until a condition is met.

# Examples:

# When you want to use comparison operators
# while count <= 100:
# When you want to loop based on receiving specific user input.
# while user_input == 'y':

# -->Break, Continue
# Sometimes we need more control over when a loop should end, or skip an iteration. 
# In these cases, we use the break and continue keywords, which can be used in both for and while loops.

# break terminates a loop
# continue skips one iteration of a loop
# the code breaks the loop when weight exceeds or reaches the limit

# example
manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]

print("METHOD 1")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking loop now!")
        break
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))

# skips an iteration when adding an item would exceed the limit
# breaks the loop if weight is exactly the value of the limit
print("\nMETHOD 2")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking from the loop now!")
        break
    elif weight + cargo_weight > 100:
        print("  skipping {} ({})".format(cargo_name, cargo_weight))
        continue
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))

