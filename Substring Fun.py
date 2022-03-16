def nth_char(v):
    u, x = [], 0
    for t in v:
        u.append(t[x])
        x+=1
    return ''.join(u)
    
    
