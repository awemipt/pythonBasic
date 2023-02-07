rivers = input().split()
rivers.sort(reverse=True,key=len)
print(*rivers)