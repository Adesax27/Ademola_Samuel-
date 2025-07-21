"""
# This is a comment because it has
# hash symbols at the beginning
length = 5
print()
time = 7.2
print()
in_flight = True
print()
First_name = "Ademola"

print(length, time, in_flight, First_name)
"""
"""
colors = ["yellow","blue","red","purple"]
samples = [67.2,71.3,33.2,4.01]

text = input("what is your name: ?")
color = input("what is your favourite color?")

print(f"My name is {text} and my favourite color is {color}.")
"""
"""
# Example 1
# Create variables of different data types and then
# print the variable names, data types and values.
a = "Her name is " # string
b = "Isabella " # string
c = a + b # string plus string makes string
print(f"a:  {type(a)} {a}")
print(f"b:  {type(b)} {b}")
print(f"c:  {type(c)} {c}")
print()
d = False # boolean
e = True # boolean
print(f"d:  {type(d)} {d}")
print(f"e:  {type(e)} {e}")
print()
f = 15 # int
g = 7.62 # float
h = f + g # int plus float makes float
print(f"f:  {type(f)} {f}")
print(f"g:  {type(g)} {g}")
print(f"h:  {type(h)} {h}")
print()
i = "True" # string because of surrounding quotes 
j = "2.71" # string because of surronding quotes
print(f"i:  {type(i)} {i}")
print(f"j:  {type(j)} {j}")
"""

"""
# Example 2
# The input function always return a string
k = input("Please enter a number") # This returns a string
m = input("Please enter another number") # This returns a string
n = k + m # string plus string makes string
print(f"k:  {type(k)} {k}")
print(f"m:  {type(m)} {m}")
print(f"n:  {type(n)} {n}")
print()
p = int(input("please enter a number")) # This will return a integer value
q = float(input("please enter another number")) # This will return a float value
r = p + q # string plus string makes string
print(f"p:  {type(p)} {p}")
print(f"q:  {type(q)} {q}")
print(f"r:  {type(r)} {r}")
"""
"""
# Arithemetic Operators
x = 5
y = 3
result = x + y

x1 = 5
y1 = 3
result1 = x1 ** y1

x2 = 5
y2 = 3
result2 = x2 // y2

x3 = 17
y3 = 3
result3 = x3 % y3
"""
"""
print(f"21 % 5 == {21 % 5}")
print(f"5 ** 3 == {5 ** 3}")
print(f" 17 // 4 == {17 // 4}")
print(f"17 / 4 == {17 / 4}")
"""
"""
# In arithemetric, it solves from left to right
# example: X/Y*C
print(f" 10 / 5 * 2 == {10 / 5 * 2}")
"""

"""
# Calculating dip and sag
span = float(input(" what is the span distance "))
sag = float(input("what is the sag distance "))
lenght = span + (8 * sag ** 2) / (3 * span)

print(f"The length of cable in meters is:  {lenght:.2f}")
"""

"""
# Example 4
# Calculating the price of pizza and it toppings
pizza_price = 10.95
number_toppings = int(input("How many toppings do you want? "))
toppings = 1.45
total_toppings = number_toppings * toppings
packed_pizza = pizza_price + total_toppings

print(f"Your pizza payment is: ${packed_pizza:.2f}")
"""

# if Statement
# Checking if a number is greater than 500
# if the balance is grater than 500, compute and add interest 
"""
balance = float(input("Enter your amount"))
if balance > 500:
    interest = balance * 0.03
    balance += interest

print(f"The balance is ${balance:.2f}")
"""

# if, elif and else
# Get the rate of cost from a user
"""
cost = float(input("what is the stock cost? "))
if cost < 100:
    rate = 0.10
elif cost < 250:
    rate = 0.15
elif cost < 400:
    rate = 0.18
else:
    rate = 0.20

discount = cost * rate
cost -= discount
#appilied_discount = discount - cost
print(f"After the discount, you will pay {cost:.2f}")
"""

# Logical Operators (or, and)
# A car weight should not exceed 100!
"""
driver = float(input("Drivers weight"))
passengers = float(input("passengers weight"))
if driver >= 54 or (driver <= 54 and passengers >=  46):
    message = "Enjoy the ride"
print(message)
"""

# built-in functions
"""
n = float(input("enter number"))
r = round(n , 2)
print(r)

n = float(input("enter number"))
r = round(n)
print(r)
"""
"""
import math
number = float(input("Enter your number? "))
print(f" the number is {math.sqrt(number)}")
"""
"""
name = input("what is your name: ")
lname = input("what is your last name: ")
mname = input(" what is your middle name: ")

print(name, lname, mname, sep = "|", flush=True, end = "\n")
print(name, lname, mname, sep = "|", flush=False)
"""