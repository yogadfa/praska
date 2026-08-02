def tokenize(source):
    tokens = []
    op = ["+","-","/","*","="]
    boolean = ["<",">","==","!=",">=","<=","!"]
    i = 0  # posisi karakter yang lagi dibaca
    
    while i < len(source):
        char = source[i]
        if char.isdigit():
           start = i
           while i < len(source) and source[i].isdigit():
             i+=1
             num = source[start:i]
             
             continue
           tokens.append(("NUMBER",int(num)))
           
        elif char.isalpha():
          start = i
          while i < len(source) and source[i].isalpha():
            i += 1
            
            var_str = source[start:i]
            
            continue
          tokens.append("IDENTIFIER",var_str)
            
        elif char == " ":
          pass
        elif char in op or char in boolean:
          start = i
          while i < len(source) and (source[i] in op or source[i] in boolean):
            i += 1
            
            char_str = source[start:i]
            
          if char_str == "==":
            tokens.append(("EQUALEQUAL","=="))
          elif char_str == "!=":
            tokens.append(("NOTEQUALS","!="))
          elif char_str == "<=":
            tokens.append(("LESSEQUAL","<="))
          elif char_str == ">=":
            tokens.append(("GREATEREQUAL",">="))
          elif char_str == "=":
            tokens.append(("EQUAL","="))
          elif char_str == "+":
            tokens.append(("PLUS","+"))
          elif char_str == "*":
            tokens.append(("TIMES","*"))
          elif char_str == "/":
            tokens.append(("divide","/"))
          elif char_str == ">":
            tokens.append(("GREATERTHAN",">"))
          elif char_str == "<":
            tokens.append(("LESSTHAN","<"))
          elif char_str == "-":
            tokens.append(("minus","-"))
          elif char_str == "!":
            tokens.append(("NOT","!"))
          else:
            tokens.append("ERROR_CHAR_NOT_DEFINITED")
          continue
        
        else:
          tokens.append("ERROR_TYPE_NOT_DEFINITED")
        
        
        i += 1  # maju ke karakter berikutnya
    
    return tokens
    
def run(source):
  code = tokenize(source)
  i = 0
  
  while i < len(code):
    break

a = "!="
print(tokenize(a))