s = input()
word = "ра"
indexes = []
for i in range(len(s)):
    if s.find(word, i) == -1:
        break
    elif s.find(word, i) not in indexes:
        indexes.append(s.find(word, i))
if not indexes:
    indexes.append(-1)
print(*indexes)