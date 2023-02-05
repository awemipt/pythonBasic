def addTag(tag='h1'):
    return lambda func: lambda *args: f'<{tag}>{func(*args)}</{tag}>'



@addTag('div')
def f(s):
    return s.lower()


s = input()
print(f(s))
