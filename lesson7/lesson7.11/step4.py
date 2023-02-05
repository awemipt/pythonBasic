def todict(func):
    def wrapper(*args):
        l1, l2 = func(*args)
        d = {a: b for a, b in zip(l1, l2)}
        return d

    return wrapper


@todict
def tolists(s1, s2):
    return s1.split(), s2.split()


s1 = input()
s2 = input()
d = tolists(s1, s2)
print(*sorted(d.items()))
