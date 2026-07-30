def tokenize(source):
    tokens = []
    op = ["+","-","/","*","="]
    boolean = ["<",">","==","==="]
    i = 0  # posisi karakter yang lagi dibaca
    
    while i < len(source):
        char = source[i]
        if char.isdigit():
           start = i
           while i < len(source) and source[i].isdigit():
             i+=1
             num_str = source[start:i]
             
             continue
           tokens.append(f"NUMBER({num_str})")
           
        elif char.isalpha():
          start = i
          while i < len(source) and source[i].isdigit():
            i += 1
            
            var_str = source[start:i]
            
            continue
          tokens.append(f"IDENTIFIER({char})")
            
        elif char == " ":
          pass
        elif char in op or char in boolean:
          tokens.append(f"CHAR({char})")
        else:
          tokens.appenf("ERROR")
        
        
        i += 1  # maju ke karakter berikutnya
    
    return tokens

a = "10 + 5"
print(tokenize(a))