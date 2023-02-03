number = int(input())
prod = 1
while number > 0:
    prod *= number % 10
    number//=10
print(prod)