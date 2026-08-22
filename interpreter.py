from asyncio import Condition
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
    elif tipe == "IF":
      condition= node[1]
      block = node[2]
      condition = evaluate(condition)

      if condition == True:
        value = []
        for stmt in block:
          value.append(evaluate(stmt))
        return evaluate(stmt)
      else:
        return None
    elif tipe == "VARIABEL":
        name, value = node[1], node[2]
        var[name] = evaluate(value)
    elif tipe == "IDENTIFIER":
        nilai = node[1]
        print(var)

        if nilai in var:
            return var[nilai]
        else:
            raise SyntaxError(f"Error identifier no definited, got {nilai}")
    else:
        raise SyntaxError(f"expected OP type {tipe}")
