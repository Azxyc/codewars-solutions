def is_same_language(u): 
    return True if len(
        set([v.get('language') for v in u])
    ) == 1 else False
