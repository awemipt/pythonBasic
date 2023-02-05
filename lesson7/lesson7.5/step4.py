def get_biggest_city(*args):
    lens = [len(city) for city in args]
    m = max(lens)
    return args[lens.index(m)]