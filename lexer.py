def tokenize(source):
    tokens = []
    op = ["+", "-", "/", "*", "="]
    boolean = ["<", ">", "==", "!=", ">=", "<=", "!"]
    KEYWORDS ={
        "if":"IF",
        "else":"ELSE",
        "elif":"ELIF"
    }
    
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
            if var_str in KEYWORDS:
                tokens.append((KEYWORDS[var_str],var_str))
            else:
                tokens.append(("IDENTIFIER", var_str))
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
                tokens.append(("NOTEQUAL", "!="))
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
            continue
            
        elif char[0] in ("(",")","{","}"):
            char_str = char

            if char_str == "(":
                tokens.append(("LPAREN","("))
            elif char_str == ")":
                tokens.append(("RPAREN",")"))
            elif char_str == "{":
                tokens.append(("LBRACE","{"))
            elif char_str == "}":
                tokens.append(("RBRACE","}"))
            else:
                tokens.append(("ERROR_CHAR_NOT_DEFINED ", char_str))
        else:
            tokens.append(("ERROR_TYPE_NOT_DEFINED", char))
        
        i += 1
    
    return tokens
