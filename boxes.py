import math
items = int(input("What is the number of manufactured items? "))
box = int(input("What is the number of box? "))
boxes = math.ceil(items / box)
print(f" for {items} items, packing {box} items in each box, you will need {boxes}")

items = int(input("what is the number of manfactured items? "))
box = int(input("what is the number of box? "))
boxes = math.ceil(items / box)
print(f"foe {items} items, packing {box} items in each box, you will need {boxes}")