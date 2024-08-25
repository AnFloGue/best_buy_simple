import sys
from products import Product
from store import Store, order


def display_menu():
    """
    Show the menu options.
    """
    print("********** Store Menu **********")
    print("Menu:\n1. List all products in store\n2."
          " Show total amount in store\n3."
          " Make an order\n4."
          " Quit\n")

def get_user_input():
    """
    Get and validate user input.
    """
    while True:
        try:
            user_input = int(input("Please choose a number: "))
            if 1 <= user_input <= 4:
                return user_input
        except ValueError:
            print("Invalid input. Please enter a number.")

def list_all_products(store):
    """
    List all products with prices and quantities.
    """
    for i, product in enumerate(store.products, 1):
        print(f"{i}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}")

def show_total_amount(store):
    """
    Show total quantity of items in store.
    """
    total_amount = store.get_total_quantity()
    print(f"Total of {total_amount} items in store\n")

def make_order(store):
    """
    Create an order by selecting products and quantities.
    """
    shopping_list = []
    while True:
        print("------")
        list_all_products(store)
        print("------")
        product_input = input("Which product would you like to order? (Enter empty text to finish order): ")
        if not product_input:
            break
        try:
            product_index = int(product_input) - 1
            if 0 <= product_index < len(store.products):
                product = store.products[product_index]
            else:
                print("Error: Invalid product number.")
                continue
        except ValueError:
            product = next((p for p in store.products if p.name.lower() == product_input.lower()), None)
            if not product:
                print("Error: Invalid product name.")
                continue

        try:
            quantity = int(input("What amount do you want? "))
            if quantity <= 0:
                print("Quantity must be a positive number.")
            elif quantity > product.quantity:
                print("Error: Insufficient quantity in store.")
            else:
                shopping_list.append((product, quantity))
                product.quantity -= quantity
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")

    if shopping_list:
        total_price = order(shopping_list)
        print(f"Total price of the order: ${total_price}")

def quit():
    """
    Exit the program.
    """
    print("Exiting the program...")
    sys.exit()

def start(store):
    """
    Start the program and show the menu.
    """
    display_menu()

    while True:
        user_input = get_user_input()
        menu_functionality = {
            1: list_all_products,
            2: show_total_amount,
            3: make_order,
            4: quit
        }
        if user_input in menu_functionality:
            menu_functionality[user_input](store)
        else:
            print("You entered the wrong key")

        # Only break the loop if user chooses quit (option 4)
        if user_input == 4:
            break
        display_menu()  # Display menu again after any option

def main():
    """
    Initialize the store and start the program.
    """
    product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250)
                ]
    best_buy = Store(product_list)
    start(best_buy)

if __name__ == "__main__":
    main()