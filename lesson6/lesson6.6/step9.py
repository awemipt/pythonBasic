text = input().lower()
words = set(text.split())
count = {word:text.count(word) for word in words}
count.setdefault('и', 0)
print(count['и'])