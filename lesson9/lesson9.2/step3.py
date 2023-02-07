import random
from string import ascii_lowercase, ascii_uppercase
chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
# установка зерна датчика случайных чисел (не менять)
random.seed(1)

# здесь продолжайте программу
def passwords(N):
    while True:
        psw = ''
        for i in range(N):
            psw += chars[random.randint(0, len(chars)-1)]
        yield psw


N = int(input())
for i in range(5):
    print(next(passwords(N)))