class Delivery:
    """
    Handles delivery tracking for an order.
    """

    def __init__(self, delivery_id, order_id, address):

        self.__delivery_id = delivery_id
        self.__order_id = order_id
        self.__address = address
        self.__status = "Preparing"



    def get_delivery_id(self):

        return self.__delivery_id



    def get_order_id(self):

        return self.__order_id



    def get_address(self):

        return self.__address



    def get_status(self):

        return self.__status



    def update_status(self, status):

        self.__status = status



    def display_delivery(self):

        print("\n========== DELIVERY ==========")

        print(f"Delivery ID: {self.__delivery_id}")
        print(f"Order ID: {self.__order_id}")
        print(f"Address: {self.__address}")
        print(f"Status: {self.__status}")

        print("==============================\n")