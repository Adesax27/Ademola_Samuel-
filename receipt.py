# Creativity Additions: 
# - Added basic formatting for alignment in the receipt.
# - Included item count next to the subtotal.
# - Used a specific date/time format.

import csv
from datetime import datetime

# Constants
STORE_NAME = "Ademola's Empire"
PRODUCTS_FILENAME = 'products.csv'
REQUEST_FILENAME = 'request.csv'
SALES_TAX_RATE = 0.06  # 6% sales tax

def read_dictionary(filename, key_column_index=0):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters:
        filename (str): The path to the CSV file to read.
        key_column_index (int): The index of the column
            to use as the keys in the dictionary.
    Return:
        dict: A dictionary that contains
            the contents of the CSV file.
    """
    compound_dict = {}
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            # Ensure row has enough columns
            if len(row) > max(key_column_index, 1): # Need at least key and one value col
                key = row[key_column_index]
                # Create list of values from columns other than the key
                value = [elem for i, elem in enumerate(row) if i != key_column_index]
                compound_dict[key] = value
            else:
                print(f"Warning: Skipping malformed row in {filename}: {row}")
    return compound_dict

def main():
    """
    Processes product requests, calculates costs, handles errors, 
    and prints a formatted receipt.
    """
    try:
        # Requirement 1: Print store name
        print(f"\n{STORE_NAME}\n")

        # Read the products dictionary
        products_dict = read_dictionary(PRODUCTS_FILENAME, 0) # Use column 0 as key

        # Initialize calculation variables
        total_items = 0
        subtotal = 0.0

        # Requirement 2: Print requested products (header)
        print("Requested Items:")
        
        # Open and process the request.csv file
        with open(REQUEST_FILENAME, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row

            # Process each row in the request.csv file
            for row in reader:
                if len(row) >= 2: # Ensure row has product number and quantity
                    product_number = row[0]
                    try:
                        quantity = int(row[1])
                    except ValueError:
                        print(f"Warning: Invalid quantity '{row[1]}' for product '{product_number}'. Skipping.")
                        continue # Skip this item if quantity is not an integer

                    # Find the corresponding item in the products_dict
                    # Use direct access [] inside try block to potentially raise KeyError
                    # Although products_dict.get() could also be used safely.
                    # We need the except KeyError block per requirements.
                    product_info = products_dict[product_number] # This might raise KeyError
                    # Assumes product_info list structure is [Name, Price] based on read_dictionary
                    product_name = product_info[0] 
                    try:
                        product_price = float(product_info[1])
                    except ValueError:
                         print(f"Warning: Invalid price '{product_info[1]}' for product '{product_number}'. Skipping item total.")
                         continue # Skip calculations if price is invalid

                    # Print the product name, requested quantity, and product price
                    print(f"  {product_name}: {quantity} @ ${product_price:.2f}")

                    # Update totals
                    total_items += quantity
                    subtotal += quantity * product_price
                else:
                     print(f"Warning: Skipping malformed row in {REQUEST_FILENAME}: {row}")


        print("-" * 30) # Separator line

        # Requirement 3: Print number of items
        print(f"Number of Items: {total_items}")

        # Requirement 4: Print subtotal
        print(f"Subtotal: ${subtotal:.2f}")

        # Requirement 5: Compute and print sales tax
        sales_tax = subtotal * SALES_TAX_RATE
        print(f"Sales Tax ({SALES_TAX_RATE:.0%}): ${sales_tax:.2f}")

        # Requirement 6: Compute and print total
        total = subtotal + sales_tax
        print(f"Total: ${total:.2f}")

        # Requirement 7: Print thank you message
        print("\nThank you for shopping at Ademola's Empire!")

        # Requirement 8: Print current date and time
        # Format: Weekday Month Day Hour:Minute:Second Year (e.g., Sat Apr 05 11:39:34 2025)
        # Reference for formats: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
        now = datetime.now()
        # Example format: %a %b %d %H:%M:%S %Y -> Sat Apr 05 11:39:34 2025
        # Another common format: %Y-%m-%d %I:%M:%S %p -> 2025-04-05 11:39:34 AM
        formatted_datetime = now.strftime("%a %b %d %H:%M:%S %Y") 
        print(f"Date: {formatted_datetime}")


    # Requirement 9 & 11: Handle FileNotFoundError
    except FileNotFoundError as fnf_err:
        print(f"\nError: Missing file.")
        print(f"  Details: {fnf_err}")
        print("  Please ensure '{PRODUCTS_FILENAME}' and '{REQUEST_FILENAME}' exist in the same directory.")

    # Requirement 9 & 10: Handle KeyError
    except KeyError as key_err:
        print(f"\nError: Unknown product ID found in '{REQUEST_FILENAME}'.")
        print(f"  Details: Product ID '{key_err}' not found in '{PRODUCTS_FILENAME}'.")
        print("  Please check the product IDs in the request file.")
        
    # Generic error handler for other potential issues
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")


if __name__ == "__main__":
    main()