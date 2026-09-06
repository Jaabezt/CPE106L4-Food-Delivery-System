from abc import ABC, abstractmethod


class Payment(ABC):
    """
    Abstract payment class.
    """

    def __init__(self, payment_id, amount):

        self.__payment_id = payment_id
        self.__amount = float(amount)


    def get_payment_id(self):

        return self.__payment_id


    def get_amount(self):

        return self.__amount


    @abstractmethod
    def process_payment(self):

        pass



class CashPayment(Payment):
    """
    Cash payment implementation.
    """

    def __init__(self, payment_id, amount):

        super().__init__(payment_id, amount)



    def process_payment(self):

        return (
            f"Cash payment successful.\n"
            f"Payment ID: {self.get_payment_id()}\n"
            f"Amount: ₱{self.get_amount():.2f}"
        )



class CardPayment(Payment):
    """
    Card payment implementation.
    """

    def __init__(self, payment_id, amount):

        super().__init__(payment_id, amount)



    def process_payment(self):

        return (
            f"Card payment successful.\n"
            f"Payment ID: {self.get_payment_id()}\n"
            f"Amount: ₱{self.get_amount():.2f}"
        )