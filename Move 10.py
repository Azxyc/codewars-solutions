def move_ten(o):
    return ''.join([
        chr(ord(c)+10)
        if ord(c) in [x for x in range(97,113)]
        else chr(ord(c)-16)
        for c in o
    ])
    
