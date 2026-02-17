# Team Name : Techstorm


def count_inventory(fruit_list: list[str]) -> dict[str, int]:
    """
    Create a frequency dictionary from a list of fruits.
    """

    inventory = {}

    for fruit in fruit_list:
        inventory[fruit] = inventory.get(fruit, 0) + 1

    return inventory
