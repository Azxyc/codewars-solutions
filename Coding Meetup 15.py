def find_odd_names(u): 
    return [
        v for v in u
        if sum([ord(c) for c in v.get('firstName')])
        %2!=0
    ]
    
