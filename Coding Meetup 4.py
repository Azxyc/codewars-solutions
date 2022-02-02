def get_first_python(u):
    try:
        return(
            ([v['first_name'] +
              ', '+
              v['country']
              for v in u
              if v['language']
              == 'Python'])
            [0]
        )
    except:
        return 'There will be no Python developers'
