# Team Name :Techstorm


def average_passing_grades(grades: list[int]) -> float:
    """
    Calculate the average of grades that are 50 or higher.
    """

    total = 0
    count = 0

    for g in grades:
        if g >= 50:
            total += g
            count += 1

    if count == 0:
        return 0.0

    return float(total / count)
