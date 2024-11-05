from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price

    @abstractmethod
    def calculate_price(self):
        """Calculate the final price based on specific product type."""
        pass


class Book(Product):
    def calculate_price(self):
        tax = 0.1  # 10% tax for books
        final_price = self.base_price * (1 + tax)
        return final_price


class Electronics(Product):
    def calculate_price(self):
        tax = 0.2  # 20% tax for electronics
        final_price = self.base_price * (1 + tax)
        return final_price


class PaymentProcessor(ABC):
    def connection_checker():
        print("Connected successfully")

    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")


class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")


class BitcoinProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing Bitcoin payment of ${amount}")


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)
        print(f"Added {product.name} to cart.")

    def remove_product(self, product_name):
        self.items = [item for item in self.items if item.name != product_name]
        print(f"Removed {product_name} from cart.")

    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            for item in self.items:
                print(f"{item.name} - ${item.calculate_price():.2f}")

    def calculate_total(self):
        return sum(item.calculate_price() for item in self.items)


class User(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def perform_action(self, cart):
        pass


class Customer(User):
    def __init__(self, name):
        super().__init__(name)

    def perform_action(self, cart, payment_processor):
        total = cart.calculate_total()
        print(f"Total price for {self.name} is ${total:.2f}")
        payment_processor.process_payment(total)


class Admin(User):
    def __init__(self, name):
        super().__init__(name)

    def perform_action(self, cart):
        print(f"Admin {self.name} is viewing the cart:")
        cart.view_cart()


# Create products
book1 = Book("Python Programming", 50)
electronics1 = Electronics("Smartphone", 500)

# Create a cart and add products
cart = Cart()
cart.add_product(book1)
cart.add_product(electronics1)

# Create payment processors
credit_card_processor = CreditCardProcessor()
paypal_processor = PayPalProcessor()

# Create users
customer = Customer("Alice")
admin = Admin("Bob")

# Admin views the cart
admin.perform_action(cart)  # Admin can only view

# Customer checks out
customer.perform_action(cart, credit_card_processor)  # Customer uses Credit Card to pay

# Removing a product and re-checking out with a different payment method
cart.remove_product("Smartphone")
customer.perform_action(cart, paypal_processor)  # Customer uses PayPal to pay
