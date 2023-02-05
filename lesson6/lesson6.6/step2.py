marks = input().split()
num0 = int(marks[0])
d = {i: mark for i, mark in zip(range(num0, num0 + len(marks)-1),marks[1:]) }
print(d[4])