def find_admin(u, l): 
    return [
        v for v in u
        if v.get('language') == l
        and v.get('githubAdmin') == 'yes'
    ]
