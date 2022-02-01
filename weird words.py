def next_letter(y):
    return ''.join([(chr(ord(x)+1)
                     if x in 'abcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXY'
                     else (x if x not in 'Zz'
                           else ('a' if x == 'z' 
                                 else 'A'))) for x in y])
   
