#forcing a sync

num1 = 42 #variable declaration
num2 = 2.3 # variable declaration
boolean = True # this is a variable named "boolean" that contains boolean value
string = 'Hello World' # this is a variable of type string, also named "string"
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  # this is an array stored in a variable
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}  # this is a dictionary with key: value pairs; some values are stings, some integers and some boolean
fruit = ('blueberry', 'strawberry', 'banana')
print(type(fruit))
print(pizza_toppings[1]) # this is instructed to print the 1st index value from the array called "pizza_toppings"
pizza_toppings.append('Mushrooms') # append is not ringing a bell; it looks as though it wants to perform a similar function as push, in which a value is added to an array
print(person['name']) # this instructs to print (display) the index value of name from the array called person
person['name'] = 'George' #i know what this is doing but not sure how to describe it... in the array named person, it is setting a new key:value for the index position  of "name" with its value being "George"
person['eye_color'] = 'blue' #i know what this is doing but not sure how to describe it... in the array named person, it is setting a new key:value for the index position  of "eye_color" with its value being "blue"
print(fruit[2]) # this instruction displays the second index, i.e. position 2, of the array named "fruit"

# an if/else statement evaluating the value of variable "num1" and displaying (printing) a result
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

# an if/else with an added if condition on the length of the variable "string": less than 5 do this; greater than 15 do this; otherwise for anything else between 5 and 15 do the other
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5): #this is creating a sequence of numbers (0,1,2,3,4) and printing them (five numbers in all hence the "5")
    print(x) 
for x in range(2,5): #this is creating a seqence of numbers starting at 2 and ending at 5, printing each (2,3,4)
    print(x)
for x in range(2,10,3): # this creates a sequqnce of numbers starting at 2 and ending by 10, incrementing by 3 each time (2,5,8) and printing
    print(x)
# this is looping with an increment of 1. it starts at 0, prints that, increments by 1 and printing each time SO LONG AS the value of x is less than 5 (0,1,2,3,4)
x = 0 
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop() # this removes the last value in the list named "pizza_toppings"
pizza_toppings.pop(1) # this removes the item at index position 1 and returns that value

# this appears to be adding a key to the list or dictionary named "person". in this case eye_color is added as a key but there is no value
print(person)
person.pop('eye_color')
print(person)


for topping in pizza_toppings:
    if topping == 'Pepperoni': #this is evaluating if value is same, without regard to datatype as a boolean (if it is true the topping is exactly "Pepperoni")...
        continue
    print('After 1st if statement') #the previous condition being true, it continues and prints (displys) string "After 1st if statement"
    if topping == 'Olives': #similar to above, this says if conditions evauates true (topping is exactly "Olives" withut regard for datatype), exit
        break

# this is a function named "print_hello_ten_times" and its instructions are to loop through a sequence from 1-10, each time printing "Hello"
def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times() #this is the previous function being called (executed)

#this sets up a function to sequence through a series of numbers, passed as an argumrnt, to determine how many times, if any, to print the word "Hello"
def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4) # the function above being called with an argument of 4, so the word "Hello" will print (display) 4 times (1-4)

#function is created to print (display) "Hello" as above, but this time the argument is provided inititally. this would print"Helo" ten times after sequqncing through the numbers 1-10
def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times() #this would execute the function above with no change to the argument (result of 10 Hello's)
print_hello_x_or_ten_times(4) #this would append 4 more to the bui;t-in argumnt so "Hello" ends up printing 10 times plus 4 times (14 times)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)