class MenuItem:
    """
    Represents a single menu item.
    """

    def __init__(self, item_id, name, price, category):

        # Encapsulation
        self.__item_id = item_id
        self.__name = name
        self.__price = float(price)
        self.__category = category

    # Getters

    def get_item_id(self):
        return self.__item_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_category(self):
        return self.__category

    # Update menu item

    def update_item(self, name, price, category):
        self.__name = name
        self.__price = float(price)
        self.__category = category

    # Display single item

    def display_item(self):
        print(
            f"{self.__item_id:<8}"
            f"{self.__name:<30}"
            f"₱{self.__price:>7.2f}"
        )


class Menu:
    """
    Handles multiple MenuItem objects.
    """

    def __init__(self):

        # Private list of MenuItem objects
        self.__items = []

    # Add item

    def add_item(self, item):
        self.__items.append(item)

    # Get all items

    def get_items(self):
        return self.__items

    # Remove item

    def remove_item(self, item_id):

        for item in self.__items:

            if item.get_item_id() == item_id:

                self.__items.remove(item)

                return True

        return False

    # Find item

    def find_item(self, item_id):

        for item in self.__items:

            if item.get_item_id() == item_id:

                return item

        return None

    # Display menu

    def display_menu(self):

        print("\n========== CAFE MENU ==========\n")

        current_category = None

        for item in self.__items:

            category = item.get_category()

            if category != current_category:

                print(f"\n--- {category.upper()} ---")

                current_category = category

            item.display_item()

        print("\n===============================\n")