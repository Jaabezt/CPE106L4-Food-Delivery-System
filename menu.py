class MenuItem:
    """
    Represents a single food item in the menu.
    """

    def __init__(self, item_id, name, price, category):

        self.__item_id = item_id
        self.__name = name
        self.__price = float(price)
        self.__category = category


    def get_item_id(self):

        return self.__item_id


    def get_name(self):

        return self.__name


    def get_price(self):

        return self.__price


    def get_category(self):

        return self.__category


    def update_item(self, name, price, category):

        self.__name = name
        self.__price = float(price)
        self.__category = category


    def display_item(self):

        print(
            f"{self.__item_id} | "
            f"{self.__name} | "
            f"₱{self.__price:.2f} | "
            f"{self.__category}"
        )



class Menu:
    """
    Manages MenuItem objects.
    """

    def __init__(self):

        self.__items = []


    def add_item(self, item):

        self.__items.append(item)


    def remove_item(self, item_id):

        for item in self.__items:

            if item.get_item_id() == item_id:

                self.__items.remove(item)

                return True


        return False


    def find_item(self, item_id):

        for item in self.__items:

            if item.get_item_id() == item_id:

                return item


        return None


    def display_menu(self):

        print("\n========== CAFE MENU ==========")

        for item in self.__items:

            item.display_item()

        print("===============================\n")