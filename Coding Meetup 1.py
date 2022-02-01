def count_developers(u):
    return len(([v for v in u
                 if v.get('continent') == 'Europe'
                and v.get('language') == 'JavaScript'
                         ]))
