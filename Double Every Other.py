def double_every_other(u):
    return [
        2*v if u.index(v) % 2 != 0 else v
        for v in u
    ]
