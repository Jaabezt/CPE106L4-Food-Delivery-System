import json
import os

from customer import Customer
from order import Order
from payment import CashPayment, CardPayment
from delivery import Delivery
from transaction import Transaction
from menu import MenuItem


DATA_FILE = "data.json"


def save_data(customers, transactions, menu):

    data = {
        "customers": [],
        "menu_items": [],
        "transactions": []
    }

    # Save customers
    for customer in customers.values():

        data["customers"].append({
            "customer_id": customer.get_customer_id(),
            "name": customer.get_name(),
            "address": customer.get_address(),
            "phone": customer.get_phone()
        })

    # Save menu items
    for item in menu.get_items():

        data["menu_items"].append({
            "item_id": item.get_item_id(),
            "name": item.get_name(),
            "price": item.get_price(),
            "category": item.get_category()
        })

    # Save transactions
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

        for order_item in order.get_items():

            menu_item = order_item.get_menu_item()

            order_data["items"].append({
                "item_id": menu_item.get_item_id(),
                "quantity": order_item.get_quantity()
            })

        payment_data = None

        if payment is not None:

            payment_type = "Cash"

            if isinstance(payment, CardPayment):
                payment_type = "Card"

            payment_data = {
                "payment_id": payment.get_payment_id(),
                "amount": payment.get_amount(),
                "type": payment_type
            }

        delivery_data = None

        if delivery is not None:

            delivery_data = {
                "delivery_id": delivery.get_delivery_id(),
                "order_id": delivery.get_order_id(),
                "address": delivery.get_address(),
                "status": delivery.get_status()
            }

        transaction_data = None

        if transaction is not None:

            transaction_data = {
                "transaction_id": transaction.get_transaction_id()
            }

        data["transactions"].append({
            "order": order_data,
            "payment": payment_data,
            "delivery": delivery_data,
            "transaction": transaction_data
        })

    with open(DATA_FILE, "w", encoding="utf-8") as file:

        json.dump(
            data,
            file,
            indent=4
        )


def load_data(menu):

    if not os.path.exists(DATA_FILE):

        return {}, {}

    with open(
        DATA_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)

    customers = {}
    transactions = {}

    # Load customers
    for customer_data in data.get("customers", []):

        customer = Customer(
            customer_data["customer_id"],
            customer_data["name"],
            customer_data["address"],
            customer_data["phone"]
        )

        customers[
            customer.get_customer_id()
        ] = customer

    # Load menu items
    saved_menu_items = data.get("menu_items", [])

    for item_data in saved_menu_items:

        # Avoid duplicate items
        if menu.find_item(item_data["item_id"]) is None:

            menu.add_item(
                MenuItem(
                    item_data["item_id"],
                    item_data["name"],
                    item_data["price"],
                    item_data["category"]
                )
            )

    # Load transactions
    for record_data in data.get("transactions", []):

        order_data = record_data["order"]

        customer_id = order_data["customer_id"]

        if customer_id not in customers:
            continue

        customer = customers[customer_id]

        order = Order(
            order_data["order_id"],
            customer
        )

        order.update_status(
            order_data["status"]
        )

        for item_data in order_data["items"]:

            menu_item = menu.find_item(
                item_data["item_id"]
            )

            if menu_item is not None:

                order.add_item(
                    menu_item,
                    item_data["quantity"]
                )

        payment = None

        payment_data = record_data["payment"]

        if payment_data is not None:

            if payment_data["type"] == "Cash":

                payment = CashPayment(
                    payment_data["payment_id"],
                    payment_data["amount"]
                )

            else:

                payment = CardPayment(
                    payment_data["payment_id"],
                    payment_data["amount"]
                )

        delivery = None

        delivery_data = record_data["delivery"]

        if delivery_data is not None:

            delivery = Delivery(
                delivery_data["delivery_id"],
                delivery_data["order_id"],
                delivery_data["address"]
            )

            delivery.update_status(
                delivery_data["status"]
            )

        transaction = None

        transaction_data = record_data["transaction"]

        if transaction_data is not None:

            transaction = Transaction(
                transaction_data["transaction_id"],
                order,
                payment,
                delivery
            )

        transactions[
            order.get_order_id()
        ] = {
            "order": order,
            "payment": payment,
            "delivery": delivery,
            "transaction": transaction
        }

    return customers, transactions