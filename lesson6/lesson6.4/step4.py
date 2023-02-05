word = list(input().split())
word = [s.lower() for s in word]
print(len(set(word)))