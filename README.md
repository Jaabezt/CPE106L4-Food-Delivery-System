# 🍔 CPE106L4 Food Delivery System

<p align="center">
  <strong>A Modular Python-Based Food Delivery & Order Management System</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Project-Collaboration-orange?style=for-the-badge" alt="Collaboration">
  <img src="https://img.shields.io/badge/Course-CPE106L4-green?style=for-the-badge" alt="CPE106L4">
</p>

<p align="center">
  Built as a collaboration activity for the <strong>BS Computer Engineering</strong> program.
</p>

---

## 👨‍💻 Developers

| Developer                  | Program                 | Role      |
| -------------------------- | ----------------------- | --------- |
| **Jabez C. Molar**         | BS Computer Engineering | Developer |
| **Edmarc Justin C. Oabel** | BS Computer Engineering | Developer |

> 🤝 This project was developed collaboratively, with both members contributing to the system's design, implementation, testing, and documentation.

---

## 📌 About the Project

The **CPE106L4 Food Delivery System** is a modular, Python-based application designed to simulate the core operations of a food delivery and order management platform.

The system organizes different responsibilities into separate modules, allowing customer management, menu operations, order processing, delivery handling, payment processing, and transaction recording to work together as one system.

### 🎯 Main Goal

To apply **Object-Oriented Programming (OOP)** and modular programming concepts in developing a functional food delivery system while practicing effective collaboration and code organization.

---

## ✨ Features

<details>
<summary>👤 <strong>Customer Management</strong></summary>

Manages customer information, profiles, and associations with their orders.

</details>

<details>
<summary>🍔 <strong>Menu & Catalog System</strong></summary>

Handles food items, categories, prices, and available dishes through the menu modules.

</details>

<details>
<summary>🛒 <strong>Order Processing</strong></summary>

Allows customers to create orders, add food items, manage carts, and calculate order information.

</details>

<details>
<summary>🚴 <strong>Delivery Handling</strong></summary>

Manages delivery assignments and tracks the status of orders during the delivery process.

</details>

<details>
<summary>💳 <strong>Payment & Transactions</strong></summary>

Processes payments, manages payment states, and records transaction information.

</details>

<details>
<summary>💾 <strong>Data Persistence</strong></summary>

Provides a dedicated data management layer for handling system records and stored information.

</details>

<details>
<summary>🆔 <strong>Automated Identification</strong></summary>

Generates unique identifiers for system records such as customers, orders, and transactions.

</details>

---

## 🔄 System Workflow

```text
              ┌─────────────────┐
              │     Customer    │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │   Browse Menu   │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │   Create Order  │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │     Payment     │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │   Transaction   │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │     Delivery   │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │  Order Complete │
              └─────────────────┘
```

---

## 📂 Project Structure

```text
CPE106L4-Food-Delivery-System/
│
├── 👤 customer.py
│   └── Customer class and account operations
│
├── 💾 data_manager.py
│   └── Data handling, storage, and persistence logic
│
├── 🚴 delivery.py
│   └── Delivery dispatching and status tracking
│
├── 🆔 id_generator.py
│   └── Unique identifier utilities
│
├── ▶️ main.py
│   └── Application entry point and runtime workflow
│
├── 🍔 menu.py
│   └── Menu item models and menu operations
│
├── 📋 menu_list.py
│   └── Static/preset catalog of food items
│
├── 🛒 order.py
│   └── Order cart creation and state handling
│
├── 💳 payment.py
│   └── Payment processing logic
│
├── 🧾 transaction.py
│   └── Transaction records and receipt generation
│
├── 🚫 .gitignore
│   └── Git ignore rules
│
├── 📄 LICENSE
│   └── Project license
│
└── 📖 README.md
    └── Project documentation
```

---

## 🧩 Module Overview

