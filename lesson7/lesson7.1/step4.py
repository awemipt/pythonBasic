def foo(name, surname):
    print(f"Уважаемый, {name} {surname}! Вы верно выполнили это задание!")


name, surname = input().split()
foo(name,surname)