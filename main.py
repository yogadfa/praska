import operator

#var global
ops = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul
}
variabel = {}

def tokenize(source):
    tokens = []
    op = ["+", "-", "/", "*", "="]
    boolean = ["<", ">", "==", "!=", ">=", "<=", "!"]
    i = 0
    
    while i < len(source):
        char = source[i]
        
        if char.isdigit():
            start = i
            while i < len(source) and source[i].isdigit():
                i += 1
            num = source[start:i]
            tokens.append(("NUMBER", int(num)))
            continue
            
        elif char.isalpha():
            start = i
            while i < len(source) and source[i].isalpha():
                i += 1
            var_str = source[start:i]
            tokens.append(("IDENTIFIER", var_str))
            continue
            
        elif char == " ":
            pass
            
        elif char in op or char in boolean:
            char_str = source[i]
            
            if char_str == "==":
                tokens.append(("EQUALEQUAL", "=="))
            elif char_str == "!=":
                tokens.append(("NOTEQUALS", "!="))
            elif char_str == "<=":
                tokens.append(("LESSEQUAL", "<="))
            elif char_str == ">=":
                tokens.append(("GREATEREQUAL", ">="))
            elif char_str == "+":
                tokens.append(("PLUS", "+"))
            elif char_str == "*":
                tokens.append(("TIMES", "*"))
            elif char_str == "/":
                tokens.append(("DIVIDE", "/"))
            elif char_str == ">":
                tokens.append(("GREATERTHAN", ">"))
            elif char_str == "<":
                tokens.append(("LESSTHAN", "<"))
            elif char_str == "-":
                tokens.append(("MINUS", "-"))
            elif char_str == "!":
                tokens.append(("NOT", "!"))
            elif char_str == "=":
                tokens.append(("EQUAL", "="))
            else:
                tokens.append(("ERROR_CHAR_NOT_DEFINED ", char_str))
            
        elif char[0] in ("(",")"):
            char_str = char

            if char_str == "(":
                tokens.append(("LPAREN","("))
            elif char_str == ")":
                tokens.append(("RPAREN",")"))
            else:
                tokens.append(("ERROR_CHAR_NOT_DEFINED ", char_str))
        else:
            tokens.append(("ERROR_TYPE_NOT_DEFINED", char))
        
        i += 1
    
    return tokens

def parse_assignment(token, var, pos):
    if pos+1 < len(token) and token[pos+1][0] == "EQUAL" and token[pos][0] == "IDENTIFIER":
        identifier = token[pos][1]
        pos += 2

        value, pos = parse_addition(token, var, pos)
        i = ("VARIABEL", identifier, value)

        return (i, pos)
    else:
        value, pos = parse_addition(token, var,pos)

        return (value, pos)

def parse_primary(token, var, pos):
    if pos >= len(token):
        raise SyntaxError("Unexpected end of input")
    tipe, nilai = token[pos]
    if tipe == "NUMBER":
        pos += 1
        
        return ((tipe,int(nilai)), pos)
    elif tipe == "LPAREN":
        if pos+1 < len(token) and token[pos +1][0] == "RPAREN":
            pos += 2
            
            return (None, pos)
             
        pos += 1
        value, pos = parse_addition(token, var, pos)
        
        if token[pos][0] == "RPAREN":
            pos += 1
            
            return value,pos
        else:
            raise SyntaxError(f"Expected ')', got {tipe}")
    elif tipe == "MINUS":
        pos += 1
        value, pos = parse_primary(token, var, pos)
        
        return value, pos
    elif tipe == "IDENTIFIER":
        pos += 1

        return ((tipe,nilai), pos)
    else:
        raise SyntaxError(f"Expected a type, got {tipe}")

def parse_unary(token, var, pos):
    if token[pos][0] == "MINUS":
        pos += 1
        
        primary, pos = parse_primary(token, var, pos)
        value = ("UMINUS",primary)

        return value, pos
    else:
        value, pos = parse_primary(token, var, pos)
        
        return (value, pos)


def parse_multiplication(token, var, pos):
    left, pos = parse_unary(token, var, pos)

    while pos < len(token) and token[pos][0] in ("TIMES", "DIVIDE"):
        op_type, op_val = token[pos]  
        pos += 1
        right, pos = parse_unary(token, var, pos)
        left = (op_type, left, right)

    return (left, pos)

def parse_addition(token, var, pos):
    left, pos = parse_multiplication(token, var, pos)
        
    while pos < len(token) and token[pos][0] in ("PLUS","MINUS"):
        op_type, op_val = token[pos]
        pos += 1
        right, pos = parse_multiplication(token, var, pos)
        left = (op_type, left, right)

    return (left, pos)

def evaluate(node,var):
    tipe = node[0]

    if tipe == "NUMBER":
        return node[1]
    elif tipe == "UMINUS":
        value = node[1]

        return -evaluate(value,var)
    elif tipe == "PLUS":
        left, right = node[1], node[2]

        return evaluate(left,var) + evaluate(right, var)
    elif tipe == "MINUS":
        left, right = node[1], node[2]

        return evaluate(left, var) - evaluate(right, var)
    elif tipe == "TIMES":
        left, right = node[1], node[2]

        return evaluate(left, var) * evaluate(right, var)
    elif tipe == "DIVIDE":
        left, right = node[1], node[2]

        return evaluate(left, var) / evaluate(right, var)
    elif tipe == "VARIABEL":
        name, value = node[1], node[2]
        var[name] = evaluate(value, var)
    elif tipe == "IDENTIFIER":
        nilai = node[1]
        
        if nilai in var:
            return var[nilai]
        else:
            raise SyntaxError(f"Error identifier no definited, got {nilai}")
    else:
        raise SyntaxError(f"expected OP type {tipe}")

def run(source):
    token = tokenize(source)
    print("Tokens:", token) 
    pos = 0
    
    while pos < len(token):
        value, pos = parse_assignment(token, variabel, pos)
        print("parse_assigment tuple return:", value)
        result = evaluate(value,variabel)
        print("var global: ", variabel)
        print()
        print("Result:", result)


# Test
a = "x = 5"
run(a)
# Test lebih kompleks
b = "x"
run(b)
