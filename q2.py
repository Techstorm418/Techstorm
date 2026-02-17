# Team Name: Techstorm

def convert_seconds(total_seconds: int) -> str:
    """
    Convert total seconds into minutes and remaining seconds.

    Args:
        total_seconds: An integer representing time in seconds.

    Returns:
        A string formatted as "Xm Ys".
    """
    # Calculate full minutes using integer division
    minutes = total_seconds // 60
    
    # Calculate remaining seconds using modulo
    seconds = total_seconds % 60
    
    # Return cleanly formatted string using an f-string
    return f"{minutes}m {seconds}s"
