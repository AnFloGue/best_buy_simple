from products import Product

class Store:
    """
    Represents a store with a collection of products.
    """

    def __init__(self, products=None):
        """
        Initializes the store with a list of products.
        """
        self.products = products if products is not None else []

    def add_product(self, product):
        """
        Adds a new product to the store.
        """
        self.products.append(product)

    def remove_product(self, product):
        """
        Removes a product from the store.
        """
        index = self.products.index(product)
        del self.products[index]

    def get_total_quantity(self) -> int:
        """
        Returns the total quantity of all products in the store.
        """
        total_quantity = 0
        for product in self.products:
            total_quantity += product.quantity
        return total_quantity

    def get_all_products(self) -> list[Product]:
        """
        Returns a list of all active products in the store.
        """
        products_list_active = []
        for product in self.products:
            if product.active is True:
                products_list_active.append(product)
        return products_list_active

def order(shopping_list) -> float:
    """
    Processes an order and returns the total price.
    """
    total_price = 0
    for product, quantity in shopping_list:
        total_price += product.buy(quantity)
    return total_price