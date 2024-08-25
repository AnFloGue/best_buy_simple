class Product:
    """
    Represents a product in the store.
    """

    def __init__(self, name, price, quantity):
        """
        Initializes the product with a name, price, and quantity.
        Sets active to True by default.
        """
        if not name:
            raise ValueError("Name can't be empty")
        if price < 0:
            raise ValueError("Price can't be negative")
        if quantity < 0:
            raise ValueError("Quantity can't be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def is_active(self) -> bool:
        """
        Checks if the product is active.
        """
        return self.active

    def activate(self):
        """
        Activates the product.
        """
        self.active = True

    def deactivate(self):
        """
        Deactivates the product.
        """
        self.active = False

    def get_quantity(self) -> float:
        """
        Gets the product quantity.
        """
        return self.quantity

    def set_quantity(self, quantity):
        """
        Sets the product quantity. Deactivates if quantity is zero.
        """
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def show(self) -> str:
        """
        Shows product details.
        """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity) -> float:
        """
        Buys a quantity of the product.
        """
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity to buy must be a positive integer")

        if quantity > self.quantity:
            raise Exception("Not enough quantity available to buy")

        total_price = self.price * quantity
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()

        return total_price