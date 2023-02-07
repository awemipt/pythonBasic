notes = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
ord = range(7)
d = dict(zip(notes, ord))
music = input().split()
music.sort(key=lambda x: d[x])
print(*music)
