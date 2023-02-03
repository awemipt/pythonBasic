lst = list(map(int, input().split()))
ans = []
ans.append(min(lst))
lst.remove(min(lst))
ans.append(min(lst))
lst.remove(min(lst))
ans.append(min(lst))
lst.remove(min(lst))
print(ans)