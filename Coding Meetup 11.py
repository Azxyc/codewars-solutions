
def get_average(u): 
    return round(sum(
    [
        v.get('age')
        for v in u

    ])/len(u))
    
