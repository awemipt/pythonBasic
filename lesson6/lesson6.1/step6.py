
d = input().split()
d = [x.split("=") for x in d]
d = [[z,x] for z,x in d]
d = dict(d)
if 'False' in d:
    del d['False']
if '3' in d:
    del d['3']
print(*sorted(d.items()))