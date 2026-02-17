# Team Name : Techstorm
def count_inventory(fruit_list: list[str]) -> dict[str, int]:
    """
    Create a frequency dictionary from a list of fruits.

    Args:
        fruit_list: A list of strings.

    Returns:
        A dictionary with fruit names as keys and counts as values.
    """
    inventory = {}
    
    # Iterate through each fruit in the list
    for fruit in fruit_list:
        # .get() fetches the current count, or 0 if it's the first time seeing this fruit
        inventory[fruit] = inventory.get(fruit, 0) + 1
        
    return inventory
