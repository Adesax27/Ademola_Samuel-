# Creating a dictionary with student IDs as the key and student names as the values
students_dict = {"42-039-4736" : "John Doe", "42-039-4737" : "Jane Doe", 
"42-039-4738" : "John Smith", "42-039-4739" : "Jane Smith"} 
# adding an item to the dictionary
students_dict["42-039-4740"] = "John Johnson"
# removing an item from the dictionary  
# using the pop() method
students_dict.pop("42-039-4736")
# Get the number of items in the dictionary
print(len(students_dict))
# print the entire dicrionary
print(students_dict)
# Get a student ID from the user
student_id = input("Enter a student ID: ")
# Check if the student ID is in the dictionary
if student_id in students_dict:
    print("Student name:", students_dict[student_id])   
else:
    print("Student ID not found")
# Find student ID in the dictionary and retrieve the coreesponding student name
student_name = students_dict.get("42-039-4737")
print(student_name)

