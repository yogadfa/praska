import parser
import lexer
import interpreter

def run(source):
    token = lexer.tokenize(source)
    print("Tokens:", token) 
    pos = 0
    
    while pos < len(token):
        value, pos = parser.assignment(token, pos)
        print("parse_assigment tuple return:", value)
        result = interpreter.evaluate(value)
        print()
        print("Result:", result)


# Test
a = "if(){}"
run(a)
# Test lebih kompleks
b = ">="
#run(b)
