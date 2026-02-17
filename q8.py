# Team Name :Techstorm


def sanitize_email(raw_input: str) -> str:
    """
    Clean an email string and validate basic structure.

    Args:
        raw_input: A string containing a potential email address.

    Returns:
        The cleaned lowercase email or "Invalid Email".
    """
    # Chain string methods to strip whitespace and convert to lowercase
    cleaned_email = raw_input.strip().lower()
    
    # Check if exactly one '@' symbol exists in the cleaned string
    if cleaned_email.count('@') == 1:
        return cleaned_email
        
    return "Invalid Email"
