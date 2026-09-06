from customer import Customer
from id_generator import generate_id
from menu import MenuItem
from menu_list import create_cafe_menu
from order import Order
from payment import CashPayment, CardPayment
from delivery import Delivery
from transaction import Transaction
from data_manager import save_data, load_data


customers = {}
transactions = {}

cafe_menu = create_cafe_menu()


def customer_management():

    while True:

        print("\n========== CUSTOMER MANAGEMENT ==========")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Update Customer")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == "1":

            customer_id = generate_id(
                "CUST",
                customers.keys()
            )

            name = input("Enter Name: ")
            address = input("Enter Address: ")
            phone = input("Enter Phone: ")

            customer = Customer(
                customer_id,
                name,
                address,
                phone
            )

            customers[customer_id] = customer

            save_data(
                customers,
                transactions,
                cafe_menu
            )

            print("\nCustomer added successfully!")
            print(f"Customer ID: {customer_id}")

        elif choice == "2":

            if not customers:

                print("\nNo customers found.")

            else:

                print("\n========== CUSTOMERS ==========")

                for customer in customers.values():

                    customer.display_customer()

                print("===============================")

        elif choice == "3":

            customer_id = input(
                "Enter Customer ID: "
            )

            if customer_id in customers:

                name = input("Enter New Name: ")
                address = input("Enter New Address: ")
                phone = input("Enter New Phone: ")

                customers[customer_id].update_information(
                    name,
                    address,
                    phone
                )

                save_data(
                    customers,
                    transactions,
                    cafe_menu
                )

                print("\nCustomer updated successfully!")

            else:

                print("\nCustomer not found.")

        elif choice == "4":

            break

        else:

            print("\nInvalid choice.")


def menu_management():

    while True:

        print("\n========== MENU MANAGEMENT ==========")
        print("1. Display Menu")
        print("2. Add Menu Item")
        print("3. Remove Menu Item")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == "1":

            cafe_menu.display_menu()

        elif choice == "2":

            name = input("Enter Item Name: ")

            try:

                price = float(
                    input("Enter Price: ")
                )

            except ValueError:

                print("\nInvalid price.")
                continue

            print("\nSelect Category:")
            print("1. Coffee")
            print("2. Non-Coffee")
            print("3. Main Meal")
            print("4. Snack")
            print("5. Side")

            category_choice = input(
                "Enter your choice: "
            )

            categories = {
                "1": ("Coffee", "COF"),
                "2": ("Non-Coffee", "DRK"),
                "3": ("Main Meal", "ML"),
                "4": ("Snack", "SNK"),
                "5": ("Side", "SID")
            }

            if category_choice not in categories:

                print("\nInvalid category.")
                continue

            category, prefix = categories[
                category_choice
            ]

            existing_item_ids = [
                item.get_item_id()
                for item in cafe_menu.get_items()
            ]

            item_id = generate_id(
                prefix,
                existing_item_ids
            )

            item = MenuItem(
                item_id,
                name,
                price,
                category
            )

            cafe_menu.add_item(item)

            print("\nMenu item added successfully!")
            print(f"Item ID: {item_id}")
            print(f"Category: {category}")

        elif choice == "3":

            item_id = input(
                "Enter Item ID to remove: "
            )

            if cafe_menu.remove_item(item_id):

                print(
                    "\nMenu item removed successfully!"
                )

            else:

                print("\nMenu item not found.")

        elif choice == "4":

            break

        else:

            print("\nInvalid choice.")


def create_food_order():

    print("\n========== CREATE FOOD ORDER ==========")

    if not customers:

        print("No customers registered.")
        print("Please add a customer first.")

        return

    customer_id = input(
        "Enter Customer ID: "
    )

    if customer_id not in customers:

        print("\nCustomer not found.")

        return

    order_id = generate_id(
        "ORD",
        transactions.keys()
    )

    customer = customers[customer_id]

    order = Order(
        order_id,
        customer
    )

    while True:

        cafe_menu.display_menu()

        item_id = input(
            "Enter Item ID to add "
            "(or type DONE to finish): "
        )

        if item_id.upper() == "DONE":

            break

        menu_item = cafe_menu.find_item(
            item_id
        )

        if menu_item is None:

            print("\nMenu item not found.")

            continue

        try:

            quantity = int(
                input("Enter Quantity: ")
            )

            if quantity <= 0:

                print(
                    "\nQuantity must be greater than zero."
                )

                continue

        except ValueError:

            print(
                "\nPlease enter a valid quantity."
            )

            continue

        order.add_item(
            menu_item,
            quantity
        )

        print(
            f"\n{menu_item.get_name()} "
            f"added to order."
        )

    if not order.get_items():

        print(
            "\nNo items were added. "
            "Order cancelled."
        )

        return

    order.display_order()

    confirm = input(
        "Confirm this order? (Y/N): "
    )

    if confirm.upper() == "Y":

        order.update_status(
            "Confirmed"
        )

        transactions[order_id] = {
            "order": order,
            "payment": None,
            "delivery": None,
            "transaction": None
        }

        save_data(
            customers,
            transactions,
            cafe_menu
        )

        print("\nOrder confirmed!")
        print(f"Order ID: {order_id}")

    else:

        print("\nOrder cancelled.")


