def validate_word(w):
    return(
        True
        if len(list(set([w.lower().count(x)
                         for x in list(set(list(w.lower())))])))
        == 1 else False
    )
    
