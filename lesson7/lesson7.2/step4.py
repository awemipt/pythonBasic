def is_even(x):
    return x % 2 == 0


t = 0
while t != 1:
    t = int(input())
    if is_even(t):
        print(t)
