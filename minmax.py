def find_max_min(number):
   
    if max(number) == min(number):
        return [len(number)]
    return [min(number), max(number)]