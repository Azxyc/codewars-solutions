def count_languages(u): 
    k= dict.fromkeys(
        list(
            set(
                [v.get('language')
                  for v in u]
        )))      
    for a in k:
        k[a] = [v.get('language')
            for v in u].count(a)
    return k
