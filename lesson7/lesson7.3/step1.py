def get_nod(a, b):
    if a < b:
        b, a = a, b
    while b != 0:
        a, b = b, a % b
    return a


print(get_nod(100,2))