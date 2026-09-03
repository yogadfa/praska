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
        print()
        runing  = interpreter.evaluate(value)


# Test
a = 'print("lorem")'
run(a)
# Test lebih kompleks
b = "if(1 < 4) {if(a == 5){a+5}}"
#run(b)
