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
