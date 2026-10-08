# 🛒 Shopping Cart System (Python)

A console-based shopping cart application built in Python, with separate **Admin** and **User** roles. It uses only core Python (lists, loops, conditionals, and `input()`), so no external libraries are needed.

## Features

### Admin
- Add a new product (ID, name, price, stock)
- Update an existing product's name, price, or stock
- Remove a product
- View all products
- View registered users

### User
- View available products
- Add products to the cart with a quantity (stock is reduced automatically)
- Remove products from the cart (stock is restored)
- View the cart with subtotals and total amount
- Checkout with order confirmation

## Tech Stack
- Python 3.6+ (uses f-strings)
- Core Python only: lists, loops, and conditional statements

## Project Structure
```
.
├── main.py
└── README.md
```

## How to Run

1. Clone the repository:
```bash
   git clone https://github.com/vikas160405/Shopping_Cart_System.git
   cd Shopping_Cart_System
```
2. Run the program:
```bash
   python main.py
```

## Usage

```
Shopping Cart System
Enter who is using(1 for Admin, 2 for User, 3 for Exit):
```

| Input | Role |
|-------|------|
| 1 | Admin menu |
| 2 | User menu |
| 3 | Exit the program |

### Admin Menu
```
1. Add Product
2. Update Product
3. Remove Product
4. View Products
5. View Users
6. Exit Admin Menu
```

### User Menu
```
1. View Products
2. Add to Cart
3. Remove from Cart
4. View Cart
5. Checkout
6. Exit User Menu
```

## Default Products

| ID  | Name        | Price (₹) | Stock |
|-----|-------------|-----------|-------|
| 101 | Pen         | 10        | 50    |
| 102 | Pencil      | 5         | 100   |
| 103 | Eraser      | 5         | 75    |
| 104 | Sharpener   | 15        | 40    |
| 105 | Notebook    | 50        | 30    |
| 106 | Ruler       | 20        | 25    |
| 107 | Marker      | 30        | 35    |
| 108 | Highlighter | 25        | 30    |
| 109 | Stapler     | 80        | 15    |
| 110 | Glue Stick  | 20        | 20    |

## How It Works
- Products, users, cart, and orders are stored in Python lists.
- Adding to the cart validates the quantity (must be > 0 and within available stock).
- Removing from the cart returns the quantity back to stock.
- On checkout, the cart is saved to the order list and then cleared.

## Limitations
- Data is stored in memory only and resets when the program exits.
- User registration is not implemented yet, so "View Users" shows no users.
- No input validation for non-numeric entries.

## Future Improvements
- User registration and login
- Persistent storage (file or database)
- Input validation and error handling
- Order history view
- Duplicate product ID checks
