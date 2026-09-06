from menu import Menu, MenuItem

def create_cafe_menu():

    menu = Menu()


    # ==========================
    # COFFEE
    # ==========================

    coffee_items = [

        ("COF001", "Americano", 120.00, "Coffee"),
        ("COF002", "Cafe Latte", 150.00, "Coffee"),
        ("COF003", "Cappuccino", 160.00, "Coffee"),
        ("COF004", "Caramel Macchiato", 180.00, "Coffee"),
        ("COF005", "Spanish Latte", 170.00, "Coffee"),
        ("COF006", "Mocha Latte", 175.00, "Coffee"),
        ("COF007", "Vanilla Latte", 170.00, "Coffee")

    ]



    # ==========================
    # NON COFFEE
    # ==========================

    non_coffee_items = [

        ("DRK001", "Chocolate Frappe", 190.00, "Non-Coffee"),
        ("DRK002", "Matcha Latte", 180.00, "Non-Coffee"),
        ("DRK003", "Strawberry Milk", 160.00, "Non-Coffee"),
        ("DRK004", "Cookies and Cream Frappe", 200.00, "Non-Coffee"),
        ("DRK005", "Iced Lemon Tea", 130.00, "Non-Coffee"),
        ("DRK006", "Blueberry Yakult", 150.00, "Non-Coffee")

    ]



    # ==========================
    # MAIN MEALS
    # ==========================

    main_meals = [

        ("ML001", "Creamy Carbonara", 220.00, "Main Meal"),
        ("ML002", "Chicken Alfredo Pasta", 240.00, "Main Meal"),
        ("ML003", "Chicken Rice Bowl", 190.00, "Main Meal"),
        ("ML004", "Beef Teriyaki Bowl", 250.00, "Main Meal"),
        ("ML005", "Garlic Chicken Rice", 200.00, "Main Meal"),
        ("ML006", "Seafood Pasta", 260.00, "Main Meal")

    ]



    # ==========================
    # SNACKS
    # ==========================

    snacks = [

        ("SNK001", "Clubhouse Sandwich", 210.00, "Snack"),
        ("SNK002", "Tuna Sandwich", 180.00, "Snack"),
        ("SNK003", "French Toast", 150.00, "Snack"),
        ("SNK004", "Ham and Cheese Sandwich", 190.00, "Snack"),
        ("SNK005", "Chicken Wrap", 200.00, "Snack")

    ]



    # ==========================
    # SIDES
    # ==========================

    sides = [

        ("SID001", "French Fries", 90.00, "Side"),
        ("SID002", "Potato Wedges", 140.00, "Side"),
        ("SID003", "Mozzarella Sticks", 160.00, "Side"),
        ("SID004", "Onion Rings", 120.00, "Side"),
        ("SID005", "Nachos", 170.00, "Side")

    ]



    # Combine all menu items

    all_items = (
        coffee_items +
        non_coffee_items +
        main_meals +
        snacks +
        sides
    )



    # Convert data into MenuItem objects

    for item_id, name, price, category in all_items:

        menu.add_item(
            MenuItem(
                item_id,
                name,
                price,
                category
            )
        )


    return menu