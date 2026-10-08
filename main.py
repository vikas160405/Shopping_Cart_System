
product_list = [
    [101, 'Pen', 10, 50],
    [102, 'Pencil', 5, 100],
    [103, 'Eraser', 5, 75],
    [104, 'Sharpener', 15, 40],
    [105, 'Notebook', 50, 30],
    [106, 'Ruler', 20, 25],
    [107, 'Marker', 30, 35],
    [108, 'Highlighter', 25, 30],
    [109, 'Stapler', 80, 15],
    [110, 'Glue Stick', 20, 20]
]
user_list = []
cart_list = []
order_list = []

print("Shopping Cart System")

while True:
    a = int(input("Enter who is using(1 for Admin, 2 for User, 3 for Exit): "))
    if a == 1:
        print("Welcome Admin")
        while True:
            print("\nAdmin Menu:")
            print("1. Add Product")
            print("2. Update Product")
            print("3. Remove Product")
            print("4. View Products")
            print("5. View Users")
            print("6. Exit Admin Menu")
            b = int(input("Enter your choice: "))
            if b == 1:
                product_id = int(input("Enter the product ID: "))
                product_name = input("Enter the name of the product to add: ")
                product_price = float(input("Enter the price of the product: "))
                product_stock = int(input("Enter the stock quantity of the product: "))
                product_list.append([product_id, product_name, product_price, product_stock])
                print(f"{product_name} has been added to the product list.")
            elif b == 2:
                print("========== UPDATE PRODUCT ==========")
                product_id = int(input("Enter the product ID to update: "))

                for product in product_list:
                    if product[0] == product_id:
                        print("Product Found")
                        print(f"ID: {product[0]}")
                        print(f"Name: {product[1]}")
                        print(f"Price: ₹{product[2]}")
                        print(f"Stock: {product[3]}")

                        print("\nWhat do you want to update?")
                        print("1. Update Name")
                        print("2. Update Price")
                        print("3. Update Stock")
                        print("4. Cancel")

                        choice = int(input("Enter your choice: "))

                        if choice == 1:
                            new_name = input("Enter new product name: ")
                            product[1] = new_name
                            print("Product name updated successfully.")

                        elif choice == 2:
                            new_price = float(input("Enter new price: "))
                            product[2] = new_price
                            print("Product price updated successfully.")

                        elif choice == 3:
                            new_stock = int(input("Enter new stock: "))
                            product[3] = new_stock
                            print("Product stock updated successfully.")

                        elif choice == 4:
                            print("Update cancelled.")

                        else:
                            print("Invalid choice.")

                        break

                else:
                    print("Product not found.")
            elif b == 3:
                print("========== REMOVE PRODUCT ==========")
                product_id = int(input("Enter the product ID to remove: "))
                for product in product_list:
                    if product[0] == product_id:
                        product_list.remove(product)
                        print(f"{product[1]} has been removed from the product list.")
                        break
                else:
                    print("Product not found.")
            elif b == 4:
                print("\n========== PRODUCT LIST ==========")
                for product in product_list:
                    print(f"ID       : {product[0]}")
                    print(f"Name     : {product[1]}")
                    print(f"Price    : ₹{product[2]}")
                    print(f"Stock    : {product[3]}")
                    print("-" * 30)
            elif b == 5:
                print("========== VIEW USERS ==========")
                if len(user_list) == 0:
                    print("No users registered yet.")
                else:
                    for user in user_list:
                        print(f"User ID : {user[0]}")
                        print(f"Name    : {user[1]}")
                        print(f"Email   : {user[2]}")
                        print("-" * 30)
                        
            elif b == 6:
                print("Exiting Admin Menu")
                break
            else:
                print("Invalid input. Please enter a number between 1 and 6.")
    elif a == 2:
        print("welcome User")
        while True:
            print("\nUser Menu:")
            print("1. View Products")
            print("2. Add to Cart")
            print("3. Remove from Cart")
            print("4. View Cart")
            print("5. Checkout")
            print("6. Exit User Menu")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print("\n========== PRODUCT LIST ==========")
                for product in product_list:
                    print(f"ID       : {product[0]}")
                    print(f"Name     : {product[1]}")
                    print(f"Price    : ₹{product[2]}")
                    print(f"Stock    : {product[3]}")
                    print("-" * 30)
            elif choice == 2:
                print("\n========== ADD TO CART ==========")
                product_id = int(input("Enter the product ID to add: "))
                for product in product_list:
                    if product[0] == product_id:   
                        print(f"Product Found: {product[1]}")
                        print(f"Price: ₹{product[2]}")
                        print(f"Available Stock: {product[3]}")
                        
                        quantity = int(input("Enter the Quantity: "))
                        if quantity <= 0:
                            print("Quantity must be greater than 0.")
                        elif quantity > product[3]:
                            print("Not enough stock available.")
                        else:
                            cart_list.append([product[0], product[1], product[2], quantity])
                            product[3] = product[3] - quantity
                            print(f"{quantity}{product[1]} added to cart.")
                            print(f"Remaning stock: {product[3]}")
                        break
                else:
                    print("Product not found.")
                    
            elif choice == 4:
                print("\n========== YOUR CART ==========")
                if len(cart_list)==0:
                    print("Your cart is empty.")
                else:
                    total = 0
                    for cart in cart_list:
                        subtotal = cart[2] * cart[3]
                        total = total + subtotal
                        print(f"Product ID : {cart[0]}")
                        print(f"Name       : {cart[1]}")
                        print(f"Price      : ₹{cart[2]}")
                        print(f"Quantity   : {cart[3]}")
                        print(f"Subtotal   : ₹{subtotal}")
                        print("-" * 30)
                        
                    print(f"Total Amount: ₹{total}")
                    
            elif choice == 3:
                print("\n========== REMOVE FROM CART ==========")
                product_id = int(input("Enter the product ID to remove: "))
                for cart in cart_list:
                    if cart[0] == product_id:
                        print(f"Product Found: {cart[1]}")
                        print(f"Quantity in cart: {cart[3]}")
                        
                        for product in product_list:
                            if product[0] == product_id:
                                product[3] = product[3] + cart[3]
                                break
                        
                        cart_list.remove(cart)
                        print(f"{cart[1]} remove from cart.")
                        break
                else:
                    print("Product not found in cart.")
                    
            elif choice == 5:
                print("\n========== CHECKOUT ==========")
                if len(cart_list) == 0:
                    print("Your cart is empty.")
                else:
                    total = 0
                    for cart in cart_list:
                        subtotal = cart[2] * cart[3]
                        total = total + subtotal
                        print(f"Product : {cart[1]}")
                        print(f"Price   : ₹{cart[2]}")
                        print(f"Quantity: {cart[3]}")
                        print("-" * 30)
                    print(f"Total Amount: ₹{total}")
                    confirm = input("Do you want to place the order? (yes/no): ")
                    if confirm.lower() == 'yes':
                        order_list.append(cart_list.copy())
                        cart_list.clear()
                        print("Order placed successfully.")
                        print("Thank you for shopping!")  
                    else:
                        print("Checkout cancelled.")
                        
            elif choice == 6:
                print("Exiting User Menu")
                break
                    
    elif a == 3:
        print("Exiting the system")
        break
    else:
        print("Invalid input. Please enter 1 for Admin, 2 for User, or 3 for Exit.")
    