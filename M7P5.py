# Kirill M7P5 09/24/2026

# Start count number of total discount
total_discount = 0

# Asking user to continue program  
choose_user = str(input("What do you want to continue this program (Y): "))

# Begining of the while loop
while choose_user == "Y":

# Entering quantity of iteam and price per of iteam
    quantity = float(input("Enter quantity of the iteam: "))
    price_iteam = float(input("Enter price of an iteam: $"))

# Finding extended price by multiplying quantity by the price of  item
    extended_price = quantity * price_iteam

# If statement: extended price is more than 10000, discount amount is 25%, else 10%
    if extended_price > 10000:
        discount = 0.25 
    else:
        discount = 0.10

# Finding discount amount ny multipling extended price on discount 
    discount_amount = extended_price * discount

# Finding final price by extracting discount amount from extended price
    final_price = extended_price - discount_amount

# Printing Extended price, Discount amount, and Total price
    print()
    print(f"Extended price: ${extended_price:.2f}")
    print()
    print(f"Discount amount: {discount_amount}%")
    print()
    print(f"Total: ${final_price:.2f}")
    print()

# Additing in total discount every discount from user
    total_discount += discount_amount 

# Asking user to continue program
    choose_user = str(input("What do you want to continue this program (Y): "))

# Printing total discount from all users
print()
print(f"Total discount amount: ${total_discount:.2f}")