def merge(list1, list2):
    i = 0
    j = 0
    ans = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            ans.append(list1[i])
            i += 1
        else:
            ans.append(list2[j])
            j += 1
    while j < len(list2):
        ans.append(list2[j])
        j += 1
    while i < len(list1):
        ans.append(list1[i])
        i += 1
    return ans


def mergesort(lst):
    if len(lst) == 1:
        return lst
    return merge(mergesort(lst[:len(lst) // 2]), mergesort(lst[len(lst) // 2:]))

print(mergesort([10,1,2,3,13]))
