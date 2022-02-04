def odd_ones_out(u):
    return [v for v in u if not u.count(v) % 2 ]
