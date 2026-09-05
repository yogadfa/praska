#!/data/data/com.termux/files/usr/bin/python
import sys
import parser
import lexer
import interpreter

def run(source):
    token = lexer.tokenize(source)
    pos = 0
    
    while pos < len(token):
        value, pos = parser.statement(token, pos)
        runing  = interpreter.evaluate(value)

fileprk = sys.argv[1]

with open(fileprk, "r") as f:
    isi = f.read()

run(isi)

