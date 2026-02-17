# Team Name :Techstorm


def sanitize_email(raw_input: str) -> str:
    """
    Clean an email string and validate basic structure.
    """

    cleaned = raw_input.strip().lower()

    if cleaned == "":
        return "Invalid Email"

    if cleaned.count("@") != 1:
        return "Invalid Email"

    return cleaned
