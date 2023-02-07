def is_string(data):
    return all(map(lambda x: type(x) == str, data))
