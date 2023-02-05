def countPerimeter(width, height):
    print(f"Периметр прямоугольника, равен {2 * (width + height)}")


x, y = map(int, input().split())
countPerimeter(x, y)
