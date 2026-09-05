boolean = ("LESSTHAN", "GREATERTHAN", "EQUALEQUAL", "NOTEQUAL", "LESSEQUAL", "GREATEREQUAL")

def parse_assignment(token, pos):
    if pos+1 < len(token) and token[pos+1][0] in ("EQUAL","MINUSEQUAL","PLUSEQUAL") and token[pos][0] == "IDENTIFIER":
        tipe = token[pos+1][0]
        identifier = token[pos][1]
        pos += 2

        value, pos = parse_addition(token, pos)
        if tipe == "EQUAL":
            result = ("VARIABEL", identifier, value)

            return (result, pos)
        elif tipe == "PLUSEQUAL":
            result = ("PLUSEQUAL", identifier, value)

            return (result, pos)
        elif tipe == "MINUSEQUAL":
            result = ("MINUSEQUAL", identifier, value)

            return (result, pos)
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
    elif tipe == "SEMICOLON":
        pos += 1
        
        return (tipe, nilai)
    elif tipe == "IDENTIFIER":
        pos += 1
        
        return ((tipe,nilai), pos)
    elif tipe in ("PLUSEQUAL","MINUSEQUAL"):
        if tipe == "PLUSEQUAL":
            return (tipe,nilai),pos
        elif tipe == "MINUSEQUAL":
            return (tipe,nilai),pos
        else:
            raise SyntaxError(f"Expected a type, got {tipe}")
    elif tipe == "STRING":
        pos += 1
        return (tipe, nilai), pos

def parse_unary(token, pos):
    if pos >= len(token):
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
    elif token[pos][0] == "FOR":
        return parse_for(token, pos)
    elif token[pos][0] == "WHILE":
        return parse_while(token, pos)
    elif token[pos][0] == "PRINT":
        return parse_print(token, pos)
    elif token[pos][0] == "PRINTLN":
        return parse_println(token, pos)
    else:
        return parse_assignment(token,pos)

def parse_block(token,pos):
    statements = []
    if token[pos][0] == "LBRACE":
        pos += 1
        
        while pos < len(token) and token[pos][0] != "RBRACE":
            stmt, pos = statement(token,pos)
            statements.append(stmt)
    else:
        raise SyntaxError("Expected '{'")

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
            raise SyntaxError("Expected ')'")

        return (("IF",comparison_value,block_value), pos)
    else:
        raise SyntaxError("Expected '(' in after IF")

def parse_for(token, pos):
    pos += 1
    
    if pos < len(token) and token[pos][0] == "LPAREN":
        pos += 1
        if token[pos][0] != "SEMICOLON":
          init, pos = parse_assignment(token,pos)
          pos += 1
        else:
            init = None
            pos += 1
            
        if pos < len(token) and token[pos][0] != "SEMICOLON":
            cond, pos= parse_comparison(token, pos)
            pos += 1
        else:
            cond = None
            pos += 1
            

        if pos < len(token) and token[pos][0] != "RPAREN":
            incr, pos = parse_assignment(token, pos)
            if pos < len(token) and token[pos][0] == "RPAREN":
                pos += 1
            else:
                raise SyntaxError("Expected ')' after FOR")
        else:
            incr = None
            pos += 1

        block, pos = parse_block(token, pos)
    else:
        raise SyntaxError("Expected '(' after FOR")
        
    return ("FOR", init, cond, incr, block), pos

def parse_while(token, pos):
    pos += 1

    if pos < len(token) and token[pos][0] == "LPAREN":
        pos += 1

        cond, pos = parse_comparison(token, pos)
        
        if pos < len(token) and token[pos][0] == "RPAREN":
            pos += 1
            block, pos = parse_block(token, pos)

            return ("WHILE", cond, block), pos
        else:
            raise SyntaxError("Expected ')' after WHILE")
    else:
        raise SyntaxError("Expected '(' after WHILE")
        

def parse_comparison(token, pos):
    left, pos = parse_addition(token,pos)

    while pos < len(token) and token[pos][0] in boolean:
        bool_type = token[pos][0]
        pos += 1
        right, pos = parse_addition(token,pos)
        left = (bool_type, left, right)
    return left, pos

def parse_print(token, pos):
    pos += 1

    if pos < len(token) and token[pos][0] == "LPAREN":
        value, pos = parse_assignment(token, pos)

        return ("PRINT", value), pos
    else:
        raise SyntaxError("Expected '(' after PRINT")

def parse_println(token, pos):
    pos += 1

    if pos < len(token) and token[pos][0] == "LPAREN":
        value, pos = parse_assignment(token, pos)

        return ("PRINTLN", value), pos
    else:
         raise SyntaxError("Expected '(' after PRINTLN")