def process_payment():

    print("\n========== PROCESS PAYMENT ==========")

    if not transactions:

        print("No orders available.")

        return

    order_id = input(
        "Enter Order ID: "
    )

    if order_id not in transactions:

        print("\nOrder not found.")

        return

    record = transactions[order_id]

    if record["payment"] is not None:

        print(
            "\nPayment has already been processed."
        )

        return

    order = record["order"]

    amount = order.calculate_total()

    print(
        f"\nAmount to pay: ₱{amount:.2f}"
    )

    print("\n1. Cash")
    print("2. Card")

    choice = input(
        "Select payment method: "
    )

    if choice not in ("1", "2"):

        print("\nInvalid payment method.")

        return

    payment_ids = []

    for record_item in transactions.values():

        payment = record_item["payment"]

        if payment is not None:

            payment_ids.append(
                payment.get_payment_id()
            )

    payment_id = generate_id(
        "PAY",
        payment_ids
    )

    if choice == "1":

        payment = CashPayment(
            payment_id,
            amount
        )

    else:

        payment = CardPayment(
            payment_id,
            amount
        )

    print(
        "\n" + payment.process_payment()
    )

    record["payment"] = payment

    order.update_status(
        "Preparing"
    )

    save_data(
        customers,
        transactions,
        cafe_menu
    )

    print(
        "\nPayment processed successfully!"
    )

    print(
        f"Payment ID: {payment_id}"
    )


def track_delivery():

    print("\n========== TRACK DELIVERY ==========")

    if not transactions:

        print("No orders available.")

        return

    order_id = input(
        "Enter Order ID: "
    )

    if order_id not in transactions:

        print("\nOrder not found.")

        return

    record = transactions[order_id]

    order = record["order"]
    payment = record["payment"]

    if payment is None:

        print(
            "\nPayment has not been processed yet."
        )

        return

    delivery = record["delivery"]

    if delivery is None:

        delivery_ids = []

        for record_item in transactions.values():

            existing_delivery = (
                record_item["delivery"]
            )

            if existing_delivery is not None:

                delivery_ids.append(
                    existing_delivery.get_delivery_id()
                )

        delivery_id = generate_id(
            "DEL",
            delivery_ids
        )

        delivery = Delivery(
            delivery_id,
            order.get_order_id(),
            order.get_customer().get_address()
        )

        record["delivery"] = delivery

        save_data(
            customers,
            transactions,
            cafe_menu
        )

        print("\nDelivery created!")
        print(f"Delivery ID: {delivery_id}")

    while True:

        delivery.display_delivery()

        print("1. Out for Delivery")
        print("2. Delivered")
        print("3. Back")

        choice = input(
            "Enter your choice: "
        )

        if choice == "1":

            delivery.update_status(
                "Out for Delivery"
            )

            order.update_status(
                "Out for Delivery"
            )

            save_data(
                customers,
                transactions,
                cafe_menu
            )

            print(
                "\nDelivery status updated."
            )

        elif choice == "2":

            delivery.update_status(
                "Delivered"
            )

            order.update_status(
                "Delivered"
            )

            save_data(
                customers,
                transactions,
                cafe_menu
            )

            complete_transactions()

            print("\nOrder delivered!")

            break

        elif choice == "3":

            break

        else:

            print("\nInvalid choice.")


def complete_transactions():

    transaction_ids = []

    for record in transactions.values():

        transaction = record["transaction"]

        if transaction is not None:

            transaction_ids.append(
                transaction.get_transaction_id()
            )

    for order_id, record in transactions.items():

        order = record["order"]
        payment = record["payment"]
        delivery = record["delivery"]

        if (
            payment is not None
            and delivery is not None
            and delivery.get_status() == "Delivered"
            and record["transaction"] is None
        ):

            transaction_id = generate_id(
                "TXN",
                transaction_ids
            )

            transaction = Transaction(
                transaction_id,
                order,
                payment,
                delivery
            )

            record["transaction"] = transaction

            transaction_ids.append(
                transaction_id
            )

    save_data(
        customers,
        transactions, 
        cafe_menu
    )


def view_completed_transactions():

    print(
        "\n========== COMPLETED TRANSACTIONS =========="
    )

    complete_transactions()

    found = False

    for record in transactions.values():

        transaction = record["transaction"]

        if transaction is not None:

            transaction.display_transaction()

            found = True

    if not found:

        print(
            "No completed transactions found."
        )

    print(
        "============================================"
    )


def main():

    global customers
    global transactions

    customers, transactions = load_data(
        cafe_menu
    )

    print("\nData loaded successfully.")

    while True:

        complete_transactions()

        print("\n")
        print("========================================")
        print("          CAFE FOOD DELIVERIES          ")
        print("========================================")
        print("1. Customer Management")
        print("2. Menu Management")
        print("3. Create Food Order")
        print("4. Process Payment")
        print("5. Track Delivery")
        print("6. View Completed Transactions")
        print("7. Exit")
        print("========================================")

        choice = input(
            "Enter your choice: "
        )

        if choice == "1":

            customer_management()

        elif choice == "2":

            menu_management()

        elif choice == "3":

            create_food_order()

        elif choice == "4":

            process_payment()

        elif choice == "5":

            track_delivery()

        elif choice == "6":

            view_completed_transactions()

        elif choice == "7":

            save_data(
                customers,
                transactions,
                cafe_menu
            )

            print(
                "\nThank you for using "
                "the Cafe Food Deliveries!"
            )

            break

        else:

            print(
                "\nInvalid choice. Please try again."
            )


if __name__ == "__main__":
    main()