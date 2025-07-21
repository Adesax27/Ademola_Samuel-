import datetime
# print timestamps to see how long sections code
# take to run

first_name = "Susan"
print("task completed")
print(datetime.datetime.now())
print()

for x in range(0, 10):
    print(x)
print("task completed")
print(datetime.datetime.now())
print()

# INSTEAD USE A USER DEFINE FUNCTION "def"
from datetime import datetime
def print_time():
    print("task complete")
    print(datetime.now())
    print()

first_name = "Susan"
print_time()

for x in range (0,10):
    print(x)
print_time()

# Getting names
def get_intials_names(name):
    initial_names = name[0:1].upper()
    return initial_names

first_name = input("enter fisrt name")
#fisrt_name_initial = get_intials_names(first_name)
last_name = input("enter last name")

print(" Your initials are: " \
      + get_intials_names(first_name) \
        + get_intials_names(last_name))
