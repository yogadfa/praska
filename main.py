import parser
import lexer
import interpreter

def run(source):
    token = lexer.tokenize(source)
    print("Tokens:", token) 
    pos = 0
    
    while pos < len(token):
        value, pos = parser.statement(token, pos)
        print("parser.statement tuple return:", value)
        result = interpreter.evaluate(value)
        print()
        print("Result:", result)


# Test
a = "if(5 < 6) {a = 5+1}"
run(a)
# Test lebih kompleks
b = "if(8 <= 8) {b = a-1}"
#run(b)
