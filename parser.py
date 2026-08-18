boolean = ("LESSTHAN", "GREATERTHAN", "EQUALEQUAL", "NOTEQUALS", "LESSEQUAL", "GREATEREQUAL")

def parse_assignment(token, pos):
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

def statement(token,pos):
    if token[pos][0] == "IF":
        return parse_if(token, pos)
    else:
        return parse_assignment(token,pos)

def parse_block(token,pos):
    statements = []
    if token[pos][0] == "LBRACE":
        pos += 1
        
        while pos < len(token) and token[pos][0] != "RBRACE":
            stmt, pos = statement(token,pos)
            statements.append(stmt)

    if token[pos][0] == "RBRACE":
        pos +=1
        return statements, pos
    else:
        raise SyntaxError("Expected '}'")

def parse_if(token,pos):
    pos += 1

    if token[pos][0] == "LPAREN":
        pos += 1
        comparison_value, pos = parse_comparison(token,pos)
        
        if pos < len(token) and token[pos][0] == "RPAREN":
            pos += 1

            if pos < len(token) and token[pos][0] == "LBRACE":
                block_value, pos= parse_block(token, pos)
            else:
                raise SyntaxError("Expected '{' after IF")
        else:
            raise SyntaxError("Unexpected ')'")

        return (("IF",comparison_value,block_value), pos)
    else:
        raise SyntaxError("Expected '(' in after IF")

def parse_comparison(token, pos):
    left, pos = parse_addition(token,pos)

    while pos < len(token) and token[pos][0] in boolean:
        bool_type = token[pos][0]
        pos += 1
        right, pos = parse_addition(token,pos)
        left = (bool_type, left, right)
    return left, pos
