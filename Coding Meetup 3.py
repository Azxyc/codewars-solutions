def is_ruby_coming(u): 
    return True if len(
        [v for v in u
         if v.get('language') == "Ruby"]
    ) >= 1 else False
