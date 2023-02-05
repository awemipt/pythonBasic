names = tuple(input().split())
for name in names:
    if 'ва' in name[:2].lower() :
        print(name.lower(), end=' ')