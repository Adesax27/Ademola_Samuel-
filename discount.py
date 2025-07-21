import datetime # importing datetime fuction
current_day = datetime.datetime.now().strftime("%A")

# ask the user for subtotal
subtotal = float(input("what is your subtotal amount? $"))

# discount and tax
discount_rate = 0.10
tax_rate = 0.06
# using if statement
if current_day in ["Tuesday", "Wednessday"] and subtotal >= 50:
    discount = subtotal * discount_rate
    subtotal -= discount
else:
    discount = 0
# calculating for tax
tax = tax_rate * subtotal
total_amount = subtotal + tax
if discount > 0:
    print(discount)
print(tax)
print(total_amount)

# if additional amount needed for discount
if current_day in ["Tuesday","Wednessday"] and subtotal < 50:
    additional_amount_needed = 50 - subtotal
    print(additional_amount_needed)

