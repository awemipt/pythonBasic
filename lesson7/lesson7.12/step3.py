t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def advancedToCirilic(replace=" !?"):
    def wrap1(func):
        def wrapper(*args):
            s = func(*args)
            for sym in s:
                if sym in replace:
                    s = s.replace(sym, '-')
            while s.find('--') != -1:
                s = s.replace('--','-')
            return s
        return wrapper
    return wrap1

@advancedToCirilic('"?!:;,. "')
def toCirilic(s):
    res = ''
    for sym in s.lower():
        if sym in t:
            res += t[sym]
        else:
            res += sym
    return res

s = input()
print(toCirilic(s))