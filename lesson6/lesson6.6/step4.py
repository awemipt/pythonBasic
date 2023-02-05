word = input().split()
s = {w.lower() for w in word if not (len(w) < 3)}
print(len(s))
