def tagAdder(tag):
    def add(s):
        return f"<{tag}>{s}</{tag}>"

    return add


s = input()
adder = tagAdder('h1')
print(adder(s))