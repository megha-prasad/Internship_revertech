#--> Control Flow
#Control flow is the sequence in which your code is run.
# Conditional Statements
# Boolean Expressions
# For and While Loops
# Break and Continue
# Zip and Enumerate
# List Comprehensions

#-->If Statement
#An if statement is a conditional statement that runs or skips code based on whether a condition is true or false. 

>>>if phone_balance < 5:
>>>    phone_balance += 10
>>>    bank_balance -= 10
#An if statement starts with the if keyword, followed by the condition to be checked.
#In this case phone_balance < 5, and then a colon. The condition is specified in a boolean expression that evaluates to either True or False.

#After this line is an indented block of code to be executed if that condition is true. 
#Here, the lines that increment phone_balance and decrement bank_balance only execute if it is true that phone_balance is less than 5. 
#If not, the code in this if block is simply skipped.
#Use Comparison Operators in Conditional Statements
#In conditional statements, you want to use comparison operators. For example, you'd want to use if x == 5 rather than if x = 5. 
#If your conditional statement is causing a syntax error or doing something unexpected, check whether you have written == or =!

>>>phone_balance = 3
>>>bank_balance = 100
>>>print(phone_balance, bank_balance)
>>>if phone_balance < 5:
>>>     phone_balance += 10
>>>     bank_balance -= 10
>>>print(phone_balance, bank_balance)
3, 100
13, 90

# if we want to execute something if it is False then we can use else.
>>>n=4
>>>if n % 2 == 0 :
>>>     print('Number '+str(n)+' is '+'even)
>>>else:
>>>     print('Number '+str(n)+' is '+'odd)
Number 4 is even

#if we have more than two possible cases then we can use elif:
season = 'spring'
if season == 'spring':
    print('plant the garden!')
elif season == 'summer':
    print('water the garden!')
elif season == 'fall':
    print('harvest the garden!')
elif season == 'winter':
    print('stay indoors!')
else:
    print('unrecognized season')
#output : plant the garden!

# if: An if statement must always start with an if clause, which contains the first condition that is checked. 
#               If this evaluates to True, Python runs the code indented in this if block and then skips to the rest of the code after the if statement.

# elif: elif is short for "else if." 
#               An elif clause is used to check for an additional condition if the conditions in the previous clauses in the if statement evaluate to False. As you can see in the example, you can have multiple elif blocks to handle different situations.

# else: Last is the else clause, which must come at the end of an if statement if used. This clause doesn't require a condition. 
#               The code in an else block is run if all conditions above that in the if statement evaluate to False.

#--> Quiz :Write an if statement that lets a competitor know which of these prizes they won based on the number of points they scored, which is stored in the integer variable points.

# Points	Prize
# 1 - 50	wooden rabbit
# 51 - 150	no prize
# 151 - 180	wafer-thin mint
# 181 - 200	penguin
# All of the lower and upper bounds here are inclusive, and points can only take on positive integer values up to 200.

# In your if statement, assign the result variable to a string holding the appropriate message based on the value of points. 
# If they've won a prize, the message should state "Congratulations! You won a [prize name]!" with the prize name. 
# If there's no prize, the message should state "Oh dear, no prize this time."
        
points = 174

if points <= 50:
    result = "Congratulations! You won a wooden rabbit!"
elif points <= 150:
    result = "Oh dear, no prize this time."
elif points <= 180:
    result = "Congratulations! You won a wafer-thin mint!"
else:
    result = "Congratulations! You won a penguin!"

print(result)
          
#-->complex boolean expressions:
# If statements sometimes use more complicated boolean expressions for their conditions. 
# They may contain multiple comparisons operators, logical operators, and even calculations. Examples:

if 18.5 <= weight / height**2 < 25:
    print("BMI is considered 'normal'")

if is_raining and is_sunny:
    print("Is there a rainbow?")

if (not unsubscribed) and (location == "USA" or location == "CAN"):
    print("send email")
#For really complicated conditions you might need to combine some ands, ors and nots together. Use parentheses if you need to make the combinations clear.

#However simple or complex, the condition in an if statement must be a boolean expression that evaluates to either True or False and it is this value that decides whether the indented block in an if statement executes or not.

