# Team Name: Techstorm

def calculate(expression: str) -> float:
    """
    Evaluate mathematical expression without using eval().
    """

    s = expression.replace(" ", "")
    stack = []
    
    i = 0
    operator = '+'
    
    while i < len(s):
        if s[i] in "+-*/":
            if s[i] == '-' and (i == 0 or s[i-1] in "+-*/"):
                pass
            else:
                operator = s[i]
                i += 1
                continue
                
        start = i
        if s[i] == '-':
            i += 1
            
        while i < len(s) and (s[i].isdigit() or s[i] == '.'):
            i += 1
            
        current_num = float(s[start:i])
        
        if operator == '+':
            stack.append(current_num)
        elif operator == '-':
            stack.append(-current_num)
        elif operator == '*':
            stack[-1] *= current_num
        elif operator == '/':
            stack[-1] /= current_num
            
    return round(sum(stack), 2)
