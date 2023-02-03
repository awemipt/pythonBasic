d = input().split()
d = [x.split("=") for x in d]
d = [[z,int(x)] for z,x in d]
d = dict(d)
print(*sorted(d.items()))