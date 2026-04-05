# Declaring Variables
cart = {}
amount = int
price = 0
stock = int
total = 0
discounted_total = 0
cash_amount = 0
subtotal = 0
tax = 0
change = 0
discounted_amount = 0
# List of Products
products = {
    "Sliced Bread": {"price": 500, "stock": 30},
    "Rice": {"price": 350, "stock": 45},
    "Flour": {"price": 450, "stock": 45},
    "Soda": {"price": 150, "stock": 50},
    "Water": {"price": 120, "stock": 50},
    "Tissue": {"price": 100, "stock": 25},
    "Sugar": {"price": 160, "stock": 35},
    "Toothpaste": {"price": 180, "stock": 20},
    "Soap": {"price": 100, "stock": 25},
    "Egg": {"price": 550, "stock": 15},
    "Carrot": {"price": 190, "stock": 30},
    "Tomato": {"price": 140, "stock": 25}
}
cart_product = []


# Function showing all the actions that can be taken. A loop was used so the options can be repeated after each choice.
def options_menu():
    print("1.View products available")
    print("2. Add product to cart")
    print("3. Remove product from cart")
    print("4. View products in cart")
    print("5. Cashout")
    print("6. Done")

# Function to view products. Users choose 1 for the products to be displayed.
def view_products():
    print(products)


# Function to add product to cart while checking and updating stock availability.
# Users choose 2 to select each product they would like to purchase.
def add_product_to_cart(cart):
    product = str(input("Enter product name:"))
    if product in products:
        try:
            amount = int(input("Enter the amount of product:"))
            if amount > 0:
                if products[product]["stock"] >= amount:
                    if product in cart:
                        cart[product] += amount
                    else:
                        cart[product] = amount
                    products[product]["stock"] -= amount
                    print(f"{amount} {product}(s) added to cart.")
                    if products[product]["stock"] < 5:
                        print(f"Low stock for {product}")
                else:
                    print("Invalid. Not enough stock")
            else:
                print("Product not added. Amount must be greater than 0")
        except ValueError:
            print("Invalid. Please enter a number.")
    else:
        print("not found")


# To remove products users choose 3. Function to remove products from cart using product name and amount
# Users are prompted to enter the name and amount of the product they would like to remove.
def remove_product_from_cart(cart):
    product = str(input("Enter product name you would like to remove:"))
    if product in products:
        try:
            amount = int(input("Enter the amount of product you would like to remove:"))
            if amount > 0:
                if cart[product] >= amount:
                    cart[product] -= amount
                    products[product]["stock"] += amount
                    print(f"{amount} removed from cart.")
                    print("Updated Stock", products)
                    if cart[product] == 0:
                        del cart[product]
                else:
                    print("Product not removed.")
            else:
                print("Product not removed. Amount must be greater than 0")
        except ValueError:
            print("something went wrong")
    else:
        print("Product Not Found")


# To view the cart user choose 4. Function to view cart and show subtotal
# Users are prompted to view products, amount and price along with the subtotal.
def view_cart(cart):
    if not cart:
        print("Product not in cart.")

    print(" Your Cart ")
    total = 0
    for product, amount in cart.items():
        price = products[product]["price"]
        product_total = price * amount
        print(f"{product}:{amount} * ${price:.2f} = ${product_total:.2f}")
        total += product_total
    print(f"Subtotal: ${total:.2f}")


# To cashout users choose 5.Function is used to check out or cashout after purchase is completed
# This shows all calculations done to output the total, discounted total, total after tax, amount paid and change.
def cashout(cart, subtotal, discounted_amount, discounted_total, tax, total):
    subtotal = sum(products[product]["price"] * amount for product, amount in cart.items())
    tax_rate = 0.10
    tax = subtotal * tax_rate
    total = subtotal + tax

    if subtotal > 2000:
        discount = 0.05
        discounted_amount = total * discount
        total -= discounted_amount
        discounted_total = subtotal - discounted_amount
        print(f"Discount: -${discounted_amount:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discounted Total: ${discounted_total:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total: ${total:.2f}")
    while True:
        try:
            cash_amount = int(input("Enter amount being paid: $"))
            if cash_amount >= total:
                change = cash_amount - total
                print(f"Change: ${change:.2f}")
                break
            else:
                print("Payment amount is too low")
        except ValueError:
            print("Invalid. Enter a number.")


# To print receipt users choose 6. Function is used to generate receipt
def generate_bill(cart, subtotal, tax, total, cash_amount, change):
    print("\n***Best Buy Receipt***")
    for product, amount in cart.items():
        price = products[product]["price"]
        product_total = price * amount
        print(f"{product}:{amount} * ${price:.2f} = ${product_total:.2f}")
    print("*" * 50)
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: -${discounted_amount:.2f}")
    print(f"Discounted Total: ${discounted_total:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total: ${total:.2f}")
    print(f"Cash: ${cash_amount:.2f}")
    print(f"Change: ${change:.2f}")
    print("*" * 50)
    print("Thank you for shopping with Best Buy!!")

'''The main structure or loop which runs the entire program while the functions carry out their specific tasks
'''
#A while loop is used to repeatedly display the options menu to the users and process their choices.
cart = {}
while True:
    options_menu()
    options = input("Enter your choice(1-6):")

    if options == '1':
        view_products()
    elif options == '2':
        add_product_to_cart(cart)
    elif options == '3':
        remove_product_from_cart(cart)
    elif options == '4':
        view_cart(cart)
    elif options == '5':
        cashout(cart, subtotal, discounted_amount, discounted_total, tax, total)
    elif options == '6':
        generate_bill(cart, subtotal, tax, total, cash_amount, change)
        break
    else:
        print("Error. Please enter a choice 1-6")

