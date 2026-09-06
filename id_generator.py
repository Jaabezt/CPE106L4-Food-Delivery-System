def generate_id(prefix, existing_ids):
    """
    Generates the next ID for a specific category.
    
    """

    highest_number = 0

    for item_id in existing_ids:

        item_id = str(item_id)

        if item_id.startswith(prefix):

            number_part = item_id[len(prefix):]

            if number_part.isdigit():

                number = int(number_part)

                if number > highest_number:
                    highest_number = number

    return f"{prefix}{highest_number + 1:03d}"