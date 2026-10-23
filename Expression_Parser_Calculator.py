
def tokenize(user_input):
    tokens = []
    number = ""

    for char in user_input:
        if char.isspace():
            continue

        if char.isdigit():
            number = number + char

        else:
            if number:
                tokens.append(int(number))
                number = ""

            if char in "+-*/()":
                tokens.append(char)
            else:
                raise ValueError("Invalid character: " + char)

    if number:
        tokens.append(int(number))

    return tokens


def factor(tokens, position):
    token = tokens[position]

    if isinstance(token, int):
        return token, position + 1

    if token == "(":
        result, position = expression(tokens, position + 1)

        if position >= len(tokens) or tokens[position] != ")":
            raise ValueError("Missing closing parenthesis")

        return result, position + 1

    raise ValueError("Expected a number or opening parenthesis")





def term(tokens, position):
    result, position = factor(tokens, position)

    while position < len(tokens) and tokens[position] in ("*", "/"):
        operator = tokens[position]
        position += 1

        value, position = factor(tokens, position)

        if operator == "*":
            result = result * value
        else:
            if value == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = result / value

    return result, position



def expression(tokens, position):
    result, position = term(tokens, position)

    while position < len(tokens) and tokens[position] in ("+", "-"):
        operator = tokens[position]
        position += 1

        value, position = term(tokens, position)

        if operator == "+":
            result = result + value
        else:
            result = result - value

    return result, position
    

def calculate(tokens):
    result, position = expression(tokens, 0)

    if position != len(tokens):
        raise ValueError("Invalid expression")

    return result




user_input = input("Enter expression: ")

try:
    tokens = tokenize(user_input)
    print("Tokens:", tokens)
    print("Result:", calculate(tokens))

except (ValueError, ZeroDivisionError, IndexError, TypeError) as error:
    print("Error:", error)
 

