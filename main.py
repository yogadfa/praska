#!/data/data/com.termux/files/usr/bin/python
import sys
import parser
import lexer
import interpreter
import debug

def run(source):
    token = lexer.tokenize(source)
    pos = 0
    
    while pos < len(token):
        value, pos = parser.statement(token, pos)
        runing  = interpreter.evaluate(value)

for item in sys.argv:
    if item.endswith(".prk"):
        fileprk = item

with open(fileprk, "r") as f:
    isi = f.read()

if "--debug" in sys.argv:
     debug.run(isi)
else:
     run(isi)

