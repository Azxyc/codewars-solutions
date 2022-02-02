def find_outlier(i):
    return (
        [x for x in i
         if x%2 !=0 ]
        [0]
        if len([x for x in i if x%2 !=0 ])
        == 1 else
        [x for x in i if x%2 == 0 ]
        [0]
    )
