def tagging(s, tag='h1',up=True):
    if up:
        tag = tag.upper()
    return f'<{tag}>{s}</{tag}>'

s = input()
print(tagging(s,tag='div'))
print(tagging(s,tag='div',up=False))