| Module            | Purpose                                          |
| ----------------- | ------------------------------------------------ |
| `customer.py`     | Handles customer profiles and account operations |
| `menu.py`         | Defines menu items and menu-related operations   |
| `menu_list.py`    | Contains the available food catalog              |
| `order.py`        | Creates and manages customer orders              |
| `payment.py`      | Handles payment processing                       |
| `transaction.py`  | Records transactions and generates receipts      |
| `delivery.py`     | Manages delivery assignments and statuses        |
| `data_manager.py` | Handles data storage and persistence             |
| `id_generator.py` | Generates unique system identifiers              |
| `main.py`         | Connects the modules and runs the application    |

---

## 🛠️ Technologies Used

* 🐍 **Python 3.8+**
* 🧱 **Object-Oriented Programming**
* 🧩 **Modular Programming**
* 📦 **Python Standard Library**
* 🔀 **Git & GitHub**
* 🤝 **Collaborative Development**

No external third-party Python dependencies are required.

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/CPE106L4-Food-Delivery-System.git
```

### 2️⃣ Navigate to the Project

```bash
cd CPE106L4-Food-Delivery-System
```

### 3️⃣ Run the Application

```bash
python main.py
```

> 💡 **Requirement:** Python **3.8 or later** should be installed on your computer.

---

## 🍽️ Usage Workflow

### Step 1 — Browse the Menu

Food items and their corresponding information are provided through:

```text
menu.py
menu_list.py
```

### Step 2 — Select or Register a Customer

Customer information is managed using:

```text
customer.py
```

### Step 3 — Create an Order

Customers can select food items and build their order through:

```text
order.py
```

### Step 4 — Checkout & Payment

The system calculates the order total and processes the selected payment through:

```text
payment.py
```

### Step 5 — Record the Transaction

Transaction information and receipts are handled by:

```text
transaction.py
```

### Step 6 — Process Delivery

The delivery module handles the assignment and tracking of the order:

```text
delivery.py
```

---

## 🧠 OOP Concepts Applied

The system was designed to demonstrate important **Object-Oriented Programming** concepts:

| Concept           | Application                                                         |
| ----------------- | ------------------------------------------------------------------- |
| **Encapsulation** | Organizing related data and behavior inside classes                 |
| **Abstraction**   | Hiding unnecessary implementation details                           |
| **Inheritance**   | Allowing related classes to reuse common behavior where applicable  |
| **Polymorphism**  | Allowing objects to interact through shared interfaces or behaviors |
| **Modularity**    | Separating system responsibilities into independent Python modules  |

This structure helps make the application easier to understand, maintain, test, and extend.

---

## 🤝 Collaboration

This project is a **collaboration activity** completed by two BS Computer Engineering students.

To coordinate development effectively, the project can be divided into separate branches so both developers can work on different components without interfering with each other's changes.

```text
                    main
                     │
             ┌───────┴───────┐
             │               │
        person-a          person-b
             │               │
       Assigned Parts    Assigned Parts
             │               │
             └───────┬───────┘
                     │
                 Merge / Test
                     │
                     ▼
                   main
```

### 🔀 Collaboration Approach

* Each developer works on an assigned set of modules.
* Separate Git branches are used to organize individual work.
* Changes are tested before being merged.
* Both developers coordinate module dependencies and integration.
* The completed modules are combined into the main application.

This approach allows the team to **divide tasks efficiently while maintaining a consistent and functional system**.

---

## 📈 Future Improvements

Potential improvements for future versions include:

* [ ] Add a graphical user interface
* [ ] Add more payment options
* [ ] Implement user authentication
* [ ] Add order history
* [ ] Improve delivery tracking
* [ ] Add discounts and promotional codes
* [ ] Connect the system to a database
* [ ] Add automated testing
* [ ] Improve error handling and validation

---

## 📚 Academic Context

**Course:** CPE106L4
**Program:** Bachelor of Science in Computer Engineering
**Activity:** Collaboration Activity

### 👥 Members

**Jabez C. Molar**
BS Computer Engineering

**Edmarc Justin C. Oabel**
BS Computer Engineering

---

## 📜 License

This project is licensed under the terms specified in the repository's [`LICENSE`](LICENSE) file.

---

<p align="center">
  Made with 🐍 Python and 🤝 collaboration
</p>

<p align="center">
  <strong>CPE106L4 • Food Delivery System</strong>
</p>
