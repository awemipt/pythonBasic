s = input()
s = s.replace(" ", "")
s = s.replace("+", '_+')
s = s.replace("-", "_-")
numbers = map(int, s.split("_"))
print(sum(numbers))
