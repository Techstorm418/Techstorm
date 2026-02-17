# Team Name: Techstorm
def calculate(expression: str) -> float:
    """
    Evaluate mathematical expression without using eval().
    
    Args:
        expression: Mathematical expression as string
        
    Returns:
        Result rounded to 2 decimal places
    """
    # Strip spaces to make string parsing perfectly predictable
    s = expression.replace(" ", "")
    stack = []
    
    i = 0
    operator = '+'  # Default operator for the very first number
    
    while i < len(s):
        # 1. Identify and update the active operator
        if s[i] in "+-*/":
            # Guard against unary minus (e.g., the '-' in "10 * -5" or starting "-5 + 2")
            if s[i] == '-' and (i == 0 or s[i-1] in "+-*/"):
                pass # Let the number extractor below handle this negative sign
            else:
                operator = s[i]
                i += 1
                continue
                
        # 2. Extract the full number block (handling negatives and potential decimals)
        start = i
        if s[i] == '-':  # Step past the unary minus if it exists
            i += 1
            
        while i < len(s) and (s[i].isdigit() or s[i] == '.'):
            i += 1
            
        current_num = float(s[start:i])
        
        # 3. Apply the math following the Order of Operations
        if operator == '+':
            stack.append(current_num)
        elif operator == '-':
            stack.append(-current_num)
        elif operator == '*':
            stack[-1] = stack[-1] * current_num
        elif operator == '/':
            stack[-1] = stack[-1] / current_num
            
    # 4. Summing the stack safely processes all remaining additions and subtractions
    return round(sum(stack), 2)

# --- Validating against your Test Cases ---
if __name__ == "__main__":
    assert calculate("2 + 3") == 5.0
    assert calculate("10-5 * 2") == 0.0
    assert calculate("20 / 4 + 3 * 2") == 11.0
    assert calculate("100 / 3") == 33.33
    assert calculate("5") == 5.0
