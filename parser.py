
def assignment(token, pos):
    if pos+1 < len(token) and token[pos+1][0] == "EQUAL" and token[pos][0] == "IDENTIFIER":
        identifier = token[pos][1]
        pos += 2

        value, pos = parse_addition(token, pos)
        i = ("VARIABEL", identifier, value)

        return (i, pos)
    else:
        value, pos = parse_addition(token,pos)

        return (value, pos)

def parse_primary(token, pos):
    if pos >= len(token):
        raise SyntaxError("Unexpected end of input")
    tipe, nilai = token[pos]

    if pos+1 < len(token) and token[pos+1][0] == "EQUAL" and tipe != "IDENTIFIER":
        raise SyntaxError(f"Cannot assign to a {tipe}")
    
    if tipe == "NUMBER":
        pos += 1
        
        return ((tipe,int(nilai)), pos)
    elif tipe == "LPAREN":
        if pos+1 < len(token) and token[pos +1][0] == "RPAREN":
            pos += 2
            
            return (None, pos)
             
        pos += 1
        value, pos = parse_addition(token, pos)
        
        if pos < len(token) and token[pos][0] == "RPAREN":
            pos += 1
            
            return value,pos
        else:
            raise SyntaxError(f"Expected ')'")
    elif tipe == "MINUS":
        pos += 1
        value, pos = parse_primary(token, pos)
        
        return value, pos
    elif tipe == "IDENTIFIER":
        pos += 1

        return ((tipe,nilai), pos)
    else:
        raise SyntaxError(f"Expected a type, got {tipe}")

def parse_unary(token, pos):
    if pos > len(token):
        raise SyntaxError("Unexpected end of input")
    
    if token[pos][0] == "MINUS":
        pos += 1
        
        primary, pos = parse_primary(token, pos)
        value = ("UMINUS",primary)

        return value, pos
    else:
        value, pos = parse_primary(token, pos)
        
        return (value, pos)


def parse_multiplication(token, pos):
    left, pos = parse_unary(token, pos)

    while pos < len(token) and token[pos][0] in ("TIMES", "DIVIDE"):
        op_type, op_val = token[pos]  
        pos += 1
        right, pos = parse_unary(token, pos)
        left = (op_type, left, right)

    return (left, pos)

def parse_addition(token, pos):
    left, pos = parse_multiplication(token, pos)
        
    while pos < len(token) and token[pos][0] in ("PLUS","MINUS"):
        op_type, op_val = token[pos]
        pos += 1
        right, pos = parse_multiplication(token, pos)
        left = (op_type, left, right)

    return (left, pos)

