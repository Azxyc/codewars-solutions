def all_continents(u): 
    return len(
        set([v.get('continent') for v in u])
    ) == 5
