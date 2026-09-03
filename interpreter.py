var = {}

def evaluate(node):
    tipe = node[0]

    if tipe == "NUMBER":
        return node[1]
    elif tipe == "UMINUS":
        value = node[1]

        return -evaluate(value)
    elif tipe == "PLUS":
        left, right = node[1], node[2]

        return evaluate(left) + evaluate(right)
    elif tipe == "MINUS":
        left, right = node[1], node[2]

        return evaluate(left) - evaluate(right)
    elif tipe == "TIMES":
        left, right = node[1], node[2]

        return evaluate(left) * evaluate(right)
    elif tipe == "DIVIDE":
        left, right = node[1], node[2]

        return evaluate(left) / evaluate(right)
    elif tipe == "EQUALEQUAL":
      left, right = node[1], node[2]

      return evaluate(left) == evaluate(right)
    elif tipe == "NOTEQUAL":
      left, right = node[1], node[2]

      return evaluate(left) != evaluate(right)
    elif tipe == "LESSTHAN":
      left, right = node[1], node[2]

      return evaluate(left) < evaluate(right)
    elif tipe == "GREATERTHAN":
      left, right = node[1], node[2]

      return evaluate(left) > evaluate(right)
    elif tipe == "LESSEQUAL":
      left, right = node[1], node[2]

      return evaluate(left) <= evaluate(right)
    elif tipe == "GREATEREQUAL":
      left, right = node[1], node[2]

      return evaluate(left) >= evaluate(right)
    elif tipe == "PLUSEQUAL":
        indetifier, incrby = node[1], node[2]

        if indetifier in var:
            var[indetifier] += evaluate(incrby)
        else:
            raise SyntaxError(f"IDENTIFIER not definited, got {identifier}" )
    elif tipe == "MINUSEQUAL":
        indetifier, incrby = node[1], node[2]

        if indetifier in var:
            var[indetifier] += evaluate(incrby)
        else:
            raise SyntaxError(f"IDENTIFIER not definited, got {identifier}")
    elif tipe == "IF":
      condition= node[1]
      block = node[2]
      condition = evaluate(condition)

      if condition == True:
        value = []
        for stmt in block:
          value.append(evaluate(stmt))
        return value
      else:
        return None
    elif tipe == "FOR":
        init, cond, incr, block = node[1], node[2], node[3], node[4]

        if init != None:
            init = evaluate(init)

        if cond == None or evaluate(cond):
           value = []
           while cond == None or evaluate(cond):
                evaluate(incr)
                for stmt in block:
                    value.append(evaluate(stmt))
           return value

    elif tipe == "WHILE":
        cond, block = node[1], node[2]

        if cond == None or evaluate(cond):
            value = []
            while cond == None or evaluate(cond):
                for stmt in block:
                    value.append(evaluate(stmt))
            return value
        
    elif tipe == "VARIABEL":
        name, value = node[1], node[2]
        var[name] = evaluate(value)
    elif tipe == "IDENTIFIER":
        nilai = node[1]

        if nilai in var:
            return var[nilai]
        else:
            raise SyntaxError(f"Error identifier no definited, got {nilai}")
    elif tipe == "STRING":
        value = node[1]

        return value
    elif tipe == "PRINT":
        value = node[1]
        print(evaluate(value), end = "")
    else:
        raise SyntaxError(f"expected OP type {tipe}")
