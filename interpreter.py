def evaluate(node, var):
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
