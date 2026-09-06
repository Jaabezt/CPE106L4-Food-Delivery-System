def generate_id(prefix, existing_ids):
    """
    Generates the next unique ID using a prefix and existing IDs.

    Example:
        CUST001, CUST002 → CUST003
    """

    if not existing_ids:
        return f"{prefix}001"

    numbers = []

    for item_id in existing_ids:
        number = int(item_id.replace(prefix, ""))
        numbers.append(number)

    next_number = max(numbers) + 1

    return f"{prefix}{next_number:03d}"