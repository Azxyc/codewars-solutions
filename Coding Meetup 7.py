def find_senior(u): 
    return [x for x in u
            if x.get('age')
            == max([v.get('age')
                    for v in u])
           ]
    
