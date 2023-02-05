t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

df = set(': ;.,_')


def advancedToCirilic(func):
    def wrapper(*args):
        ans = func(*args)
        while ans.find('--') != -1:
            ans = ans.replace('--', '-')
        return ans
    return wrapper

@advancedToCirilic
def toCirilic(s):
    ans = ""
    for i in s.lower():
        if i in t:
            ans += t[i]
        elif i in df:
            ans += '-'
        else:
            ans +=i
    return ans


print(toCirilic('абс   s'))