def find_short(s):
    return sorted([len(v) for v in s.split(' ')])[0]
