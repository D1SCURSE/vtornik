def evaluate_rpn(expression):
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):  
            stack.append(int(token))
        else:
            b = stack.pop() 
            a = stack.pop() 

            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            else:
                raise ValueError(f"Unknown operator: {token}")

    return stack.pop() 


if __name__ == "__main__":
    import sys

    input_expression = sys.stdin.read().strip()  
    result = evaluate_rpn(input_expression)
    print(result)
