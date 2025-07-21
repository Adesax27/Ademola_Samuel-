import random

def main():
    # Create the initial list of numbers
    numbers = [16.2, 75.1, 52.3]
    print(numbers)

    # Call append_random_numbers to add one random number
    append_random_numbers(numbers)
    print(numbers)

    # Call append_random_numbers to add three random numbers
    append_random_numbers(numbers, 3)
    print(numbers)

def append_random_numbers(numbers_list, quantity=1):
    for _ in range(quantity):
        # Generate a random float and round it to one decimal place
        random_number = round(random.uniform(0, 100), 1)
        numbers_list.append(random_number)

if __name__ == "__main__":
    main()