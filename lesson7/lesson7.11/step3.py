def sortDecor(func):
    def wrapper(*args):
        ans = sorted(func(*args))
        return ans

    return wrapper


@sortDecor
def get_list(string):
    return list(map(int, string.split()))


s = input()
lst = get_list(s)
print(*lst)