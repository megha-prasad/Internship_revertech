# -->Quiz: Break the String
# Write a loop with a break statement to create a string, news_ticker, that is exactly 140 characters long. You should create the news ticker by adding headlines from the headlines list, inserting a space in between each headline. If necessary, truncate the last headline in the middle so that news_ticker is exactly 140 characters long.

# Remember that break works in both for and while loops. Use whichever loop seems most appropriate. Consider adding print statements to your code to help you resolve bugs.

# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break

print(news_ticker)

#--> Coding Quiz: Check for Prime Numbers
# Prime numbers are whole numbers that have only two factors: 1 and the number itself. The first few prime numbers are 2, 3, 5, 7.

# For instance, 6 has four factors: 1, 2, 3, 6.
# 1 X 6 = 6
# 2 X 3 = 6
# So we know 6 is not a prime number.

# In the following coding environment, write code to check if the numbers provided in the list check_prime are prime numbers.

# If the numbers are prime, the code should print "[number] is a prime number."
# If the number is NOT a prime number, it should print "[number] is not a prime number", and a factor of that number, other than 1 and the number itself: "[factor] is a factor of [number]".
# Example output:

# 7 IS a prime number
# 26 is NOT a prime number, because 2 is a factor of 26
## Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]

for num in check_prime:         ## write your code here
    for i in range(2,num):
        if num%i==0:
            print("{} is NOT a prime number, because {} is a factor of {}".format(num,i,num))
            break
        elif i == num-1:
            print("{} is a prime number".format(num))
## HINT: You can use the modulo operator to find a factor


# -->Zip
# zip returns an iterator that combines multiple iterables into one sequence of tuples. 
# Each tuple contains the elements in that position from all the iterables. For example, printing

list(zip(['a', 'b', 'c'], [1, 2, 3])) 
# output 
[('a', 1), ('b', 2), ('c', 3)].

# Like we did for range() we need to convert it to a list or iterate through it with a loop to see the elements.

# You could unpack each tuple in a for loop like this.

letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))
# In addition to zipping two lists together, you can also unzip a list into tuples using an asterisk.

some_list = [('a', 1), ('b', 2), ('c', 3)]
letters, nums = zip(*some_list)

# -->Enumerate
# enumerate is a built in function that returns an iterator of tuples containing indices and values of a list. 

letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)
# This code would output:

0 a
1 b
2 c
3 d
4 e

# if we use zip then:
letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in zip(range(len(letters))),letters):
    print(i, letter)
    
# -->Quiz: Zip Coordinates
# Use zip to write a for loop that creates a string specifying the label and coordinates of each point and appends it to the list points. Each string should be formatted as label: x, y, z. For example, the string for the first coordinate should be F: 23, 677, 4.

x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
for label,x,y,z in zip(labels,x_coord,y_coord,z_coord):
    points.append("{}: {}, {}, {}".format(label,x,y,z))         # write your for loop here


for point in points:
    print(point)

# -->Quiz: Zip Lists to a Dictionary
# Use zip to create a dictionary cast that uses names as keys and heights as values.

cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names,cast_heights))# replace with your code
print(cast)

# -->Quiz: Unzip Tuples
# Unzip the cast tuple into two names and heights tuples.

cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

# define names and heights here

names,heights = zip(*cast)
print(names)
print(heights)

# -->Quiz: Transpose with Zip
# Use zip to transpose data from a 4-by-3 matrix to a 3-by-4 matrix. There's actually a cool trick for this! Feel free to look at the solutions if you can't figure it out.

data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
# m1,m2,m3=zip(*data)
# print(m1)
# print(m2)
# print(m3)

data_transpose = tuple(zip(*data))# replace with your code
print(data_transpose)

# -->Quiz: Enumerate
# Use enumerate to modify the cast list so that each element contains the name followed by the character's corresponding height. 
# For example, the first element of cast should change from "Barney Stinson" to "Barney Stinson 72".

cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]
for i,casts in enumerate(cast):
    cast[i] = casts + " " + str(heights[i])
# write your for loop here


print(cast)

