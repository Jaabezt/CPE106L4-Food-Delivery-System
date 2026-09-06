def generate_id(prefix, existing_ids):
    """
    Generates the next unique ID using a prefix and existing IDs.
    """

    highest_number = 0

    for item_id in existing_ids:

        item_id = str(item_id)

        # Only process IDs that use the requested prefix
        if item_id.startswith(prefix):

            number_part = item_id[len(prefix):]

            if number_part.isdigit():

                number = int(number_part)

                if number > highest_number:
                    highest_number = number

    next_number = highest_number + 1

    return f"{prefix}{next_number:03d}"