def paul(u):
    s = {'life': 0, 'eating': 1, 'Petes kata': 10, 'kata': 5}
    t = sum([s.get(c) for c in u])
    return 'Super happy!' if t < 40 else 'Happy!' if t < 70 else 'Sad!' if t < 100 else 'Miserable!'


    
