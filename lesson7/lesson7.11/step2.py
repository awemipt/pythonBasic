def show_menu(func):
    def wrapper(*args):
        menu = func(*args)
        for i, row in enumerate(menu):
            print(f"{i + 1}. {row}")
    return wrapper

@show_menu
def get_menu(s):
    return s.split()

s = input()
get_menu(s)