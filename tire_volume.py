# Generating a code for tire volume
# importing math lib
import math
# importing datatime funtion
from datetime import datetime
current_date_time = datetime.now()
# asking the users input
width = float(input("Enter the width of tire in mm (205): "))
as_ratio = float(input("Enter the aspect ratio (60): "))
diameter = float(input("Enter the diameter of the wheel in inches (15): "))

# looking for the volume of space inside a tire
volume = math.pi * width ** 2 * as_ratio * ((width * as_ratio)+ 2540 * diameter) / 10000000000

print(f" The volume of the space inside a tire is {volume:.2f} liters")
print(f"{current_date_time: %Y - %m - %d}")

# Asking user for another line of inputs
width = float(input("Enter the width of tire in mm (205): "))
as_ratio = float(input("Enter the aspect ratio (60): "))
diameter = float(input("Enter the diameter of the wheel in inches (15): "))

volume = math.pi * width ** 2 * as_ratio * ((width * as_ratio) + 2540 * diameter) / 10000000000

print(f" The volume of the space inside a tire is {volume:.2f} liters")
print(f"{current_date_time: %Y - %m - %d}")

# Introducing volumes.text file
with open("volumes.txt", "a") as file:
    file.write(f"{current_date_time}, {width}, {as_ratio}, {diameter}, {volume:.2f}")
# if elif and els statement
buy_tires = input("would like to buy tires with this diamensions? (yes or no): ").strip().lower()
if buy_tires == "yes":
    phone_number = input("enter your phone number: ").strip()
    with open("volumes.txt", "a") as file:
        file.write(f"phone_number: {phone_number}")
    print("Thank you, your details has been saved.")
elif buy_tires == "no":
    print("Thank you!")
else:
    print("Thank you, love to see you around again.")


