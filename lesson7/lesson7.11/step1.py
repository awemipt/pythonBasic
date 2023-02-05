def func_show(func):
    def wrapper(*args):
        ans = func(*args)
        print(f"Площадь прямоугольника: {ans}")
        return ans
    return wrapper

def get_sq(width, height):
    return width * height
