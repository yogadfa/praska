import operator

ops = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul
}

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
            continue  # i sudah di posisi berikutnya
            
        elif char.isalpha():
            start = i
            while i < len(source) and source[i].isalpha():
                i += 1
            var_str = source[start:i]
            tokens.append(("IDENTIFIER", var_str))  # ✅ tambah kurung
            continue
            
        elif char == " ":
            pass
            
        elif char in op or char in boolean:
            start = i
            while i < len(source) and (source[i] in op or source[i] in boolean):
                i += 1
            char_str = source[start:i]
            
            if char_str == "==":
                tokens.append(("EQUALEQUAL", "=="))
            elif char_str == "!=":
                tokens.append(("NOTEQUALS", "!="))
            elif char_str == "<=":
                tokens.append(("LESSEQUAL", "<="))
            elif char_str == ">=":
                tokens.append(("GREATEREQUAL", ">="))
            elif char_str == "=":
                tokens.append(("EQUAL", "="))
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
            else:
                tokens.append(("ERROR_CHAR_NOT_DEFINED ", char_str))
            continue
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


def parse_primary(token, pos):
    if pos >= len(token):
        raise SyntaxError("Unexpected end of input")
    tipe, nilai = token[pos]
    if tipe == "NUMBER":
        pos += 1
        return (int(nilai), pos)
    elif tipe == "LPAREN":
        if pos+1 < len(token) and token[pos +1][0] == "RPAREN":
            pos += 2
            return (None, pos)
             
        pos += 1
        value, pos = parse_addition(token, pos)
        
        if token[pos][0] == "RPAREN":
            pos += 1
            return value,pos
        else:
            raise SyntaxError(f"Expected ')', got {tipe}")
    else:
        raise SyntaxError(f"Expected a number, got {tipe}")


def parse_multiplication(token, pos):
    left, pos = parse_primary(token, pos)

    while pos < len(token) and token[pos][0] in ("TIMES", "DIVIDE"):
        op_type, op_val = token[pos]  
        pos += 1
        right, pos = parse_primary(token, pos)
        left = (op_val, left, right)

    return (left, pos)

def parse_addition(token, pos):
    left, pos = parse_multiplication(token, pos)
        
    while pos < len(token) and token[pos][0] in ("PLUS","MINUS"):
        op_type, op_val = token[pos]
        pos += 1
        right, pos = parse_multiplication(token, pos)
        left = (op_val, left, right)

    return (left, pos)


def run(source):
    token = tokenize(source)
    print("Tokens:", token) 
    print()
    pos = 0
    while pos < len(token):
        value, pos = parse_addition(token, pos)
        print("Result:", value)


# Test
a = "()"
run(a)

# Test lebih kompleks
b = "(5+5)*6"
run(b)
