from string import ascii_lowercase

gen = (ascii_lowercase[i]+ascii_lowercase[j] for i in range(len(ascii_lowercase)) for j in range(len(ascii_lowercase)))
for i in range(50):
    print(next(gen), end=' ')