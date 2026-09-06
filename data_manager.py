import json
import os

from customer import Customer
from order import Order
from payment import CashPayment, CardPayment
from delivery import Delivery
from transaction import Transaction


DATA_FILE = "data.json"


def save_data(customers, transactions):
    """
    Saves customers, orders, payments, deliveries,
    and completed transactions to a JSON file.
    """

    data = {
        "customers": {},
        "transactions": {}
    }

    # ==========================
    # SAVE CUSTOMERS
    # ==========================

    for customer_id, customer in customers.items():

        data["customers"][customer_id] = {
            "name": customer.get_name(),
            "address": customer.get_address(),
            "phone": customer.get_phone()
        }

    # ==========================
    # SAVE TRANSACTIONS / ORDERS
    # ==========================

    for order_id, record in transactions.items():

        order = record["order"]
        payment = record["payment"]
        delivery = record["delivery"]
        transaction = record["transaction"]

        order_data = {
            "order_id": order.get_order_id(),
            "customer_id": order.get_customer().get_customer_id(),
            "status": order.get_status(),
            "items": []
        }

        # Save order items
        for order_item in order.get_items():

            menu_item = order_item.get_menu_item()

            order_data["items"].append({
                "item_id": menu_item.get_item_id(),
                "quantity": order_item.get_quantity()
            })

        record_data = {
            "order": order_data,
            "payment": None,
            "delivery": None,
            "transaction": None
        }

        # ==========================
        # SAVE PAYMENT
        # ==========================

        if payment is not None:

            payment_type = "Cash"

            if isinstance(payment, CardPayment):
                payment_type = "Card"

            record_data["payment"] = {
                "payment_id": payment.get_payment_id(),
                "amount": payment.get_amount(),
                "type": payment_type
            }

        # ==========================
        # SAVE DELIVERY
        # ==========================

        if delivery is not None:

            record_data["delivery"] = {
                "delivery_id": delivery.get_delivery_id(),
                "order_id": delivery.get_order_id(),
                "address": delivery.get_address(),
                "status": delivery.get_status()
            }

        # ==========================
        # SAVE TRANSACTION
        # ==========================

        if transaction is not None:

            record_data["transaction"] = {
                "transaction_id": transaction.get_transaction_id()
            }

        data["transactions"][order_id] = record_data

    # ==========================
    # WRITE JSON FILE
    # ==========================

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print("\nData saved successfully.")


def load_data(menu):
    """
    Loads customers and transactions from the JSON file.
    Reconstructs the required Python objects.
    """

    customers = {}
    transactions = {}

    if not os.path.exists(DATA_FILE):
        return customers, transactions

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

    except (json.JSONDecodeError, OSError):
        print("\nWarning: Could not load data.json.")
        return customers, transactions

    # ==========================
    # LOAD CUSTOMERS
    # ==========================

    for customer_id, info in data.get("customers", {}).items():

        customer = Customer(
            customer_id,
            info["name"],
            info["address"],
            info["phone"]
        )

        customers[customer_id] = customer

    # ==========================
    # LOAD TRANSACTIONS / ORDERS
    # ==========================

    for order_id, record in data.get("transactions", {}).items():

        order_data = record["order"]

        customer_id = order_data["customer_id"]

        # Make sure referenced customer exists
        if customer_id not in customers:
            continue

        customer = customers[customer_id]

        order = Order(
            order_data["order_id"],
            customer
        )

        # Restore order status
        order.update_status(
            order_data.get("status", "Pending")
        )

        # Restore order items
        for item_data in order_data.get("items", []):

            menu_item = menu.find_item(
                item_data["item_id"]
            )

            if menu_item is not None:

                order.add_item(
                    menu_item,
                    item_data["quantity"]
                )

        # ==========================
        # LOAD PAYMENT
        # ==========================

        payment = None

        payment_data = record.get("payment")

        if payment_data is not None:

            if payment_data["type"] == "Card":

                payment = CardPayment(
                    payment_data["payment_id"],
                    payment_data["amount"]
                )

            else:

                payment = CashPayment(
                    payment_data["payment_id"],
                    payment_data["amount"]
                )

        # ==========================
        # LOAD DELIVERY
        # ==========================

        delivery = None

        delivery_data = record.get("delivery")

        if delivery_data is not None:

            delivery = Delivery(
                delivery_data["delivery_id"],
                delivery_data["order_id"],
                delivery_data["address"]
            )

            delivery.update_status(
                delivery_data.get("status", "Preparing")
            )

        # ==========================
        # LOAD TRANSACTION
        # ==========================

        transaction = None

        transaction_data = record.get("transaction")

        if transaction_data is not None:

            transaction = Transaction(
                transaction_data["transaction_id"],
                order,
                payment,
                delivery
            )

        transactions[order_id] = {
            "order": order,
            "payment": payment,
            "delivery": delivery,
            "transaction": transaction
        }

    return customers, transactions