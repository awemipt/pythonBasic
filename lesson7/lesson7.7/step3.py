def get_rec_sum(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + get_rec_sum(lst[1:])

lst = list(map(int, input().split()))
print(get_rec_sum(lst))