def tagging(s, tag='h1'):
    return f'<{tag}>{s}</{tag}>'

s = input()
print(tagging(s))
print(tagging(s,tag='div'))