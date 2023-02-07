marks = map(lambda x: int(x)<3, input().split())
print('отчислен' if any(marks) else 'учится')