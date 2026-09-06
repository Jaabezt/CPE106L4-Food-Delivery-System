class Transaction:
    """
    Represents a completed food delivery transaction.
    """

    def __init__(self, transaction_id, order, payment, delivery):
        self.__transaction_id = transaction_id
        self.__order = order
        self.__payment = payment
        self.__delivery = delivery

    def get_transaction_id(self):
        return self.__transaction_id

    def display_transaction(self):
        print("\n========== TRANSACTION ==========")
        print(f"Transaction ID: {self.__transaction_id}")

        print("\nOrder:")
        print(f"Order ID: {self.__order.get_order_id()}")
        print(f"Customer: {self.__order.get_customer().get_name()}")
        print(f"Order Status: {self.__order.get_status()}")
        print(f"Order Total: ₱{self.__order.calculate_total():.2f}")

        print("\nPayment:")
        print(f"Payment ID: {self.__payment.get_payment_id()}")
        print(f"Payment Amount: ₱{self.__payment.get_amount():.2f}")

        print("\nDelivery:")
        print(f"Delivery ID: {self.__delivery.get_delivery_id()}")
        print(f"Delivery Status: {self.__delivery.get_status()}")

        print("=================================\n")