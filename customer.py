class Customer:
    def __init__(self, customer_id, name, address, phone):
        self.__customer_id = customer_id
        self.__name = name
        self.__address = address
        self.__phone = phone

    def get_customer_id(self):
        return self.__customer_id

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    def update_information(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def display_customer(self):
        print(f"Customer ID: {self.__customer_id}")
        print(f"Name: {self.__name}")
        print(f"Address: {self.__address}")
        print(f"Phone: {self.__phone}")
