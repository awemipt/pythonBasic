def tagAdder(tag):
    def add(s):
        return f"<{tag}>{s}</{tag}>"

    return add


tag = input()
s = input()

adder = tagAdder(tag)
print(adder(s))