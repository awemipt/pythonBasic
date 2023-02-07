from string import ascii_lowercase, ascii_uppercase

chars = ascii_lowercase + ascii_uppercase
import random

random.seed(1)


def randomEmail(N, domen='@mail.ru'):
    while True:
        email = ""
        for i in range(N):
            email += chars[random.randint(0, len(chars) - 1)]
        email += domen
        yield email


N = int(input())
gen = randomEmail(N)
for i in range(5):
    print(next(gen))
