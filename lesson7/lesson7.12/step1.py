def decor1(start):
    def decor2(func):
        def wrapper(*args):
            return start + func(*args)

        return wrapper

    return decor2

@decor1(5)
def Sum(s):
    return sum([int(x) for x in s.split()])


s = input()
print(Sum(s))