def calc(x):
    return sum(
        [int(t)
         for t in
         ''.join(str(ord(c))
                 for c in x)
        ])-sum(
        [int(t)
         for t in
         ''.join([str(ord(c))
                 for c in x]).replace('7','1')
        ])
    
    
