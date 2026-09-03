import parser
import lexer
import interpreter

def run(source):
    token = lexer.tokenize(source)
    pos = 0
    
    while pos < len(token):
        value, pos = parser.statement(token, pos)
        runing  = interpreter.evaluate(value)


# Test
code = 'println("lorem") print("ipsum")'
run(code)

