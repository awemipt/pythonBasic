lst = list(input())
lst.remove('+')
lst.remove("-")
lst.remove("-")
lst[0] = "8"
print("".join(lst))