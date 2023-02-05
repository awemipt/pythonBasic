def lister(tp='list'):
    def tolist(*args):

        nonlocal tp
        if tp == 'list':
            return list(*args)
        else:
            return tuple(*args)

    return tolist


s = input()
nums = list(map(int, input().split()))
lst = lister(s)(nums)
print(lst)
