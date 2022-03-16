def is_nice(arr):
    if len(arr) == 0: return False
    return len(
        [True
         for n in arr
         if n+1 in arr
         or n-1 in arr
        ]) == len(arr)
            
