def get_add(a, b):
    if isinstance(a, str) and isinstance(b, str):
        return a + b
    elif isinstance(a, (float, int)) and isinstance(b, (float, int)):
        return a + b
    else:
        return None
