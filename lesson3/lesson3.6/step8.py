name = input()
author = input()
lists = int(input())
price = float(input())
book = [name, author, lists, price]
del book[2]
book[1] = 'Пушкин'
book[-1] *= 2
print(book)