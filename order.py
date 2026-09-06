from menu import MenuItem
from customer import Customer


class OrderItem:
    """
    Represents a menu item and its quantity in an order.
    """

    def __init__(self, menu_item, quantity):
        self.__menu_item = menu_item
        self.__quantity = int(quantity)

    def get_menu_item(self):
        return self.__menu_item

    def get_quantity(self):
        return self.__quantity

    def get_subtotal(self):
        return self.__menu_item.get_price() * self.__quantity


class Order:
    """
    Represents a customer's food order.
    """

    def __init__(self, order_id, customer):
        self.__order_id = order_id
        self.__customer = customer
        self.__items = []
        self.__status = "Pending"

    def get_order_id(self):
        return self.__order_id

    def get_customer(self):
        return self.__customer

    def get_items(self):
        return self.__items

    def get_status(self):
        return self.__status

    def add_item(self, menu_item, quantity):
        order_item = OrderItem(menu_item, quantity)
        self.__items.append(order_item)

    def remove_item(self, item_id):
        for order_item in self.__items:
            menu_item = order_item.get_menu_item()

            if menu_item.get_item_id() == item_id:
                self.__items.remove(order_item)
                return True

        return False

    def calculate_total(self):
        total = 0

        for order_item in self.__items:
            total += order_item.get_subtotal()

        return total

    def update_status(self, status):
        self.__status = status

    def display_order(self):
        print("\n========== ORDER ==========")
        print(f"Order ID: {self.__order_id}")
        print(f"Customer: {self.__customer.get_name()}")
        print(f"Status: {self.__status}")

        print("\nItems:")

        if not self.__items:
            print("No items in order.")
        else:
            for order_item in self.__items:
                menu_item = order_item.get_menu_item()
                quantity = order_item.get_quantity()
                subtotal = order_item.get_subtotal()

                print(
                    f"{menu_item.get_name()} x {quantity} "
                    f"= ₱{subtotal:.2f}"
                )

        print(f"\nTotal: ₱{self.calculate_total():.2f}")
        print("===========================\n")