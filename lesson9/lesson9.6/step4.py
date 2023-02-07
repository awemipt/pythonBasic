s = set(map(int,input().split()))
s = sorted(sorted(list(s))[-4:], reverse=True)
print(s)