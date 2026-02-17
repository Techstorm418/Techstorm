# Team Name: Techstorm


def calculate(expression: str) -> float:
    expression = expression.replace(" ", "")
    
    stack = []
    num = 0
    sign = '+'
    i = 0
    
    while i < len(expression):
        ch = expression[i]
        
        # Build number (handles decimals also)
        if ch.isdigit() or ch == '.':
            num_str = ""
            while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                num_str += expression[i]
                i += 1
            num = float(num_str)
            continue
        
        # If operator found
        if ch in "+-*/":
            
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack[-1] = stack[-1] * num
            elif sign == '/':
                stack[-1] = stack[-1] / num
            
            sign = ch
            num = 0
        
        i += 1
    
    # Process last number
    if sign == '+':
        stack.append(num)
    elif sign == '-':
        stack.append(-num)
    elif sign == '*':
        stack[-1] = stack[-1] * num
    elif sign == '/':
        stack[-1] = stack[-1] / num
    
    return round(sum(stack), 2)
