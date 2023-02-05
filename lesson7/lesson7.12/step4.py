from functools import wraps


def summator(func):
    @wraps(func)
    def wrapper(lst, *args, **kwargs):
        l = func(lst, *args, **kwargs)
        return sum(l)

    return wrapper


@summator
def get_list(s):
    '''Функция для формирования списка целых значений'''
    return [int(x) for x in s.split()]


