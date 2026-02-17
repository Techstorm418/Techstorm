# Team Name :Techstorm


def average_passing_grades(grades: list[int]) -> float:
    """
    Calculate the average of grades that are 50 or higher.
    
    Args:
        grades: A list of integers representing scores.
        
    Returns:
        The average of passing grades as a float, or 0.0 if none exist.
    """
    passing_sum = 0
    passing_count = 0
    
    # Iterate exactly once (O(N) time complexity)
    for grade in grades:
        if grade >= 50:
            passing_sum += grade
            passing_count += 1
            
    # Edge case: Avoid division by zero if no passing grades exist
    if passing_count == 0:
        return 0.0
        
    # Return the exact float average
    return float(passing_sum / passing_count)
