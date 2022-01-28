def word_to_bin(u):
    return [bin(ord(v)).replace('b','') for v in u]
