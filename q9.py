# Team Name: Techstorm


def generate_threes(start: int, end: int) -> list[int]:
    """
    Generate a list of numbers from start to end, skipping by 3.
    """

    if start >= end:
        return []

    return list(range(start, end, 3))
