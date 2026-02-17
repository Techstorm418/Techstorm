# Team Name :Techstorm


def get_ticket_price(age: int, is_student: bool) -> int:
    """
    Determine ticket price based on age and student status.

    Args:
        age: Integer representing the person’s age.
        is_student: Boolean indicating if the person is a student.

    Returns:
        The ticket price as an integer.
    """

    # Children
    if age < 12:
        return 8

    # Seniors
    if age >= 65:
        return 10

    # Adults (12–64)
    if is_student:
        return 12
    else:
        return 15
